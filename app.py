from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html", citat="")

@app.route("/citat")
def citat():
    with open("citaty.txt", encoding="utf-8") as soubor:
        citaty = [line.strip() for line in soubor if line.strip()]
    
    index=random.randint(0, len(citaty) - 1)
    citat = citaty[index]

    return render_template("index.html", citat=citat)

if __name__ == "__main__":
    app.run(debug=True)