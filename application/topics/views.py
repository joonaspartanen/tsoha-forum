from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from application.topics.models import Topic
from application.posts.models import Post


@app.route("/topics", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics=Topic.query.all())


@app.route("/topics/<topic_id>", methods=["GET"])
def topic_view(topic_id):
    topic = Topic.query.get(topic_id)

    if topic is None:
        return redirect(url_for("topics_index"))

    return render_template("topics/single.html", topic=topic)


@app.route("/topics/new")
def topics_form():
    return render_template("topics/new.html")


@app.route("/topics", methods=["POST"])
def topics_create():
    subject = request.form.get("subject")
    body = request.form.get("body")

    initial_post = Post(body)
    topic = Topic(subject)
    topic.posts.append(initial_post)

    db.session().add(topic)
    db.session().commit()

    return redirect(url_for("topics_index"))
