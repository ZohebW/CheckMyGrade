from data_manager import DataManager
from student import Student
from course import Course
from professor import Professor
from grades import Grades
from login import LoginUser

class CheckMyGrade:
    def __init__(self):
        self.data_manager = DataManager()
        self.current_user = None

    def login(self):
        """Handle user login"""
        email = input("Enter email: ")
        password = input("Enter password: ")
        
        for user in self.data_manager.users:
            if user.login(email, password):
                self.current_user = user
                print("Login successful!")
                return True
        print("Invalid credentials!")
        return False

    def show_menu(self):
        """Display main menu"""
        while True:
            print("\n=== CheckMyGrade Menu ===")
            print("1. Student Management")
            print("2. Course Management")
            print("3. Professor Management")
            print("4. Search Records")
            print("5. Sort Records")
            print("6. Display Reports")
            print("7. Statistics")
            print("8. User Management")
            print("9. Exit")
            
            choice = input("Enter your choice (1-9): ")
            
            if choice == '1':
                self.student_management_menu()
            elif choice == '2':
                self.course_management_menu()
            elif choice == '3':
                self.professor_management_menu()
            elif choice == '4':
                self.search_records()
            elif choice == '5':
                self.sort_records()
            elif choice == '6':
                self.display_reports()
            elif choice == '7':
                self.statistics_menu()
            elif choice == '8':
                self.user_management_menu()
            elif choice == '9':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

    def student_management_menu(self):
        """Student management menu"""
        while True:
            print("\n=== Student Management ===")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Update Student")
            print("4. Display All Students")
            print("5. Back to Main Menu")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.delete_student()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.display_all_students()
            elif choice == '5':
                break
            else:
                print("Invalid choice! Please try again.")

    def course_management_menu(self):
        """Course management menu"""
        while True:
            print("\n=== Course Management ===")
            print("1. Add Course")
            print("2. Delete Course")
            print("3. Display All Courses")
            print("4. Back to Main Menu")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                self.add_course()
            elif choice == '2':
                self.delete_course()
            elif choice == '3':
                self.display_all_courses()
            elif choice == '4':
                break
            else:
                print("Invalid choice! Please try again.")

    def professor_management_menu(self):
        """Professor management menu"""
        while True:
            print("\n=== Professor Management ===")
            print("1. Add Professor")
            print("2. Delete Professor")
            print("3. Update Professor")
            print("4. Display All Professors")
            print("5. Back to Main Menu")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                self.add_professor()
            elif choice == '2':
                self.delete_professor()
            elif choice == '3':
                self.update_professor()
            elif choice == '4':
                self.display_all_professors()
            elif choice == '5':
                break
            else:
                print("Invalid choice! Please try again.")

    def add_student(self):
        """Add a new student"""
        email = input("Enter student email: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        course_id = input("Enter course ID: ")
        grade = input("Enter grade: ")
        marks = float(input("Enter marks: "))
        
        student = Student.add_new_student(email, first_name, last_name, course_id, grade, marks)
        if self.data_manager.add_student(student):
            print("Student added successfully!")
        else:
            print("Student with this email already exists!")

    def delete_student(self):
        """Delete an existing student"""
        email = input("Enter student email to delete: ")
        if self.data_manager.delete_student(email):
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def update_student(self):
        """Update student information"""
        email = input("Enter student email to update: ")
        print("Leave blank if you don't want to update a field")
        
        first_name = input("Enter new first name: ")
        last_name = input("Enter new last name: ")
        course_id = input("Enter new course ID: ")
        grade = input("Enter new grade: ")
        marks_str = input("Enter new marks: ")
        
        kwargs = {}
        if first_name.strip():
            kwargs['first_name'] = first_name
        if last_name.strip():
            kwargs['last_name'] = last_name
        if course_id.strip():
            kwargs['course_id'] = course_id
        if grade.strip():
            kwargs['grades'] = grade
        if marks_str.strip():
            kwargs['marks'] = float(marks_str)
            
        if self.data_manager.update_student(email, **kwargs):
            print("Student updated successfully!")
        else:
            print("Student not found!")

    def display_all_students(self):
        """Display all students"""
        if not self.data_manager.students:
            print("No students found!")
            return
            
        print("\nAll Students:")
        for student in self.data_manager.students:
            student.display_records()
            print("-" * 30)

    def add_course(self):
        """Add a new course"""
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        description = input("Enter course description: ")
        
        course = Course.add_new_course(course_id, course_name, description)
        if self.data_manager.add_course(course):
            print("Course added successfully!")
        else:
            print("Course with this ID already exists!")

    def delete_course(self):
        """Delete an existing course"""
        course_id = input("Enter course ID to delete: ")
        if self.data_manager.delete_course(course_id):
            print("Course deleted successfully!")
        else:
            print("Course not found!")

    def display_all_courses(self):
        """Display all courses"""
        if not self.data_manager.courses:
            print("No courses found!")
            return
            
        print("\nAll Courses:")
        for course in self.data_manager.courses:
            course.display_courses()
            print("-" * 30)

    def add_professor(self):
        """Add a new professor"""
        professor_id = input("Enter professor email: ")
        name = input("Enter professor name: ")
        rank = input("Enter professor rank: ")
        course_id = input("Enter course ID: ")
        
        professor = Professor.add_new_professor(professor_id, name, rank, course_id)
        if self.data_manager.add_professor(professor):
            print("Professor added successfully!")
        else:
            print("Professor with this ID already exists!")

    def delete_professor(self):
        """Delete an existing professor"""
        professor_id = input("Enter professor ID to delete: ")
        if self.data_manager.delete_professor(professor_id):
            print("Professor deleted successfully!")
        else:
            print("Professor not found!")

    def update_professor(self):
        """Update professor information"""
        professor_id = input("Enter professor ID to update: ")
        print("Leave blank if you don't want to update a field")
        
        name = input("Enter new name: ")
        rank = input("Enter new rank: ")
        course_id = input("Enter new course ID: ")
        
        kwargs = {}
        if name.strip():
            kwargs['name'] = name
        if rank.strip():
            kwargs['rank'] = rank
        if course_id.strip():
            kwargs['course_id'] = course_id
            
        if self.data_manager.update_professor(professor_id, **kwargs):
            print("Professor updated successfully!")
        else:
            print("Professor not found!")

    def display_all_professors(self):
        """Display all professors"""
        if not self.data_manager.professors:
            print("No professors found!")
            return
            
        print("\nAll Professors:")
        for professor in self.data_manager.professors:
            professor.professors_details()
            print("-" * 30)

    def search_records(self):
        """Search records"""
        query = input("Enter search query: ")
        results = self.data_manager.search_students(query)
        
        if results:
            print("\nSearch Results:")
            for student in results:
                student.display_records()
                print("-" * 30)
        else:
            print("No results found!")

    def sort_records(self):
        """Sort records"""
        print("\nSort by:")
        print("1. Name (Ascending)")
        print("2. Name (Descending)")
        print("3. Marks (Ascending)")
        print("4. Marks (Descending)")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            sorted_students = self.data_manager.sort_students(key='name', reverse=False)
        elif choice == '2':
            sorted_students = self.data_manager.sort_students(key='name', reverse=True)
        elif choice == '3':
            sorted_students = self.data_manager.sort_students(key='marks', reverse=False)
        elif choice == '4':
            sorted_students = self.data_manager.sort_students(key='marks', reverse=True)
        else:
            print("Invalid choice!")
            return
        
        print("\nSorted Results:")
        for student in sorted_students:
            student.display_records()
            print("-" * 30)

    def statistics_menu(self):
        """Statistics menu"""
        while True:
            print("\n=== Statistics ===")
            print("1. Course Statistics")
            print("2. Back to Main Menu")
            
            choice = input("Enter your choice (1-2): ")
            
            if choice == '1':
                self.display_course_statistics()
            elif choice == '2':
                break
            else:
                print("Invalid choice! Please try again.")

    def display_course_statistics(self):
        """Display course statistics"""
        if not self.data_manager.courses:
            print("No courses found!")
            return
            
        print("\nAvailable Courses:")
        for i, course in enumerate(self.data_manager.courses, 1):
            print(f"{i}. {course.course_id}: {course.course_name}")
            
        try:
            index = int(input("Enter course number: ")) - 1
            course = self.data_manager.courses[index]
            
            avg_score = self.data_manager.get_average_score(course.course_id)
            median_score = self.data_manager.get_median_score(course.course_id)
            min_score = self.data_manager.get_min_score(course.course_id)
            max_score = self.data_manager.get_max_score(course.course_id)
            
            print(f"\nStatistics for {course.course_name}:")
            print(f"Average Score: {avg_score:.2f}")
            print(f"Median Score: {median_score:.2f}")
            print(f"Minimum Score: {min_score:.2f}")
            print(f"Maximum Score: {max_score:.2f}")
            
            students = [s for s in self.data_manager.students if s.course_id == course.course_id]
            print(f"Number of Students: {len(students)}")
            
        except (IndexError, ValueError):
            print("Invalid course selection!")

    def display_reports(self):
        """Display reports"""
        print("\nReport Types:")
        print("1. Course-wise Report")
        print("2. Professor-wise Report")
        print("3. Student-wise Report")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            self.display_course_report()
        elif choice == '2':
            self.display_professor_report()
        elif choice == '3':
            self.display_student_report()
        else:
            print("Invalid choice!")

    def display_course_report(self):
        """Display course report"""
        if not self.data_manager.courses:
            print("No courses found!")
            return
            
        print("\nAvailable Courses:")
        for i, course in enumerate(self.data_manager.courses, 1):
            print(f"{i}. {course.course_id}: {course.course_name}")
            
        try:
            index = int(input("Enter course number: ")) - 1
            course = self.data_manager.courses[index]
            
            report = self.data_manager.generate_course_report(course.course_id)
            if not report:
                print("Error generating report!")
                return
                
            print(f"\n=== Course Report: {course.course_name} ===")
            print(f"Course ID: {course.course_id}")
            print(f"Description: {course.description}")
            
            professor = report['professor']
            if professor:
                print(f"\nProfessor: {professor.name} ({professor.rank})")
                
            stats = report['statistics']
            print(f"\nClass Statistics:")
            print(f"Number of Students: {stats['count']}")
            print(f"Average Score: {stats['average']:.2f}")
            print(f"Median Score: {stats['median']:.2f}")
            print(f"Minimum Score: {stats['min']:.2f}")
            print(f"Maximum Score: {stats['max']:.2f}")
            
            print("\nStudent List:")
            for student in report['students']:
                print(f"{student.first_name} {student.last_name}: {student.grades} ({student.marks})")
                
        except (IndexError, ValueError):
            print("Invalid course selection!")

    def display_professor_report(self):
        """Display professor report"""
        if not self.data_manager.professors:
            print("No professors found!")
            return
            
        print("\nAvailable Professors:")
        for i, professor in enumerate(self.data_manager.professors, 1):
            print(f"{i}. {professor.name}")
            
        try:
            index = int(input("Enter professor number: ")) - 1
            professor = self.data_manager.professors[index]
            
            report = self.data_manager.generate_professor_report(professor.professor_id)
            if not report:
                print("Error generating report!")
                return
                
            print(f"\n=== Professor Report: {professor.name} ===")
            print(f"Professor ID: {professor.professor_id}")
            print(f"Rank: {professor.rank}")
            
            course = report['course']
            if course:
                print(f"\nCourse: {course.course_name} ({course.course_id})")
                print(f"Description: {course.description}")
                
            stats = report['statistics']
            print(f"\nClass Statistics:")
            print(f"Number of Students: {stats['count']}")
            print(f"Average Score: {stats['average']:.2f}")
            print(f"Median Score: {stats['median']:.2f}")
            print(f"Minimum Score: {stats['min']:.2f}")
            print(f"Maximum Score: {stats['max']:.2f}")
            
            print("\nStudent List:")
            for student in report['students']:
                print(f"{student.first_name} {student.last_name}: {student.grades} ({student.marks})")
                
        except (IndexError, ValueError):
            print("Invalid professor selection!")

    def display_student_report(self):
        """Display student report"""
        if not self.data_manager.students:
            print("No students found!")
            return
            
        print("\nAvailable Students:")
        for i, student in enumerate(self.data_manager.students, 1):
            print(f"{i}. {student.first_name} {student.last_name}")
            
        try:
            index = int(input("Enter student number: ")) - 1
            student = self.data_manager.students[index]
            
            report = self.data_manager.generate_student_report(student.email_address)
            if not report:
                print("Error generating report!")
                return
                
            print(f"\n=== Student Report: {student.first_name} {student.last_name} ===")
            print(f"Email: {student.email_address}")
            
            course = report['course']
            if course:
                print(f"\nCourse: {course.course_name} ({course.course_id})")
                
            professor = report['professor']
            if professor:
                print(f"Professor: {professor.name} ({professor.rank})")
                
            performance = report['performance']
            print(f"\nPerformance:")
            print(f"Marks: {performance['marks']}")
            print(f"Grade: {performance['grade']}")
            print(f"Course Average: {performance['course_average']:.2f}")
            print(f"Above Average: {'Yes' if performance['above_average'] else 'No'}")
                
        except (IndexError, ValueError):
            print("Invalid student selection!")

    def user_management_menu(self):
        """User management menu"""
        # Only allow admin users to access this menu
        if self.current_user.role != 'admin':
            print("Access denied! Admin privileges required.")
            return
            
        while True:
            print("\n=== User Management ===")
            print("1. Add User")
            print("2. Delete User")
            print("3. Display All Users")
            print("4. Back to Main Menu")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.delete_user()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice! Please try again.")

    def add_user(self):
        """Add a new user"""
        email_id = input("Enter user email: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/professor/student): ")
        
        user = LoginUser(email_id, password, role)
        user.password = user.encrypt_password(password)
        
        if self.data_manager.add_user(user):
            print("User added successfully!")
        else:
            print("User with this email already exists!")

    def delete_user(self):
        """Delete an existing user"""
        email_id = input("Enter user email to delete: ")
        if self.data_manager.delete_user(email_id):
            print("User deleted successfully!")
        else:
            print("User not found!")

    def display_all_users(self):
        """Display all users"""
        if not self.data_manager.users:
            print("No users found!")
            return
            
        print("\nAll Users:")
        for user in self.data_manager.users:
            print(f"Email: {user.email_id}")
            print(f"Role: {user.role}")
            print("-" * 30)

def main():
    app = CheckMyGrade()
    if app.login():
        app.show_menu()

if __name__ == "__main__":
    main() 