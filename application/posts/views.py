from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from application.posts.models import Post
from application.topics.models import Topic


@app.route("/topics/<topic_id>/posts", methods=["POST"])
def posts_create(topic_id):

    topic = Topic.query.get(topic_id)

    if topic is None:
        return redirect(url_for("topics_index"))

    body = request.form.get("body")
    post = Post(body)
    post.topic = topic

    db.session().add(post)
    db.session().commit()

    return redirect(url_for("topic_view", topic_id=topic_id))


@app.route("/posts/<post_id>/likes", methods=["PUT"])
def posts_like(post_id):
    post = Post.query.get(post_id)
    post.likes += 1
    db.session().commit()

    resp = jsonify(success=True)
    return resp


@app.route("/posts/<post_id>/likes", methods=["DELETE"])
def posts_unlike(post_id):
    post = Post.query.get(post_id)
    post.likes -= 1
    db.session().commit()

    resp = jsonify(success=True)
    return resp
