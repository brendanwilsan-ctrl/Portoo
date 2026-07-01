from flask import Blueprint, request, jsonify
from model import get_connection

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    if admin:
        return jsonify({
            "status": "success",
            "message": "Login berhasil"
        })

    return jsonify({
        "status": "failed",
        "message": "Username atau Password salah"
    })