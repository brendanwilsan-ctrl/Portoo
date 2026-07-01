import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

print("RESEND API =", resend.api_key) 
from flask import Blueprint, request, jsonify
from model import get_connection
contact_bp = Blueprint("contact", __name__)
@contact_bp.route("/contact", methods=["POST"])
def tambah_contact():
    nama = request.form.get("nama")
    email = request.form.get("email")
    subjek = request.form.get("subjek")
    pesan = request.form.get("pesan")
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
    INSERT INTO contact
    (nama, email, subjek, pesan)
    VALUES (%s,%s,%s,%s)
    """
    cursor.execute(sql, (
        nama,
        email,
        subjek,
        pesan
    ))
    conn.commit()
    resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": ["brendanwilsan@gmail.com"],
    "subject": f"Pesan Baru: {subjek}",
    "html": f"""
    Nama: {nama}
    Email: {email}
    Pesan: {pesan}
    """
})
    cursor.close()
    conn.close()
    return jsonify({
        "status": "success",
        "message": "Pesan berhasil dikirim"
    })

@contact_bp.route("/contact", methods=["GET"])
def get_contact():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM contact
        ORDER BY id DESC
    """)

    contacts = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(contacts)


@contact_bp.route("/contact/<int:id>", methods=["DELETE"])
def delete_contact(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM contact WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Pesan berhasil dihapus"
    })

