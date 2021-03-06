from datetime import datetime
from flaskproperty import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    '''
    This function help user to stay login.
    '''
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    '''
    seller account and detail
    '''
    __tablename__ = 'seller'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    '''
    post table which will save all post uploaded by seller
    '''
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(30), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    detail = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False,
                      default='default.png')
    user_id = db.Column(db.Integer, db.ForeignKey('seller.id'), nullable=False)

    def __repr__(self):
        return f"Post({self.location},\
                      {self.date_posted},\
                      {self.user_id},\
                      {self.image})"
