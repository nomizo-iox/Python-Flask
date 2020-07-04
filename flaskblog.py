from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Samuel Ademola',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'April 20, 2019'
    },
     {
        'author': 'Jordan Dockery',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.htm', posts=posts)

@app.route('/about')
def about():
    return render_template('about.htm', title='About')


if __name__ == "__main__":
    app.run(debug=True)
