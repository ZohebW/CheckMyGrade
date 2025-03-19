class Professor:
    def __init__(self, professor_id, name, rank, course_id):
        self.professor_id = professor_id
        self.name = name
        self.rank = rank
        self.course_id = course_id

    def professors_details(self):
        """Display professor details"""
        print(f"Professor ID: {self.professor_id}")
        print(f"Name: {self.name}")
        print(f"Rank: {self.rank}")
        print(f"Course ID: {self.course_id}")

    @staticmethod
    def add_new_professor(professor_id, name, rank, course_id):
        """Add a new professor"""
        return Professor(professor_id, name, rank, course_id)

    def delete_professor(self):
        """Delete professor"""
        # Implementation will be added
        pass

    def modify_professor_details(self, **kwargs):
        """Modify professor details"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_course_details_by_professor(self):
        """Show course details for professor"""
        return self.course_id 