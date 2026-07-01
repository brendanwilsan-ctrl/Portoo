from flask import Blueprint, request, jsonify
import cloudinary
import cloudinary.uploader
from config import Config

upload_bp = Blueprint("upload", __name__)

cloudinary.config(
    cloud_name=Config.CLOUD_NAME,
    api_key=Config.API_KEY,
    api_secret=Config.API_SECRET
)


@upload_bp.route("/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({
            "status": "error",
            "message": "File tidak ditemukan"
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "status": "error",
            "message": "Pilih file terlebih dahulu"
        }), 400

    try:

        result = cloudinary.uploader.upload(
            file,
            folder="portfolio"
        )

        return jsonify({
            "status": "success",
            "url": result["secure_url"]
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
