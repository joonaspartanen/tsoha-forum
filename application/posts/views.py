from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.posts.models import Post
from application.posts.forms import PostForm
from application.topics.models import Topic


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


@app.route("/posts/<post_id>/likes", methods=["PUT"])
@login_required
def like_post(post_id):
    post = Post.query.get(post_id)

    if current_user not in post.likedByUsers:
        post.likedByUsers.append(current_user)
        db.session().commit()

        resp = jsonify(success=True)
        return resp

    resp = jsonify(success=False)
    return resp


@app.route("/posts/<post_id>/likes", methods=["DELETE"])
@login_required
def unlike_post(post_id):
    post = Post.query.get(post_id)

    if current_user in post.likedByUsers:
            post.likedByUsers.remove(current_user)
            db.session().commit()

            resp = jsonify(success=True)
            return resp

    resp = jsonify(success=False)
    return resp
