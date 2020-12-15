#!flask/bin/python
import json
from flask import Flask, jsonify, request
from app import Creator

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def create_post():
    """
    to send a POST request through the shell, run the following:
    curl -i -H "Content-Type: application/json" -X POST -d '{"email":"<>"}' http://localhost:5000/post
    """
    data = json.loads(request.data)
    user = Creator.objects(email=data['email']).first()
    import ipdb;ipdb.set_trace()
    if not user:
        user = Creator(email=data['email'])
        user.save()

    # TODO: create new post
    user.update(posts_no=user.posts_no + 1)
    return jsonify(user.to_json())


@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'tasks': "d"})


@app.route('/postsnumber', methods=['GET'])
def sum_posts():
    return "Total posts number is:"


@app.route('/topcreators', methods=['GET'])
def get_top_10_creators():
    return "Top 10 creators are:"


@app.route('/runtimestats', methods=['GET'])
def get_avg_runtime():
    # TODO: \n not working
    res = f"""Average runtime for 'create_post' is: {5} \nAverage runtime for 'get_posts' is: {6} """
    return res
