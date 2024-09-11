from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__, static_folder='../static', template_folder='../templates')

response = requests.get("https://api.npoint.io/932f8e756d0f4dfa0f18")
blog = response.json()

blog_post = []
for post in blog["blogs"]:
    post_obj = Post(post["title"], post["subtitle"], post["author"], post["content"])
    blog_post.append(post_obj)


@app.route("/")
def home():
    return render_template('index.html')
    # return send_from_directory(app.static_folder, 'index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/all-blogs")
def all_blogs():
    return render_template("blogs.html", all_blog=blog_post)

@app.route("/contact", methods=["POST"])
def receive_data():
    return "Form Successfully Submited!"


if __name__ == '__main__':
    app.run(debug=True)
 
