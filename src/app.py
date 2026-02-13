from flask import Flask, render_template, request
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from model.core_engine import recommend_schemes

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
            )

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    user = {
        "age": int(request.form["age"]),
        "income": int(request.form["income"]),
        "group": request.form["group"],
        "preferred_level": request.form["preferred_level"]
    }

    recommendations = recommend_schemes(user)

    return render_template("result.html", recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)
