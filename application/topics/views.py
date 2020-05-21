from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.topics.models import Topic
from application.topics.forms import TopicForm
from application.posts.models import Post
from application.posts.forms import PostForm


@app.route("/topics", methods=["GET"])
@login_required
def topics_index():
    return render_template("topics/list.html", topics=Topic.query.all())


@app.route("/topics/<topic_id>", methods=["GET"])
@login_required
def topics_view(topic_id):
    topic = Topic.query.get(topic_id)

    if topic is None:
        return redirect(url_for("topics_index"))

    return render_template("topics/single.html", topic=topic, form=PostForm())


@app.route("/topics/new")
@login_required
def topics_form():
    return render_template("topics/new.html", form=TopicForm())


@app.route("/topics", methods=["POST"])
@login_required
def topics_create():
    form = TopicForm(request.form)

    if not form.validate():
        return render_template("topics/new.html", form=form)

    subject = form.subject.data
    body = form.body.data

    initial_post = Post(body)
    initial_post.author_id = current_user.id
    topic = Topic(subject)
    topic.posts.append(initial_post)

    db.session().add(topic)
    db.session().commit()

    return redirect(url_for("topics_index"))
