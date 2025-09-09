from app.models.degree import Degree
from app.extensions import db  

def get_degrees():
    degrees = db.session.query(Degree).all()
    return [degree.to_dict() for degree in degrees]

def get_degree_by_id(degree_id):
    degree = db.session.query(Degree).filter(Degree.id == degree_id).first()
    return degree.to_dict() if degree else None