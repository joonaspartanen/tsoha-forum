from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.posts.models import Post
from application.posts.forms import PostForm
from application.topics.models import Topic
from application.auth.services import UserService


@app.route("/topics/<topic_id>/posts", methods=["POST"])
@login_required
def create_post(topic_id):
    topic = Topic.query.get(topic_id)

    if topic is None:
        return redirect(url_for("topics_index"))

    form = PostForm(request.form)

    if not form.validate():
        return render_template("topics/single.html", topic=topic, form=form)

    body = request.form.get("body")
    post = Post(body)
    post.topic = topic
    post.author_id = current_user.id

    db.session().add(post)
    db.session().commit()

    return redirect(url_for("view_topic", topic_id=topic_id))


@app.route("/topics/<topic_id>/posts/<post_id>/edit", methods=["GET"])
@login_required
def view_edit_post_form(post_id, topic_id):
    post = Post.query.get(post_id)

    if post is None:
        return redirect(url_for("view_topic", topic_id=topic_id))

    if UserService.user_not_admin_nor_editing_own_content(post.author_id):
        return redirect(url_for("view_topic", topic_id=topic_id))

    form = PostForm()
    form.body.data = post.body
    return render_template("posts/edit_post.html", post=post, form=form)


@app.route("/topics/<topic_id>/posts/<post_id>", methods=["POST"])
@login_required
def edit_post(post_id, topic_id):
    post_in_db = Post.query.get(post_id)

    if post_in_db is None:
        return redirect(url_for("view_topic", topic_id=topic_id))

    if UserService.user_not_admin_nor_editing_own_content(post_in_db.author_id):
        return redirect(url_for("view_topic", topic_id=topic_id))

    form = PostForm(request.form)
    if not form.validate():
        return render_template("posts/edit_post.html", post=post_in_db, form=form)

    post_in_db.body = form.body.data
    db.session.commit()

    return redirect(url_for("view_topic", topic_id=topic_id))


@app.route("/topics/<topic_id>/posts/<post_id>", methods=["DELETE"])
@login_required
def delete_post(post_id, topic_id):
    post = Post.query.get(post_id)

    if post is None:
        return redirect(url_for("view_topic", topic_id=topic_id))

    if UserService.user_not_admin_nor_editing_own_content(post.author_id):
        return redirect(url_for("view_topic", topic_id=topic_id))

    db.session().delete(post)
    db.session.commit()

    resp = jsonify(success=True)
    return resp


@app.route("/topics/<topic_id>/posts/<post_id>/likes", methods=["PUT"])
@login_required
def like_post(post_id, topic_id):
    post = Post.query.get(post_id)

    if current_user not in post.liked_by_users:
        post.liked_by_users.append(current_user)
        db.session().commit()

        resp = jsonify(success=True)
        return resp

    resp = jsonify(success=False)
    return resp


@app.route("/topics/<topic_id>/posts/<post_id>/likes", methods=["DELETE"])
@login_required
def unlike_post(post_id, topic_id):
    post = Post.query.get(post_id)

    if current_user in post.liked_by_users:
        post.liked_by_users.remove(current_user)
        db.session().commit()

        resp = jsonify(success=True)
        return resp

    resp = jsonify(success=False)
    return resp
