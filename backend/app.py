from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
CORS(app)

# Serve the index.html
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# Serve any other static files (JS, CSS, images, etc.)
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# API endpoint for listings
@app.route("/api/listings", methods=["GET"])
def get_listings():
    with open("backend/listings.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
