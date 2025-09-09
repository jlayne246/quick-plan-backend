from flask import Blueprint, request
from app.controllers.faculty_controller import get_faculties, get_faculty

faculty_bp = Blueprint("faculty", __name__)

@faculty_bp.route("/faculties")
def faculties():
    return get_faculties()

@faculty_bp.route("/faculties/<int:faculty_id>")
def faculty_by_id(faculty_id):
    return get_faculty(faculty_id=faculty_id)

