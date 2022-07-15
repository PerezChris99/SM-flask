from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    email = request.form.get("email")
    username = request.form.get("userame")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))