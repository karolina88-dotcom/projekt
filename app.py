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

    if request.method == "POST":
        MOTIVACE ="motivace"
        HUMOR = "humor"
        FILOZOFIE = "filozofie"


        if tema==MOTIVACE:
            return render_template(
                citat="„Budoucnost patří těm, kdo věří svým krásným snům.“ Eleanor Roosevelt")
        elif tema==HUMOR:
            return render_template(
                citat="„Neberte život příliš vážně, stejně z něho nevyváznete živí.“ Elbert Hubbard")
        elif tema==FILOZOFIE:
            return render_template(
                citat="„Nemám slov, abych vyjádřil, co cítím při čtení knih. Trávím spoustu času čtením, protože to velmi miluji. Dokážu se v té knížce úplně ztratit a zapomenout, kde jsem. Filozofie je můj oblíbený předmět. To, co je skvělé na čtení, je, že na jednom řádku můžete narazit na něco, co jste se snažili vyjádřit celý život, nebo něco, na co jste se snažili přijít celý život.“ Michael Jackson")

        


    return render_template("index.html", citat=citat)

if __name__ == "__main__":
    app.run(debug=True)