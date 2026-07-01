from flask import Blueprint, request, jsonify
from model import get_connection

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["POST"])
def tambah_profile():
    nama = request.form.get("nama")
    profesi = request.form.get("profesi")
    deskripsi = request.form.get("deskripsi")
    email = request.form.get("email")
    telepon = request.form.get("telepon")
    alamat = request.form.get("alamat")
    foto = request.form.get("foto")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO profile
        (nama, profesi, deskripsi, email, telepon, alamat, foto)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        nama,
        profesi,
        deskripsi,
        email,
        telepon,
        alamat,
        foto
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "status": "success",
        "message": "Profile berhasil ditambahkan"
    })


@profile_bp.route("/profile", methods=["GET"])
def get_profile():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM profile
        ORDER BY id DESC
        LIMIT 1
    """)

    profile = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify(profile)


@profile_bp.route("/profile/<int:id>", methods=["PUT"])
def update_profile(id):

    nama = request.form.get("nama")
    profesi = request.form.get("profesi")
    deskripsi = request.form.get("deskripsi")
    email = request.form.get("email")
    telepon = request.form.get("telepon")
    alamat = request.form.get("alamat")
    foto = request.form.get("foto")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE profile
        SET nama=%s,
            profesi=%s,
            deskripsi=%s,
            email=%s,
            telepon=%s,
            alamat=%s,
            foto=%s
        WHERE id=%s
    """, (
        nama,
        profesi,
        deskripsi,
        email,
        telepon,
        alamat,
        foto,
        id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Profile berhasil diupdate"
    })


@profile_bp.route("/profile/<int:id>", methods=["DELETE"])
def delete_profile(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM profile WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Profile berhasil dihapus"
    })
