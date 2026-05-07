from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	citat = [ "„Neberte život příliš vážně, stejně z něho nevyváznete živí.“ Elbert Hubbard",
          "„Největší sláva není v tom, že nikdy neselžeme, ale v tom, že se vždy zvedneme.“ Konfucius",
          "„Největší dobrodružství, které můžete podniknout, je žít život svých snů.“ Oprah Winfrey",
          "„Největší překážkou k úspěchu je strach z neúspěchu.“ Sven Goran Eriksson",
          "„Největší bohatství je zdraví.“ Virgil",
          "„Bez hudby by byl život chybou.“ Friedrich Nietzsche",
          "„V životě nevěř tomu, kdo tě klame, ale nezklam toho, kdo ti věří.“ Neznámý autor",
          "„Zeptáš-li se, budeš 5 minut vypadat jako blbec. Nezeptáš-li se, budeš blbcem po celý život.“ Čínské přísloví",
          "„Zatímco ztrácíme svůj čas váháním a odkládáním, život utíká.“ Seneca",
          "„Pamatuj, že i ta nejtěžší hodina ve tvém životě, má jen 60 minut.“ Sofoklés"]


	return render_template("index.html", date=date, citat=citat)

if __name__=="__main__":
	app.run(debug=True)