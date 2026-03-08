from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file_upload"]

        if file.filename == "":
            return render_template("index.html", pred="No file selected")

        file_path = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(file_path)

        return render_template("index.html", pred="File Uploaded Successfully")

    return render_template("index.html", pred="")

if __name__ == "__main__":
    app.run()
