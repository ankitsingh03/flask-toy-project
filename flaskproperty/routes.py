from flask import render_template, flash, redirect, url_for, request, abort
from flaskproperty import app, db, bcrypt
from flaskproperty.forms import RegistrationForm, LoginForm, PostForm
from flaskproperty.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    heading = 'welcome! choose your favourite Property.'
    return render_template('home.html', title='Home',
                           heading=heading, posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    help to create new account for seller
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
                         .decode('utf-8')
        seller = User(username=form.username.data, email=form.email.data,
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
    # it will check user is login or not
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        seller = User.query.filter_by(email=form.email.data).first()
        if seller and bcrypt.check_password_hash(seller.password,
                                                 form.password.data):
            # if user is matched return true
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


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(location=form.location.data, detail=form.detail.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, heading='Write new post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.location, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    # if post.author != current_user:
    #     abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.location = form.location.data
        post.detail = form.detail.data
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
    # if post.author != current_user:
    #     abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
