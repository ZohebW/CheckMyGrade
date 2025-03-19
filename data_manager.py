import csv
import time
import statistics
from typing import List, Dict, Any
from student import Student
from course import Course
from professor import Professor
from grades import Grades
from login import LoginUser, CIPHER_SUITE

class DataManager:
    def __init__(self):
        self.students: List[Student] = []
        self.courses: List[Course] = []
        self.professors: List[Professor] = []
        self.grades: List[Grades] = []
        self.users: List[LoginUser] = []
        self.load_data()

    def load_data(self):
        """Load data from CSV files"""
        self.load_students()
        self.load_courses()
        self.load_professors()
        self.load_grades()
        self.load_users()

    def save_data(self):
        """Save data to CSV files"""
        self.save_students()
        self.save_courses()
        self.save_professors()
        self.save_grades()
        self.save_users()

    def load_students(self):
        """Load students from CSV"""
        try:
            with open('students.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row['email_address'],
                        row['first_name'],
                        row['last_name'],
                        row['course_id'],
                        row['grades'],
                        float(row['marks'])
                    )
                    self.students.append(student)
        except FileNotFoundError:
            print("Students file not found, creating new file.")
            self.save_students()

    def save_students(self):
        """Save students to CSV"""
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['email_address', 'first_name', 'last_name', 'course_id', 'grades', 'marks'])
            for student in self.students:
                writer.writerow([
                    student.email_address,
                    student.first_name,
                    student.last_name,
                    student.course_id,
                    student.grades,
                    student.marks
                ])

    def add_student(self, student: Student):
        """Add a student to the collection"""
        # Check if student with same email already exists
        for existing_student in self.students:
            if existing_student.email_address == student.email_address:
                return False
        self.students.append(student)
        self.save_students()
        return True

    def delete_student(self, email_address: str):
        """Delete a student by email"""
        for i, student in enumerate(self.students):
            if student.email_address == email_address:
                del self.students[i]
                self.save_students()
                return True
        return False

    def update_student(self, email_address: str, **kwargs):
        """Update a student's information"""
        for student in self.students:
            if student.email_address == email_address:
                student.update_student_record(**kwargs)
                self.save_students()
                return True
        return False

    def search_students(self, query: str) -> List[Student]:
        """Search students by name or email"""
        start_time = time.time()
        results = []
        for student in self.students:
            if (query.lower() in student.first_name.lower() or
                query.lower() in student.last_name.lower() or
                query.lower() in student.email_address.lower()):
                results.append(student)
        end_time = time.time()
        print(f"Search took {end_time - start_time:.4f} seconds")
        return results

    def sort_students(self, key: str = 'name', reverse: bool = False) -> List[Student]:
        """Sort students by name or marks"""
        start_time = time.time()
        if key == 'name':
            sorted_students = sorted(
                self.students,
                key=lambda x: f"{x.first_name} {x.last_name}",
                reverse=reverse
            )
        else:  # sort by marks
            sorted_students = sorted(
                self.students,
                key=lambda x: x.marks,
                reverse=reverse
            )
        end_time = time.time()
        print(f"Sorting took {end_time - start_time:.4f} seconds")
        return sorted_students

    def load_courses(self):
        """Load courses from CSV"""
        try:
            with open('courses.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    course = Course(
                        row['course_id'],
                        row['course_name'],
                        row['description']
                    )
                    self.courses.append(course)
        except FileNotFoundError:
            print("Courses file not found, creating new file.")
            self.save_courses()

    def save_courses(self):
        """Save courses to CSV"""
        with open('courses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['course_id', 'course_name', 'description'])
            for course in self.courses:
                writer.writerow([
                    course.course_id,
                    course.course_name,
                    course.description
                ])

    def add_course(self, course: Course):
        """Add a course to the collection"""
        # Check if course with same ID already exists
        for existing_course in self.courses:
            if existing_course.course_id == course.course_id:
                return False
        self.courses.append(course)
        self.save_courses()
        return True

    def delete_course(self, course_id: str):
        """Delete a course by ID"""
        for i, course in enumerate(self.courses):
            if course.course_id == course_id:
                del self.courses[i]
                self.save_courses()
                return True
        return False

    def get_course(self, course_id: str) -> Course:
        """Get a course by ID"""
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def load_professors(self):
        """Load professors from CSV"""
        try:
            with open('professors.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    professor = Professor(
                        row['professor_id'],
                        row['name'],
                        row['rank'],
                        row['course_id']
                    )
                    self.professors.append(professor)
        except FileNotFoundError:
            print("Professors file not found, creating new file.")
            self.save_professors()

    def save_professors(self):
        """Save professors to CSV"""
        with open('professors.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['professor_id', 'name', 'rank', 'course_id'])
            for professor in self.professors:
                writer.writerow([
                    professor.professor_id,
                    professor.name,
                    professor.rank,
                    professor.course_id
                ])

    def add_professor(self, professor: Professor):
        """Add a professor to the collection"""
        # Check if professor with same ID already exists
        for existing_professor in self.professors:
            if existing_professor.professor_id == professor.professor_id:
                return False
        self.professors.append(professor)
        self.save_professors()
        return True

    def delete_professor(self, professor_id: str):
        """Delete a professor by ID"""
        for i, professor in enumerate(self.professors):
            if professor.professor_id == professor_id:
                del self.professors[i]
                self.save_professors()
                return True
        return False

    def update_professor(self, professor_id: str, **kwargs):
        """Update a professor's information"""
        for professor in self.professors:
            if professor.professor_id == professor_id:
                professor.modify_professor_details(**kwargs)
                self.save_professors()
                return True
        return False

    def get_professor_by_course(self, course_id: str) -> Professor:
        """Get professor by course ID"""
        for professor in self.professors:
            if professor.course_id == course_id:
                return professor
        return None

    def load_grades(self):
        """Load grades from CSV"""
        try:
            with open('grades.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    grade = Grades(
                        row['grade_id'],
                        row['grade'],
                        row['marks_range']
                    )
                    self.grades.append(grade)
        except FileNotFoundError:
            print("Grades file not found, creating new file.")
            self.save_grades()

    def save_grades(self):
        """Save grades to CSV"""
        with open('grades.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['grade_id', 'grade', 'marks_range'])
            for grade in self.grades:
                writer.writerow([
                    grade.grade_id,
                    grade.grade,
                    grade.marks_range
                ])

    def add_grade(self, grade: Grades):
        """Add a grade to the collection"""
        # Check if grade with same ID already exists
        for existing_grade in self.grades:
            if existing_grade.grade_id == grade.grade_id:
                return False
        self.grades.append(grade)
        self.save_grades()
        return True

    def delete_grade(self, grade_id: str):
        """Delete a grade by ID"""
        for i, grade in enumerate(self.grades):
            if grade.grade_id == grade_id:
                del self.grades[i]
                self.save_grades()
                return True
        return False

    def update_grade(self, grade_id: str, **kwargs):
        """Update a grade's information"""
        for grade in self.grades:
            if grade.grade_id == grade_id:
                grade.modify_grade(**kwargs)
                self.save_grades()
                return True
        return False

    def load_users(self):
        """Load users from CSV"""
        try:
            with open('login.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = LoginUser(
                        row['user_id'],
                        row['password'],  # Password is already encrypted
                        row['role']
                    )
                    self.users.append(user)
        except FileNotFoundError:
            print("Users file not found, creating new file with default admin user.")
            # Create a default admin user
            admin = LoginUser("admin@mycsu.edu", "admin123", "admin")
            admin.password = CIPHER_SUITE.encrypt("admin123".encode()).decode()
            self.users.append(admin)
            self.save_users()

    def save_users(self):
        """Save users to CSV"""
        with open('login.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['user_id', 'password', 'role'])
            for user in self.users:
                writer.writerow([
                    user.email_id,
                    user.password,
                    user.role
                ])

    def add_user(self, user: LoginUser):
        """Add a user to the collection"""
        # Check if user with same ID already exists
        for existing_user in self.users:
            if existing_user.email_id == user.email_id:
                return False
        self.users.append(user)
        self.save_users()
        return True

    def delete_user(self, email_id: str):
        """Delete a user by ID"""
        for i, user in enumerate(self.users):
            if user.email_id == email_id:
                del self.users[i]
                self.save_users()
                return True
        return False

    def get_average_score(self, course_id: str) -> float:
        """Get the average score for a course"""
        scores = [student.marks for student in self.students if student.course_id == course_id]
        if not scores:
            return 0
        return sum(scores) / len(scores)

    def get_median_score(self, course_id: str) -> float:
        """Get the median score for a course"""
        scores = [student.marks for student in self.students if student.course_id == course_id]
        if not scores:
            return 0
        return statistics.median(scores)

    def get_min_score(self, course_id: str) -> float:
        """Get the minimum score for a course"""
        scores = [student.marks for student in self.students if student.course_id == course_id]
        if not scores:
            return 0
        return min(scores)

    def get_max_score(self, course_id: str) -> float:
        """Get the maximum score for a course"""
        scores = [student.marks for student in self.students if student.course_id == course_id]
        if not scores:
            return 0
        return max(scores)

    def generate_course_report(self, course_id: str) -> Dict[str, Any]:
        """Generate a report for a specific course"""
        course = self.get_course(course_id)
        if not course:
            return None
            
        students_in_course = [s for s in self.students if s.course_id == course_id]
        professor = self.get_professor_by_course(course_id)
        
        report = {
            'course': course,
            'professor': professor,
            'students': students_in_course,
            'statistics': {
                'average': self.get_average_score(course_id),
                'median': self.get_median_score(course_id),
                'min': self.get_min_score(course_id),
                'max': self.get_max_score(course_id),
                'count': len(students_in_course)
            }
        }
        return report

    def generate_professor_report(self, professor_id: str) -> Dict[str, Any]:
        """Generate a report for a specific professor"""
        professor = None
        for p in self.professors:
            if p.professor_id == professor_id:
                professor = p
                break
        
        if not professor:
            return None
            
        course = self.get_course(professor.course_id)
        students = [s for s in self.students if s.course_id == professor.course_id]
        
        report = {
            'professor': professor,
            'course': course,
            'students': students,
            'statistics': {
                'average': self.get_average_score(professor.course_id),
                'median': self.get_median_score(professor.course_id),
                'min': self.get_min_score(professor.course_id),
                'max': self.get_max_score(professor.course_id),
                'count': len(students)
            }
        }
        return report

    def generate_student_report(self, email_address: str) -> Dict[str, Any]:
        """Generate a report for a specific student"""
        student = None
        for s in self.students:
            if s.email_address == email_address:
                student = s
                break
                
        if not student:
            return None
            
        course = self.get_course(student.course_id)
        professor = self.get_professor_by_course(student.course_id)
        
        course_avg = self.get_average_score(student.course_id)
        above_average = student.marks > course_avg
        
        report = {
            'student': student,
            'course': course,
            'professor': professor,
            'performance': {
                'marks': student.marks,
                'grade': student.grades,
                'course_average': course_avg,
                'above_average': above_average
            }
        }
        return report 