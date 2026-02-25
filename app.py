from flask import Flask, render_template, request, redirect, flash
import os
import hashlib
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


# Fake malware hash database (simulation)
MALWARE_HASHES = {
    "5d41402abc4b2a76b9719d911017c592",
}

SUSPICIOUS_KEYWORDS = ["virus", "trojan", "malware", "hack", "exploit"]


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def calculate_file_hash(file):
    file.seek(0)
    file_hash = hashlib.sha256(file.read()).hexdigest()
    file.seek(0)
    return file_hash


def simulate_virus_scan(file, filename):
    lower_name = filename.lower()
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in lower_name:
            return False, "⚠ Suspicious filename detected."

    file_hash = calculate_file_hash(file)

    if file_hash in MALWARE_HASHES:
        return False, "🛑 Malware signature detected."

    return True, "✅ File passed virus scan."


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":

        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)

        if file and allowed_file(file.filename):

            # Generate unique filename
            filename = str(uuid.uuid4()) + "_" + secure_filename(file.filename)

            is_safe, message = simulate_virus_scan(file, filename)

            if not is_safe:
                flash(message)
                return redirect(request.url)

            # Save the file to the server
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            flash("🚀 Upload Successful! File is clean and securely stored.")
            return redirect("/")

        else:
            flash("Invalid file type. Only PDF, JPG, PNG allowed.")
            return redirect(request.url)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)