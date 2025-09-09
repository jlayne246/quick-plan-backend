from app.models.faculty import Faculty
from app.extensions import db

def get_all_faculties():
    faculties = db.session.query(Faculty).all()
    return [faculty.to_dict() for faculty in faculties]

def get_faculty(faculty_id):
    faculty = db.session.query(Faculty).filter(Faculty.faculty_id == faculty_id).first()
    return faculty.to_dict() if faculty else {"error": "Faculty not found"}