class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def display_grade_report(self):
        """Display grade report"""
        print(f"Grade ID: {self.grade_id}")
        print(f"Grade: {self.grade}")
        print(f"Marks Range: {self.marks_range}")

    @staticmethod
    def add_grade(grade_id, grade, marks_range):
        """Add a new grade"""
        return Grades(grade_id, grade, marks_range)

    def delete_grade(self):
        """Delete grade"""
        # Implementation will be added
        pass

    def modify_grade(self, **kwargs):
        """Modify grade"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value) 