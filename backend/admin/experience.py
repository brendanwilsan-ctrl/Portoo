from flask import Blueprint, request, jsonify
from model import get_connection

experience_bp = Blueprint("experience", __name__)


@experience_bp.route("/experience", methods=["POST"])
def tambah_experience():

    perusahaan = request.form.get("perusahaan")
    posisi = request.form.get("posisi")
    mulai = request.form.get("mulai")
    selesai = request.form.get("selesai")
    deskripsi = request.form.get("deskripsi")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO experience
        (perusahaan,posisi,mulai,selesai,deskripsi)
        VALUES (%s,%s,%s,%s,%s)
    """,(
        perusahaan,
        posisi,
        mulai,
        selesai,
        deskripsi
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Experience berhasil ditambahkan"
    })


@experience_bp.route("/experience", methods=["GET"])
def get_experience():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
        SELECT *
        FROM experience
        ORDER BY mulai DESC
    """)

    data=cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


@experience_bp.route("/experience/<int:id>", methods=["PUT"])
def update_experience(id):

    perusahaan=request.form.get("perusahaan")
    posisi=request.form.get("posisi")
    mulai=request.form.get("mulai")
    selesai=request.form.get("selesai")
    deskripsi=request.form.get("deskripsi")

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
        UPDATE experience
        SET perusahaan=%s,
            posisi=%s,
            mulai=%s,
            selesai=%s,
            deskripsi=%s
        WHERE id=%s
    """,(
        perusahaan,
        posisi,
        mulai,
        selesai,
        deskripsi,
        id
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Experience berhasil diupdate"
    })


@experience_bp.route("/experience/<int:id>", methods=["DELETE"])
def delete_experience(id):

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        "DELETE FROM experience WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Experience berhasil dihapus"
    })