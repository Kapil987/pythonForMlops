from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # localhost
def hello():
    return render_template("index.html")
app.run(debug=True)