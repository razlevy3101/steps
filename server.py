#!flask/bin/python
import json
from flask import Flask, jsonify, request, make_response
from app import Creator, Post

app = Flask(__name__)


# @app.route("/post", methods=["POST"])
# def create_post():
#     """
#     *Creates a new post in the DB. Each post contains at least title, body and the user who created the post.
#     *To send a POST request through the shell, run the following:
#     curl -i -H "Content-Type: application/json" -X POST -d '{"title": "<>", "body": "<>", "creator": "<email>"}' http://localhost:5000/post
#     """
#     data = json.loads(request.data)
#     if not all([field in data for field in ["creator", "title", "body"]]):
#         return make_response(jsonify({"error": "You have to enter all fields: creator(as email), "
#                                                "title and body"}),
#                              400)
#
#     user = Creator.objects(email=data["creator"]).first()
#     try:
#         if not user:
#             user = Creator(email=data["creator"])
#             user.save()
#     except Exception:
#         return make_response(jsonify({"error":
#                                       "There was a problem creating a new Creator. Please try again later."}),
#                              500)
#
#     try:
#         post = Post(creator=user,
#                     title=data["title"],
#                     body=(data["body"]))
#         post.save()
#     except Exception:
#         return make_response(jsonify({"error":
#                                           "There was a problem creating a new Post. Please try again later."}),
#                              500)
#     user.update(posts_no=user.posts_no + 1)
#     return jsonify(post.to_json())


@app.route("/posts", methods=["GET"])
def get_posts():
    """

    """
    # TODO
    import ipdb;ipdb.set_trace()
    data = json.loads(request.data)

    posts = Post.objects.order_by("-")[:10]
    if not posts:
        return "There are currently no posts"
    res = [str(post) for post in posts]
    return f"Here are the last {7} posts:<br/>{'<br/>'.join(res)}"


# @app.route("/postsnumber", methods=["GET"])
# def sum_posts():
#     return f"There are {Post.objects.count()} Posts"
#
#
# @app.route("/topcreators", methods=["GET"])
# def get_top_10_creators():
#     """ Gets the top 10 of post creators """
#     top_creators = Creator.objects.order_by("-posts_no")[:10]
#     if not top_creators:
#         return "There are currently no creators"
#     res = [str(creator) for creator in top_creators]
#     return f"Top 10 creators are:<br/>{'<br/>'.join(res)}"


@app.route("/runtimestats", methods=["GET"])
def get_avg_runtime():
    res = f"""Average runtime for 'create_post' is: {4}<br/>Average runtime for 'get_posts' is: {6} """
    return res
