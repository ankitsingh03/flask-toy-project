from flask import render_template, flash, redirect, url_for
from flaskproperty import app, db, bcrypt
from flaskproperty.forms import RegistrationForm, LoginForm
from flaskproperty.models import User

posts = [
    {
        'location': 'Delhi',
        'containt': 'delhi plot details'
    },
    {
        'location': 'mumbia',
        'containt': 'mumbai plot details'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    help to create new account for seller
    '''
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
    form = LoginForm()
    if form.validate_on_submit():
        # success is bootstrap class
        flash('you have been logedin', 'success')
        return redirect(url_for('home'))
    else:
        flash('please check once again', 'danger')
    return render_template('login.html', title='Login', form=form)
