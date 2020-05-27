from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc
from application.topics.models import Topic
from application.topics.forms import TopicForm
from application.posts.models import Post
from application.posts.forms import PostForm
from application.tags.models import Tag


@app.route("/topics", methods=["GET"])
@login_required
def topics_index():
    page = request.args.get("page", 1, type=int)
    topics = Topic.query.order_by(
        desc(Topic.date_created)).paginate(page, 5, False)

    next_url = None
    prev_url = None
    if topics.has_next:
        next_url = url_for('topics_index', page=topics.next_num)
    if topics.has_prev:
        prev_url = url_for('topics_index', page=topics.prev_num)

    most_liked_posts = Post.find_most_liked_posts_today(5)
    return render_template("topics/list.html", topics=topics.items, most_liked_posts=most_liked_posts, next_url=next_url, prev_url=prev_url)


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


@app.route("/topics/<topic_id>", methods=["DELETE"])
@login_required
def topics_delete(topic_id):
    topic = Topic.query.get(topic_id)

    if topic is None:
        return redirect(url_for("topics_index"))

    for post in topic.posts:
        db.session().delete(post)

    db.session().delete(topic)
    db.session().commit()

    resp = jsonify(success=True)
    return resp


@app.route("/topics/<topic_id>", methods=["PUT"])
@login_required
def topics_rename(topic_id):
    topic = Topic.query.get(topic_id)

    if topic is None:
        return redirect(url_for("topics_index"))

    json = request.get_json()
    topic.subject = json["Subject"]
    db.session().commit()

    resp = jsonify(success=True)
    return resp
