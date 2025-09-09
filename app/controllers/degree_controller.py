from flask import jsonify
from app.services import semester_service
import app.services.degree_service as degree_service

def get_degrees():
    try:
        degrees = degree_service.get_degrees()
        return jsonify({"success": True, "data": degrees}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
def get_degree(degree_id):
    try:
        degree = degree_service.get_degree_by_id(degree_id)
        if degree:
            return jsonify({"success": True, "data": degree}), 200
        else:
            return jsonify({"success": False, "error": "Degree not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500