from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.posts.models import Post
from application.posts.forms import PostForm
from application.topics.models import Topic


@app.route("/topics/<topic_id>/posts", methods=["POST"])
@login_required
def posts_create(topic_id):
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

    return redirect(url_for("topics_view", topic_id=topic_id))


@app.route("/posts/<post_id>/likes", methods=["PUT"])
@login_required
def posts_like(post_id):
    post = Post.query.get(post_id)
    post.likes += 1
    db.session().commit()

    resp = jsonify(success=True)
    return resp


@app.route("/posts/<post_id>/likes", methods=["DELETE"])
@login_required
def posts_unlike(post_id):
    post = Post.query.get(post_id)
    post.likes -= 1
    db.session().commit()

    resp = jsonify(success=True)
    return resp
