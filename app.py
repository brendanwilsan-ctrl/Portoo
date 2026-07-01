from flask import Flask, send_from_directory
from config import Config
from flask_cors import CORS
from backend.admin.login import login_bp
from backend.admin.profiles import profile_bp
from backend.admin.skills import skill_bp
from backend.admin.experience import experience_bp
from backend.admin.projects import project_bp
from backend.admin.upload import upload_bp
from backend.admin.contact import contact_bp

app = Flask(
    __name__,
    template_folder="frontend",
    static_folder="frontend"
)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(login_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(skill_bp)
app.register_blueprint(experience_bp)
app.register_blueprint(project_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(contact_bp)
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")
if __name__ == "__main__":
    app.run(debug=True)
    print("APP BERJALAN")
from flask import send_from_directory

@app.route("/admin/dashboard")
def dashboard():
    return send_from_directory("frontend/admin", "dashboard.html")