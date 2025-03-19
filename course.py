class Course:
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description

    def display_courses(self):
        """Display course information"""
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Description: {self.description}")

    @staticmethod
    def add_new_course(course_id, course_name, description):
        """Add a new course"""
        return Course(course_id, course_name, description)

    def delete_course(self):
        """Delete course"""
        # Implementation will be added
        pass 