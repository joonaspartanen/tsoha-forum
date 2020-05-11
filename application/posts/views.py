from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from application.posts.models import Post

@app.route("/posts", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())

@app.route("/posts/new")
def posts_form():
    return render_template("posts/new.html")

@app.route("/posts", methods=["POST"])
def posts_create():
    body = request.form.get("body")
    post = Post(body)

    db.session().add(post)
    db.session().commit()
    
    return redirect(url_for("posts_index"))

@app.route("/posts/<post_id>", methods=["POST"])
def posts_like(post_id):
    post = Post.query.get(post_id)
    post.likes += 1
    db.session().commit()

    resp = jsonify(success=True)
    return resp
