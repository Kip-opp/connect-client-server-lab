from flask import Blueprint, request, jsonify
from data import events

bp = Blueprint("events_bp", __name__)


@bp.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200


@bp.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


@bp.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()
    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400
    new_id = max((e["id"] for e in events), default=0) + 1
    new_event = {"id": new_id, "title": data["title"]}
    events.append(new_event)
    return jsonify(new_event), 201
