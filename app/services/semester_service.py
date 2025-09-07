from app.models.course import CourseOffering

from app.extensions import db

def fetch_semester_courses(semester_id):
    offerings = (
        db.session.query(CourseOffering)
        .filter(CourseOffering.semester_code == semester_id)
        .all()
    )
    
    return [offering.to_dict() for offering in offerings]