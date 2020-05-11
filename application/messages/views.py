from application import app, db
from flask import jsonify, redirect, render_template, request, url_for
from application.messages.models import Message

@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", messages = Message.query.all())

@app.route("/messages/new")
def messages_form():
    return render_template("messages/new.html")

@app.route("/messages", methods=["POST"])
def messages_create():
    subject = request.form.get("subject")
    body = request.form.get("body")
    message = Message(subject, body)

    db.session().add(message)
    db.session().commit()
    
    return redirect(url_for("messages_index"))

@app.route("/messages/<message_id>", methods=["POST"])
def messages_like(message_id):
    message = Message.query.get(message_id)
    message.likes += 1
    db.session().commit()

    resp = jsonify(success=True)
    return resp
