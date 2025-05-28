import os
from flask import Flask, request, render_template, send_from_directory, jsonify, redirect, url_for, flash
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret"
app.FILES_DIR = os.environ.get("FILES_DIR", "data")
os.makedirs(app.FILES_DIR, exist_ok=True)

def get_files_info(search=None):
    files_info = []
    for filename in os.listdir(app.FILES_DIR):
        if search and search.lower() not in filename.lower():
            continue
        path = os.path.join(app.FILES_DIR, filename)
        if os.path.isfile(path):
            files_info.append({
                "name": filename,
                "size": os.path.getsize(path),
                "modif_date": datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M:%S"),
            })
    return files_info

@app.route("/", methods=["GET", "POST"])
def index():
    query = request.form.get("search") if request.method == "POST" else ""
    files = get_files_info(search=query)
    return render_template("index.html", files=files, search=query)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.FILES_DIR, filename, as_attachment=True)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.FILES_DIR, filename))
        flash("Fichier uploadé avec succès", "success")
    return redirect(url_for("index"))

@app.route("/api/files")
def api_files():
    return jsonify(get_files_info())

@app.route("/api/download/<filename>")
def api_download(filename):
    return send_from_directory(app.FILES_DIR, filename, as_attachment=True)

@app.route("/api/upload", methods=["POST"])
def api_upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.FILES_DIR, filename))
    return jsonify({"message": "File uploaded successfully"}), 201

