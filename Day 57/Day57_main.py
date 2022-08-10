from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/4af156202f984d3464c3"
blog_content = requests.get(blog_url).json()

app = Flask(__name__)


@app.route('/')
def get_blog():
    return render_template("index.html", posts=blog_content)


@app.route('/post/<int:post_ID>')
def show_post(post_ID):
    for post in blog_content:
        if post["id"] == post_ID:
            requested_post = Post(post['id'], post['title'], post['subtitle'], post['body'])
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run()
