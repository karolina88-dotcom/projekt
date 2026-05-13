from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    with open("citaty.txt", encoding="utf-8") as soubor:
        citaty = [line.strip() for line in soubor if line.strip()]

    return render_template("index.html", citaty=citaty)

if __name__ == "__main__":
    app.run(debug=True)