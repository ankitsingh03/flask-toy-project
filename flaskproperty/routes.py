from flask import render_template, flash, redirect, url_for, request
from flaskproperty import app, db, bcrypt
from flaskproperty.forms import RegistrationForm, LoginForm, PostForm,\
    UpdateAccountForm
from flaskproperty.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
from PIL import Image
import os


@app.route('/')
@app.route('/home')
def home():
    # Fatching all the posts in post table
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    heading = 'Welcome! Choose Your Favourite Property.'
    return render_template('home.html', title='Home',
                           heading=heading, posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    help to create new account for seller
    '''
    # If logged user try to access login funtion. This will redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
                                .decode('utf-8')
        seller = User(username=form.username.data,
                      email=form.email.data,
                      password=hashed_password)

        db.session.add(seller)
        db.session.commit()

        flash(f"Account is created { form.username.data }", 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    seller can login and post the porperty detail
    '''
    # If logged user try to access login funtion. this will redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        # Fatching data in database according to email id
        seller = User.query.filter_by(email=form.email.data).first()
        # If seller and password present in DB return True
        if seller and bcrypt.check_password_hash(seller.password,
                                                 form.password.data):
            login_user(seller, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Error. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    # This funtion automatically logout the seller
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    '''
    This function save the image at definate path, \
    resize the image and encrypt the image file name and return.
    '''
    # generating random string
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/photos', picture_fn)
    # resizing the photo
    output_size = (350, 350)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    '''
    This function helps to create new post for seller.
    '''
    form = PostForm()
    if form.validate_on_submit():
        photo_file = form.photo.data
        if photo_file:
            # Take encrypt file name
            photo_file = save_picture(photo_file)
        post = Post(location=form.location.data,
                    detail=form.detail.data,
                    image=photo_file,
                    author=current_user)

        db.session.add(post)
        db.session.commit()

        flash('Your account has been updated!', 'success')
        return redirect(url_for('home'))

    return render_template('create_post.html', title='Create Post',
                           form=form, heading='Write New Post for Buyers')


@app.route("/post/<int:post_id>")
def post(post_id):
    '''
    This function shows the single post to seller for update and delete.
    '''
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.location, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()

    if form.validate_on_submit():
        post.location = form.location.data
        post.detail = form.detail.data
        if form.photo.data:
            post.image = save_picture(form.photo.data)
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.location.data = post.location
        form.detail.data = post.detail
    return render_template('create_post.html', title='Update Post',
                           form=form, heading='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    # I have to apply count queary
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc()).all()
    return render_template('user_posts.html',
                           title='My Post',
                           heading=username,
                           posts=posts,
                           user=user)


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', title='Page Not Found'), 404


@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', title='Not Found'), 403


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', title='Not Found'), 500
