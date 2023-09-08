from flask import Flask, flash, request, render_template, url_for, redirect
from file_functions import create_invoices
from waitress import serve
from config import secret

app = Flask(__name__)
app.secret_key = secret


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form.get("2_fakturor") == "Skapa 2 fakturor":
                create_invoices(2)
                flash("Du har skapat 2 fakturor")

            if request.form.get("3_fakturor") == "Skapa 3 fakturor":
                create_invoices(3)
                flash("Du har skapat 3 fakturor")

        except Exception as e:
            flash(str(e))

    elif request.method == "GET":
        return render_template("index.html")

    return redirect(
        url_for("index")
    )  # Instead of render_template, so that it won't send again if refreshed


if __name__ == "__main__":
    serve(app, port=5000, host='0.0.0.0')
