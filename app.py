from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2646f74c677249c898e8d52d28ee19f7'
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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
