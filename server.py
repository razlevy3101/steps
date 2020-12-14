#!flask/bin/python
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/post', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


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
    res = f"""Average runtime for 'create_post' is: {4} \nAverage runtime for 'get_posts' is: {6} """
    return res


if __name__ == '__main__':
    app.run(debug=True)

