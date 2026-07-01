from flask import Blueprint, request, jsonify
from model import get_connection
skill_bp = Blueprint("skill", __name__)
@skill_bp.route("/skill", methods=["POST"])
def tambah_skill():
    nama_skill = request.form.get("nama_skill")
    persentase = request.form.get("persentase")
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
    INSERT INTO skill
    (nama_skill, persentase)
    VALUES (%s,%s)
    """
    cursor.execute(sql, (
        nama_skill,
        persentase
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({
        "status": "success",
        "message": "Skill berhasil ditambahkan"
    })
@skill_bp.route("/skill", methods=["GET"])
def get_skill():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM skill
        ORDER BY id DESC
    """)
    skills = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(skills)    
@skill_bp.route("/skill/<int:id>", methods=["PUT"])
def update_skill(id):
    nama_skill = request.form.get("nama_skill")
    persentase = request.form.get("persentase")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE skill
        SET nama_skill=%s,
            persentase=%s
        WHERE id=%s
    """, (
        nama_skill,
        persentase,
        id
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Skill berhasil diupdate"
    })
@skill_bp.route("/skill/<int:id>", methods=["DELETE"])
def delete_skill(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM skill WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Skill berhasil dihapus"
    })
