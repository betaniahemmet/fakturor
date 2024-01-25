from flask import Blueprint, current_app, flash, render_template, url_for, redirect, request

from .file_functions import create_invoices, magnus_order

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    app = current_app  # Access the current Flask app instance

    if request.method == "POST":
        try:
            if request.form.get("1_faktura") == "Skapa 1 faktura":
                create_invoices(1)
                flash("Du har skapat en faktura")

            if request.form.get("2_fakturor") == "Skapa 2 fakturor":
                create_invoices(2)
                flash("Du har skapat 2 fakturor")

            if request.form.get("3_fakturor") == "Skapa 3 fakturor":
                create_invoices(3)
                flash("Du har skapat 3 fakturor")

            if request.form.get("magnus") == "Magnusson & Freij":
                magnus_order()
                flash("Du har skapat en beställning till M&F")

        except Exception as e:
            flash(str(e))

    elif request.method == "GET":
        return render_template("index.html")

    return redirect(
        url_for("main.index")
    )  # Instead of render_template, so that it won't send again if refreshed
