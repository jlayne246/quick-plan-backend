from flask import Blueprint, request
from app.controllers.semester_controller import get_semester_courses, get_semester_courses_by_degree

semester_bp = Blueprint("semester", __name__)

@semester_bp.route("/courses")
def semester_courses():
    semester_id = request.args.get("semester", type=int)
    return get_semester_courses(semester_id)

@semester_bp.route("/courses/int:<degree_id>")
def semester_courses_by_degree():
    semester_id = request.args.get("semester", type=int)
    degree_id = request.view_args.get("degree_id", type=int)
    return get_semester_courses_by_degree(semester_id, degree_id=degree_id)

