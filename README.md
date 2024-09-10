# Blogging_ninja
Blogging Ninja is just a Blog website which can be used for multipurpose, to learn, create or copy template.

Blogging Ninja is an innovative blog website created by you, designed to be a versatile resource for learning, upgrading skills, or even serving as a template for others. The site leverages APIs to fetch blog content dynamically, ensuring that users always have access to the latest information. The backend is powered by a Flask server, which efficiently renders templates and manages the site’s functionality. For styling, you have utilized Bootstrap along with custom CSS to create a visually appealing and responsive design. JavaScript is employed to add interactivity, enhancing the user experience.

Home Page (index.html)
The home page serves as the main landing page, welcoming users and providing an overview of the latest blog posts.

HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blogging Ninja - Home</title>
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/custom.css">
</head>
<body>
    <header>
        <h1>Welcome to Blogging Ninja</h1>
    </header>
    <section id="latest-posts">
        <!-- Latest blog posts will be rendered here -->
    </section>
    <script src="static/js/main.js"></script>
</body>
</html>

About Section
The about section provides information about the purpose of the blog and its creator.

HTML

<section id="about">
    <h2>About Blogging Ninja</h2>
    <p>Blogging Ninja is a platform created to help you learn, upgrade your skills, or use as a template for your own projects.</p>
</section>

Contact Us
The contact section allows users to get in touch with the blog’s creator.

HTML

<section id="contact">
    <h2>Contact Us</h2>
    <form action="/contact" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <button type="submit">Send</button>
    </form>
</section>

All Posts
This section lists all the blog posts available on the site.

HTML

<section id="all-posts">
    <h2>All Posts</h2>
    <div id="posts-list">
        <!-- Blog posts will be rendered here -->
    </div>
</section>

Welcome Page
The welcome page greets new users and provides an introduction to the blog.

HTML

<section id="welcome">
    <h2>Welcome to Blogging Ninja</h2>
    <p>We're excited to have you here! Explore our latest posts and start your learning journey.</p>
</section>

Flask Code
Here’s a snippet of the code demonstrating how Flask is used in Blogging Ninja:

Python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts')
def posts():
    return render_template('all_posts.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)

This setup not only makes Blogging Ninja a robust platform but also a great example for others to learn from and build upon.
