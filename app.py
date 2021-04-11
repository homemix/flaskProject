from flask import Flask, render_template, url_for
from forms import RegistrationForm,LoginForm
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
def hello_world():
    return render_template('home.html', posts=post)


@app.route("/about")
def about():
    return render_template('about.html', title="about page")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form =form)

@app.route('/login')
def register():
    form = LoginForm()
    return render_template('login.html',title='Login',form =form)

if __name__ == '__main__':
    app.run()
