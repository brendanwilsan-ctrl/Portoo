from flask import Blueprint, request, jsonify
from model import get_connection
project_bp = Blueprint("project", __name__)
@project_bp.route("/project", methods=["POST"])
def tambah_project():
    nama_project = request.form.get("nama_project")
    deskripsi = request.form.get("deskripsi")
    teknologi = request.form.get("teknologi")
    github = request.form.get("github")
    demo = request.form.get("demo")
    gambar = request.form.get("gambar")
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
    INSERT INTO project
    (nama_project, deskripsi, teknologi, github, demo, gambar)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql, (
        nama_project,
        deskripsi,
        teknologi,
        github,
        demo,
        gambar
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({
        "status": "success",
        "message": "Project berhasil ditambahkan"
    })
@project_bp.route("/project", methods=["GET"])
def get_project():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM project
        ORDER BY id DESC
    """)
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(projects)
@project_bp.route("/project/<int:id>", methods=["PUT"])
def update_project(id):

    nama_project = request.form.get("nama_project")
    deskripsi = request.form.get("deskripsi")
    teknologi = request.form.get("teknologi")
    github = request.form.get("github")
    demo = request.form.get("demo")
    gambar = request.form.get("gambar")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE project
        SET
            nama_project=%s,
            deskripsi=%s,
            teknologi=%s,
            github=%s,
            demo=%s,
            gambar=%s
        WHERE id=%s
    """,(
        nama_project,
        deskripsi,
        teknologi,
        github,
        demo,
        gambar,
        id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Project berhasil diupdate"
    })


@project_bp.route("/project/<int:id>", methods=["DELETE"])
def delete_project(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM project WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status":"success",
        "message":"Project berhasil dihapus"
    })

