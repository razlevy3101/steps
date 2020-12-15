#!flask/bin/python
import json
from flask import Flask, jsonify, request
from app import Creator, Post

app = Flask(__name__)


@app.route("/post", methods=["POST"])
def create_post():
    """
    to send a POST request through the shell, run the following:
    curl -i -H "Content-Type: application/json" -X POST -d '{"title": "<>", "body": "<>", "creator": "<>"}' http://localhost:5000/post
    curl -i -H "Content-Type: application/json" -X POST -d '{"title": "BLA", "creator": "raz@gmail.com"}' http://localhost:5000/post
    """
    # TODO: handle errors
    data = json.loads(request.data)
    user = Creator.objects(email=data["creator"]).first()
    if not user:
        user = Creator(email=data["creator"])
        user.save()

    post = Post(creator=user,
                title=data["title"],
                body=(data["body"] if "body" in data else ""))
    post.save()
    user.update(posts_no=user.posts_no + 1)
    return jsonify(post.to_json())


@app.route("/posts", methods=["GET"])
def get_posts():
    # TODO
    import ipdb;ipdb.set_trace()
    return jsonify({"tasks": "d"})


@app.route("/postsnumber", methods=["GET"])
def sum_posts():
    return f"There are {Post.objects.count()} Posts"


@app.route("/topcreators", methods=["GET"])
def get_top_10_creators():
    """ Gets the top 10 of post creators """
    top_creators = Creator.objects.order_by("-posts_no")[:10]
    if not top_creators:
        return "There are currently no creators"
    res = [str(creator) for creator in top_creators]
    return f"Top 10 creators are:<br/>{'<br/>'.join(res)}"


@app.route("/runtimestats", methods=["GET"])
def get_avg_runtime():
    res = f"""Average runtime for 'create_post' is: {4}<br/>Average runtime for 'get_posts' is: {6} """
    return res
