from flask import Blueprint, request
from app.controllers.degree_controller import get_degrees, get_degree

degree_bp = Blueprint("degree", __name__)

@degree_bp.route("/degrees")
def degree_courses():
    return get_degrees()

@degree_bp.route("/degrees/<int:degree_id>")
def degree_courses_by_id(degree_id):
    return get_degree(degree_id=degree_id)

