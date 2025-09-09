from app.extensions import db

class Course(db.Model):
    __tablename__ = "courses"

    course_code = db.Column(db.String(10), primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    programme_code = db.Column(db.String(10), nullable=False)
    
    # backref to CourseOffering will be established via relationship in CourseOffering model
    offerings = db.relationship("CourseOffering", back_populates="course")
    credits = db.relationship("CourseCredits", back_populates="course")
    mandatory_for_degrees = db.relationship("MandatoryCourses", back_populates="course")

    def to_dict(self):
        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "programme_code": self.programme_code,
            "credits": self.credits[0].credits if self.credits else None,
            "mandatory_for_degrees": [mc.degree_id for mc in self.mandatory_for_degrees]
        }

class CourseCredits(db.Model):
    __tablename__ = "credits"

    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(
        db.String(20), db.ForeignKey("courses.course_code"), nullable=False
    )
    credits = db.Column(db.Integer, nullable=False)

    course = db.relationship("Course", back_populates="credits")

    def to_dict(self):
        return {
            "id": self.id,
            "course_code": self.course_code,
            "credits": self.credits
        }

class CourseOffering(db.Model):
    __tablename__ = "offerings"

    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(
        db.String(20), db.ForeignKey("courses.course_code"), nullable=False
    )
    semester_code = db.Column(db.Integer, nullable=False)
    lecturer = db.Column(db.String(100), nullable=True)
    
    # Establish relationship back to Course
    course = db.relationship("Course", back_populates="offerings")

    def to_dict(self):
        return {
            "id": self.id,
            "course": self.course.to_dict() if self.course else None,
            "semester_code": self.semester_code,
            "lecturer": self.lecturer
        }

class MandatoryCourses(db.Model):
    __tablename__ = "mandatory_courses"

    id = db.Column(db.Integer, primary_key=True)
    degree_id = db.Column(
        db.Integer, db.ForeignKey("degrees.id"), nullable=False
    )
    course_code = db.Column(
        db.String(20), db.ForeignKey("courses.course_code"), nullable=False
    )
    
    course = db.relationship("Course", back_populates="mandatory_for_degrees")

    def to_dict(self):
        return {
            "id": self.id,
            "degree_id": self.degree_id,
            "course_code": self.course_code
        }