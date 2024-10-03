# Flask Tech Blog

A simple tech blog application built with Flask and SQLite. This blog allows users to view posts, read detailed articles, and add comments.

## Features

- **Home Page:** Displays a list of blog posts.
- **Post Details:** Each post can be viewed in detail, including the content, author, and date posted.
- **Comment Section:** Users can add comments to each post.

## Technologies Used

- Flask:** A lightweight WSGI web application framework for Python.
- SQLite:** A lightweight, disk-based database to store blog posts and comments.
- HTML/CSS:** For structuring and styling the web pages.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name

2. Install the required packages:
pip install Flask Flask-SQLAlchemy

3. Create the SQLite database (uncomment the db.create_all() line in app.py):
python
# with app.app_context():
#     db.create_all()


### Running the Application

Run the Flask application:
Open terminal, navigate to project directory and run: python app.py
Open your web browser and navigate to http://127.0.0.1:5000.

Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any enhancements.

License
This project is licensed under the MIT License. See the LICENSE file for details.
