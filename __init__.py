from flask import Flask

DEFAULT_START_POSTS = 0
DEFAULT_LIMIT_POSTS = 5

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'steps_task',
    'host': 'localhost',
    'port': 27017
}

app.start_index = DEFAULT_START_POSTS
app.limit_index = DEFAULT_LIMIT_POSTS
