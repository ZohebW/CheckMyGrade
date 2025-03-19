class Student:
    def __init__(self, email_address, first_name, last_name, course_id, grades, marks):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grades = grades
        self.marks = marks

    def display_records(self):
        """Display student records"""
        print(f"Email: {self.email_address}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Course ID: {self.course_id}")
        print(f"Grade: {self.grades}")
        print(f"Marks: {self.marks}")

    @staticmethod
    def add_new_student(email_address, first_name, last_name, course_id, grades, marks):
        """Add a new student record"""
        return Student(email_address, first_name, last_name, course_id, grades, marks)

    def delete_student(self):
        """Delete student record"""
        # Implementation will be added
        pass

    def check_my_grades(self):
        """Check student grades"""
        return self.grades

    def update_student_record(self, **kwargs):
        """Update student record"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def check_my_marks(self):
        """Check student marks"""
        return self.marks 