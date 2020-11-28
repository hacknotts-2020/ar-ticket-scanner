from flask import Blueprint
import pyqrcode

bp = Blueprint("create_qr", __name__)

@bp.route("/")
def create_qr():
    big_code = pyqrcode.create('0987654321')
    big_code.show()

    return {"qr": big_code.png_as_base64_str()}