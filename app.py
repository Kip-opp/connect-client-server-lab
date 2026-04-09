from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import bp

app = Flask(__name__, static_folder="client")
CORS(app)

app.register_blueprint(bp)


@app.route("/client/<path:path>")
def serve_client(path):
    return send_from_directory("client", path)


if __name__ == "__main__":
    app.run(debug=True)
