from app.extensions import db
from app.models.degree import programme_degrees  

class Programme(db.Model):
    __tablename__ = "programmes"
    programme_code = db.Column(db.String(20), primary_key=True)
    programme_name = db.Column(db.String(100), nullable=False)
    department_code = db.Column(db.String(10), nullable=False)
    faculty_code = db.Column(db.String(10), db.ForeignKey("faculties.faculty_code"), nullable=False)
    
    degrees = db.relationship("Degree", secondary="programme_degrees", back_populates="programmes")

    faculty = db.relationship("Faculty", back_populates="programmes")

    def to_dict(self):
        return {
            "programme_code": self.programme_code,
            "programme_name": self.programme_name,
            "department_code": self.department_code,
            "faculty_code": self.faculty_code,
            "degrees": [degree.to_dict() for degree in self.degrees]
        }
        