from app.extensions import db

class Faculty(db.Model):
    __tablename__ = "faculties"
    id = db.Column(db.Integer, primary_key=True)
    faculty_code = db.Column(db.String(10), unique=True, nullable=False)
    faculty_name = db.Column(db.String(100), nullable=False)
    
    programmes = db.relationship(
        "Programme",
        back_populates="faculty",
        primaryjoin="Faculty.faculty_code == Programme.faculty_code"  # ✅ explicit join
    )

    def to_dict(self):
        return {
            "faculty_code": self.faculty_code,
            "faculty_name": self.faculty_name,
            "programmes": [programme.programme_code for programme in self.programmes]
        }