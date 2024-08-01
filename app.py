from flask import Flask,render_template

app = Flask(__name__)



@app.get("/")
@app.get("/home")
def home():
    return render_template("home/index.html","Home Page")





if __name__ == "__main__":
    app.run(debug=True)