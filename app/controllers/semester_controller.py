from flask import jsonify
import app.services.semester_service as semester_service

def get_semester_courses(semester_id):
    try:
        courses = semester_service.fetch_semester_courses(semester_id)
        return jsonify({"success": True, "data": courses}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500