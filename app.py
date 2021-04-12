from flask import Flask
from flask import render_template, redirect, url_for, flash,request
from forms import RegistrationForm, LoginForm
from models import db, User, Post
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from models import login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = '2646f74c677249c898e8d52d28ee19f7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

post = [
    {
        'author': 'kennedy wambua',
        'title': 'blog post 1',
        'content': 'first blog',
        'date_posted': 'March 21,2021'
    },
    {
        'author': 'kennedy ken',
        'title': 'blog post 2',
        'content': 'second blog',
        'date_posted': 'March 21,2021'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=post)


@app.route("/about")
def about():
    return render_template('about.html', title="about page")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account created succesfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


if __name__ == '__main__':
    app.run(debug=True)
