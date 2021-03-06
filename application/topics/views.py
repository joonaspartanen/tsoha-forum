from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from application.auth.services import UserService
from application.topics.models import Topic
from application.topics.forms import TopicForm, SearchForm
from application.posts.models import Post
from application.posts.forms import PostForm
from application.tags.models import Tag


@app.route("/topics", methods=["GET"])
@login_required
def topics_index():
    page = request.args.get("page", 1, type=int)
    topics = Topic.query.options(joinedload(Topic.posts), joinedload(Topic.tags), joinedload(
        Topic.author)).order_by(desc(Topic.date_created)).paginate(page, 5, False)

    next_url = None
    prev_url = None
    if topics.has_next:
        next_url = url_for("topics_index", page=topics.next_num)
    if topics.has_prev:
        prev_url = url_for("topics_index", page=topics.prev_num)

    most_liked_posts = Post.find_most_liked_posts_today()
    return render_template("topics/all_topics.html", topics=topics.items, most_liked_posts=most_liked_posts, next_url=next_url, prev_url=prev_url)


@app.route("/topics/<topic_id>", methods=["GET"])
@login_required
def view_topic(topic_id):
    topic = Topic.query.options(joinedload(Topic.posts), joinedload(
        Topic.tags), joinedload(Topic.author)).get(topic_id)

    if topic is None:
        return redirect(url_for("topics_index"))

    return render_template("topics/single.html", topic=topic, form=PostForm())


@app.route("/topics/new")
@login_required
def view_new_topic_form():
    tags = Tag.query.all()
    return render_template("topics/new.html", form=TopicForm(), tags=tags)


@app.route("/topics", methods=["POST"])
@login_required
def create_topic():
    form = TopicForm(request.form)

    form.tags.choices = [form.tags.data]

    if not form.validate():
        return render_template("topics/new.html", form=form)

    subject = form.subject.data
    body = form.body.data
    author_id = current_user.id

    initial_post = Post(body)
    initial_post.author_id = author_id
    topic = Topic(subject, author_id)
    topic.posts.append(initial_post)

    tag_names = form.tags.data[0].split(",")
    for tag_name in tag_names:
        tag = Tag.query.filter_by(name=tag_name).first()
        if not tag:
            tag = Tag(tag_name)
        topic.tags.append(tag)

    db.session().add(topic)
    db.session().commit()

    return redirect(url_for("topics_index"))


@app.route("/topics/<topic_id>", methods=["DELETE"])
@login_required
def delete_topic(topic_id):
    topic = Topic.query.get(topic_id)

    if UserService.user_not_admin_nor_editing_own_content(topic.author_id):
        return redirect(url_for("topics_index"))

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
def rename_topic(topic_id):
    topic = Topic.query.get(topic_id)

    if UserService.user_not_admin_nor_editing_own_content(topic.author_id):
        return redirect(url_for("topics_index"))

    if topic is None:
        return redirect(url_for("topics_index"))

    json = request.get_json()
    topic.subject = json["Subject"]
    db.session().commit()

    resp = jsonify(success=True)
    return resp


@app.route("/topics/search", methods=["GET"])
@login_required
def view_search_form():
    tags = Tag.query.all()
    return render_template("topics/search.html", form=SearchForm(), tags=tags)


@app.route("/topics/search", methods=["POST"])
@login_required
def search_topics():
    form = SearchForm(request.form)

    if not form.validate():
        return render_template("topics/search.html", form=form)

    search_results = Topic.search_topics(
        subject=form.subject.data, author=form.author.data)

    return render_template("topics/search_results.html", topics=search_results)
