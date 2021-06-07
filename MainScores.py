from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("Scores.txt", "r") as f:
            content = f.read()
            return render_template("index.html", SCORE=content)
    except IOError:
        return render_template("error.html", ERROR='could not read file')

if __name__ == "__main__":
    app.run(debug=True)
