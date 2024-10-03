from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.String(20), nullable=False)

# Create the database tables (uncomment the line below if you're running it for the first time)
# with app.app_context():
#     db.create_all()

# Sample blog posts (for testing)
posts = [
    {
        'title': 'Getting Started with Flask',
        'content': 'Flask is a lightweight WSGI web application framework in Python. It is designed with simplicity in mind and is great for beginners. In this post, we will explore how to set up a basic Flask application and its key components.',
        'author': 'Alex King',
        'date_posted': 'October 3, 2024',
        'comments': []
    },
    {
        'title': 'Understanding Flask Routing',
        'content': 'Routing is a key feature of Flask that allows you to define URL patterns for your application. In this post, we will discuss how to create routes, handle dynamic URLs, and return responses.',
        'author': 'Alex King',
        'date_posted': 'October 3, 2024',
        'comments': []
    },
    {
        'title': 'Working with Flask Templates',
        'content': 'Flask uses Jinja2 as its templating engine, which allows you to create dynamic HTML pages. In this post, we will learn how to use templates, pass data to them, and create reusable components.',
        'author': 'Alex King',
        'date_posted': 'October 3, 2024',
        'comments': []
    },
    {
        'title': 'Flask and Databases',
        'content': 'Flask can easily connect to databases using extensions like Flask-SQLAlchemy. In this post, we will explore how to set up a database, perform CRUD operations, and handle migrations.',
        'author': 'Alex King',
        'date_posted': 'October 3, 2024',
        'comments': []
    },
    {
        'title': 'Creating APIs with Flask',
        'content': 'Flask is not just for web applications; it is also excellent for building RESTful APIs. In this post, we will cover how to create API endpoints, handle JSON requests and responses, and use Flask-RESTful.',
        'author': 'Alex King',
        'date_posted': 'October 3, 2024',
        'comments': []
    },
    {
        'title': 'Deploying Your Flask App',
        'content': 'Once you have developed your Flask application, you might want to deploy it. In this post, we will discuss various deployment options, including Heroku and AWS, and the steps to get your app live.',
        'author': 'Alex King',
        'date_posted': 'October 3, 2024',
        'comments': []
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = posts[post_id]

    if request.method == 'POST':
        author = request.form['author']
        content = request.form['content']
        
        # Append the new comment to the post's comments list
        post['comments'].append({'author': author, 'content': content})
        
        return redirect(url_for('post', post_id=post_id))

    return render_template('post.html', post=post, post_id=post_id)

if __name__ == '__main__':
    app.run(debug=True)
