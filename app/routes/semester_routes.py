from flask import Blueprint, request
from app.controllers.semester_controller import get_semester_courses

semester_bp = Blueprint("semester", __name__)

@semester_bp.route("/courses")
def semester_courses():
    semester_id = request.args.get("semester", type=int)
    return get_semester_courses(semester_id)

