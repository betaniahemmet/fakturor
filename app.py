from flask import Flask, flash, request, render_template
from invoice_functions import create_invoices
from time import sleep

app = Flask(__name__)
app.secret_key = "askimsviken"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("2_fakturor") == "Skapa 2 fakturor":
            create_invoices(2)
            flash("Du har skapat 2 fakturor")
        if request.form.get("3_fakturor") == "Skapa 3 fakturor":
            create_invoices(3)
            flash("Du har skapat 3 fakturor")
    elif request.method == "GET":
        return render_template("index.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
