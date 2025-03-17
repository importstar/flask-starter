from flask import Blueprint, render_template, redirect, url_for, request
from ..forms.user_form import LoginForm
from ...services.user_service import UserService

module = Blueprint("users", __name__, url_prefix="/users")


@module.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if not form.validate_on_submit():
        if "password" in form.errors:
            if "Field must be at least 6 characters long." in form.errors["password"]:
                error_msg = "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"
            elif "This field is required." in form.errors["password"]:
                error_msg = "กรุณากรอกรหัสผ่าน"
            else:
                error_msg = "เกิดข้อผิดพลาดในการป้อนรหัสผ่าน"
        else:
            error_msg = "เกิดข้อผิดพลาด กรุณาลองใหม่"

        return render_template("/users/login.html", form=form, error_msg=error_msg)

    # Authenticate user
    login_result = UserService.login(form.username.data, form.password.data)
    if not login_result["success"]:
        return render_template(
            "/users/login.html", form=form, error_msg=login_result["error_msg"]
        )

    return redirect(request.args.get("next", url_for("index.index")))


@module.route("/register")
def register():
    return render_template("/users/register.html")
