from ..models.user_model import User
from flask_login import login_user
import datetime


class UserService:
    @staticmethod
    def login(username: str, password: str):
        user = User.objects(username=username).first()
        error_msg = ""
        if not user or not user.check_password(password):
            error_msg = "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"

        if user and user.status == "disactive":
            error_msg = "บัญชีของท่านถูกลบออกจากระบบ"

        if error_msg:
            return {"error_msg": error_msg, "success": False}
        login_user(user)
        user.last_login_date = datetime.datetime.now()
        user.save()
        return {"error_msg": "", "success": True}

    @staticmethod
    def register(username: str, password: str):
        pass
