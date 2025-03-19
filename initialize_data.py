import csv
from student import Student
from course import Course
from professor import Professor
from grades import Grades
from login import LoginUser, CIPHER_SUITE

def initialize_sample_data():
    """Initialize sample data for the application"""
    # Create sample courses
    create_sample_courses()
    
    # Create sample professors
    create_sample_professors()
    
    # Create sample grades
    create_sample_grades()
    
    # Create sample users
    create_sample_users()
    
    # Create sample students
    create_sample_students()
    
    print("Sample data initialization complete.")

def create_sample_courses():
    """Create sample courses"""
    courses = [
        ["DATA200", "Data Science", "Introduction to Data Science with Python"],
        ["CS101", "Computer Science", "Introduction to Computer Science"],
        ["MATH101", "Mathematics", "Calculus and Linear Algebra"],
        ["ENG101", "English", "Composition and Rhetoric"],
        ["PHYS101", "Physics", "Classical Mechanics"]
    ]
    
    with open('courses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['course_id', 'course_name', 'description'])
        writer.writerows(courses)

def create_sample_professors():
    """Create sample professors"""
    professors = [
        ["micheal@mycsu.edu", "Michael John", "Senior Professor", "DATA200"],
        ["jane@mycsu.edu", "Jane Smith", "Associate Professor", "CS101"],
        ["robert@mycsu.edu", "Robert Johnson", "Assistant Professor", "MATH101"],
        ["emily@mycsu.edu", "Emily Davis", "Senior Professor", "ENG101"],
        ["david@mycsu.edu", "David Wilson", "Professor", "PHYS101"]
    ]
    
    with open('professors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['professor_id', 'name', 'rank', 'course_id'])
        writer.writerows(professors)

def create_sample_grades():
    """Create sample grades"""
    grades = [
        ["A", "A", "90-100"],
        ["B", "B", "80-89"],
        ["C", "C", "70-79"],
        ["D", "D", "60-69"],
        ["F", "F", "0-59"]
    ]
    
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['grade_id', 'grade', 'marks_range'])
        writer.writerows(grades)

def create_sample_users():
    """Create sample users"""
    def encrypt_password(password):
        return CIPHER_SUITE.encrypt(password.encode()).decode()
    
    users = [
        ["admin@mycsu.edu", encrypt_password("admin123"), "admin"],
        ["micheal@mycsu.edu", encrypt_password("professor123"), "professor"],
        ["jane@mycsu.edu", encrypt_password("professor123"), "professor"],
        ["student1@mycsu.edu", encrypt_password("student123"), "student"],
        ["student2@mycsu.edu", encrypt_password("student123"), "student"]
    ]
    
    with open('login.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'password', 'role'])
        writer.writerows(users)

def create_sample_students():
    """Create sample students"""
    students = [
        ["student1@mycsu.edu", "John", "Doe", "DATA200", "A", "95"],
        ["student2@mycsu.edu", "Jane", "Smith", "DATA200", "B", "85"],
        ["student3@mycsu.edu", "Michael", "Johnson", "CS101", "A", "92"],
        ["student4@mycsu.edu", "Emily", "Davis", "CS101", "C", "75"],
        ["student5@mycsu.edu", "David", "Wilson", "MATH101", "B", "88"],
        ["student6@mycsu.edu", "Sarah", "Brown", "MATH101", "A", "94"],
        ["student7@mycsu.edu", "Robert", "Martinez", "ENG101", "C", "78"],
        ["student8@mycsu.edu", "Jennifer", "Taylor", "ENG101", "B", "83"],
        ["student9@mycsu.edu", "William", "Anderson", "PHYS101", "A", "97"],
        ["student10@mycsu.edu", "Lisa", "Thomas", "PHYS101", "D", "65"]
    ]
    
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['email_address', 'first_name', 'last_name', 'course_id', 'grades', 'marks'])
        writer.writerows(students)

if __name__ == "__main__":
    initialize_sample_data()
    print("Login with admin@mycsu.edu / admin123 to access all features.") 