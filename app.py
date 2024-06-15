from flask import Flask,render_template,request,url_for
from model import get_all_post

app = Flask(__name__)

@app.route("/",methods=["GET"])
@app.route("/home",methods=["GET"])
def home():
    return render_template("home/index.html")

@app.route('/all_posts')
def all_posts():
    posts = get_all_post()
    return render_template("posts/index.html",posts=posts)

if __name__ == "__main__":
    app.run(debug=True)