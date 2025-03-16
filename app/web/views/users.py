from flask import Blueprint, render_template

module = Blueprint("users", __name__, url_prefix="/users")


@module.route("/login")
def login():
    return render_template("/users/login.html")
