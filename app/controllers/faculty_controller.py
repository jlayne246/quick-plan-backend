from app.services.faculty_service import get_all_faculties, get_faculty
from flask import jsonify

def get_faculties():
    try:
        faculties = get_all_faculties()
        return jsonify({"success": True, "data": faculties}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def get_faculty(faculty_id):
    try:
        faculty = get_faculty(faculty_id)
        return jsonify({"success": True, "data": faculty}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500