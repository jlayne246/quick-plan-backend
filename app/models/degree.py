from app.extensions import db
from sqlalchemy.dialects.postgresql import ARRAY

programme_degrees = db.Table(
    "programme_degrees",
    db.Column("programme_code", db.String(20), db.ForeignKey("programmes.programme_code"), primary_key=True),
    db.Column("degree_id", db.Integer, db.ForeignKey("degrees.id"), primary_key=True)
)

class Degree(db.Model):
    __tablename__ = "degrees"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=True)
    minor = db.Column(ARRAY(db.String), nullable=True)
    
    programmes = db.relationship("Programme", secondary=programme_degrees, back_populates="degrees")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "major": self.major,
            "minor": self.minor
        }
