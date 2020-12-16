from flask import Flask
from flask_mongoengine import MongoEngine

DEFAULT_LAST_POSTS = 5

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class Creator(db.Document):
    email = db.StringField(required=True)
    posts_no = db.IntField(default=0)

    def to_json(self):
        return {"email": self.email, "posts_no": self.posts_no}

    def __str__(self):
        return f"Email: {self.email}, Number of Posts: {self.posts_no}"


class Post(db.Document):
    creator = db.ReferenceField(Creator, required=True)
    title = db.StringField(required=True)
    body = db.StringField(required=True)

    def to_json(self):
        return {"creator": self.creator.email, "title": self.title, "body": self.body}

    def to_html(self):
        return str(self).replace("\n", "<br/>")

    def __str__(self):
        return f"Title: {self.title}\nCreated by: {self.creator.email}\nBody:{self.body}"


class Runtime(db.Document):
    func_name = db.StringField(required=True)
    total_time = db.DecimalField(required=True)
