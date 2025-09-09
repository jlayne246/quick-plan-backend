from app.models.course import CourseOffering

from app.extensions import db

def fetch_semester_courses(semester_id):
    offerings = (
        db.session.query(CourseOffering)
        .filter(CourseOffering.semester_code == semester_id)
        .all()
    )
    
    return [offering.to_dict() for offering in offerings]

def fetch_semester_courses_by_degree(semester_id, degree_id):
    offerings = (
        db.session.query(CourseOffering)
        .filter(CourseOffering.semester_code == semester_id)
        .filter(CourseOffering.course.mandatory_for_degrees.contains(degree_id))
        .all()
    )
    
    return [offering.to_dict() for offering in offerings]