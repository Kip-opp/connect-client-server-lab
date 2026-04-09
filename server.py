from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [{"id": 1, "title": "Sample Event 1"}, {"id": 2, "title": "Sample Event 2"}]


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Events Catalog API"})


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)


@app.route("/events", methods=["POST"])
def post_event():
    data = request.get_json()
    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400
    new_id = max(event["id"] for event in events) + 1 if events else 1
    new_event = {"id": new_id, "title": data["title"]}
    events.append(new_event)
    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)
