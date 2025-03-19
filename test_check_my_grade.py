import unittest
import os
import csv
import time
import random
from student import Student
from course import Course
from professor import Professor
from grades import Grades
from login import LoginUser
from data_manager import DataManager


class TestDataManager(unittest.TestCase):
    def setUp(self):
        # Set up test data files
        self.data_manager = DataManager()
        
        # Clear existing data
        self.data_manager.students = []
        self.data_manager.courses = []
        self.data_manager.professors = []
        self.data_manager.grades = []
        self.data_manager.users = []
        
        # Add test data
        self.setup_test_data()
        
    def tearDown(self):
        # Clean up test files
        if os.path.exists('students.csv'):
            os.remove('students.csv')
        if os.path.exists('courses.csv'):
            os.remove('courses.csv')
        if os.path.exists('professors.csv'):
            os.remove('professors.csv')
        if os.path.exists('grades.csv'):
            os.remove('grades.csv')
        if os.path.exists('login.csv'):
            os.remove('login.csv')
    
    def setup_test_data(self):
        # Add test courses
        course1 = Course("DATA200", "Data Science", "Introduction to Data Science with Python")
        course2 = Course("CS101", "Computer Science", "Introduction to Computer Science")
        self.data_manager.add_course(course1)
        self.data_manager.add_course(course2)
        
        # Add test professors
        prof1 = Professor("prof1@mycsu.edu", "John Smith", "Senior Professor", "DATA200")
        prof2 = Professor("prof2@mycsu.edu", "Jane Doe", "Associate Professor", "CS101")
        self.data_manager.add_professor(prof1)
        self.data_manager.add_professor(prof2)
        
        # Add test grades
        grade1 = Grades("A", "A", "90-100")
        grade2 = Grades("B", "B", "80-89")
        grade3 = Grades("C", "C", "70-79")
        self.data_manager.add_grade(grade1)
        self.data_manager.add_grade(grade2)
        self.data_manager.add_grade(grade3)
        
        # Add test users
        admin = LoginUser("admin@mycsu.edu", "admin123", "admin")
        admin.password = admin.encrypt_password("admin123")
        self.data_manager.add_user(admin)
        
        prof_user = LoginUser("prof1@mycsu.edu", "prof123", "professor")
        prof_user.password = prof_user.encrypt_password("prof123")
        self.data_manager.add_user(prof_user)
        
        # Add test students
        student1 = Student("student1@mycsu.edu", "Alice", "Johnson", "DATA200", "A", 95)
        student2 = Student("student2@mycsu.edu", "Bob", "Smith", "DATA200", "B", 85)
        student3 = Student("student3@mycsu.edu", "Charlie", "Brown", "CS101", "A", 92)
        self.data_manager.add_student(student1)
        self.data_manager.add_student(student2)
        self.data_manager.add_student(student3)
    
    def test_student_operations(self):
        """Test student add/delete/modify operations"""
        # Test adding a student
        new_student = Student("test@mycsu.edu", "Test", "User", "DATA200", "A", 90)
        self.assertTrue(self.data_manager.add_student(new_student))
        
        # Test adding a student with existing email
        duplicate_student = Student("test@mycsu.edu", "Duplicate", "User", "DATA200", "B", 80)
        self.assertFalse(self.data_manager.add_student(duplicate_student))
        
        # Test updating a student
        self.assertTrue(self.data_manager.update_student("test@mycsu.edu", first_name="Updated"))
        
        # Verify update worked
        for student in self.data_manager.students:
            if student.email_address == "test@mycsu.edu":
                self.assertEqual(student.first_name, "Updated")
        
        # Test deleting a student
        self.assertTrue(self.data_manager.delete_student("test@mycsu.edu"))
        
        # Verify deletion worked
        for student in self.data_manager.students:
            self.assertNotEqual(student.email_address, "test@mycsu.edu")
    
    def test_course_operations(self):
        """Test course add/delete operations"""
        # Test adding a course
        new_course = Course("TEST101", "Test Course", "Test Description")
        self.assertTrue(self.data_manager.add_course(new_course))
        
        # Test adding a course with existing ID
        duplicate_course = Course("TEST101", "Duplicate Course", "Duplicate Description")
        self.assertFalse(self.data_manager.add_course(duplicate_course))
        
        # Test deleting a course
        self.assertTrue(self.data_manager.delete_course("TEST101"))
        
        # Verify deletion worked
        for course in self.data_manager.courses:
            self.assertNotEqual(course.course_id, "TEST101")
    
    def test_professor_operations(self):
        """Test professor add/delete/modify operations"""
        # Test adding a professor
        new_prof = Professor("testprof@mycsu.edu", "Test Prof", "Assistant Professor", "DATA200")
        self.assertTrue(self.data_manager.add_professor(new_prof))
        
        # Test adding a professor with existing ID
        duplicate_prof = Professor("testprof@mycsu.edu", "Duplicate Prof", "Lecturer", "CS101")
        self.assertFalse(self.data_manager.add_professor(duplicate_prof))
        
        # Test updating a professor
        self.assertTrue(self.data_manager.update_professor("testprof@mycsu.edu", rank="Senior Lecturer"))
        
        # Verify update worked
        for prof in self.data_manager.professors:
            if prof.professor_id == "testprof@mycsu.edu":
                self.assertEqual(prof.rank, "Senior Lecturer")
        
        # Test deleting a professor
        self.assertTrue(self.data_manager.delete_professor("testprof@mycsu.edu"))
        
        # Verify deletion worked
        for prof in self.data_manager.professors:
            self.assertNotEqual(prof.professor_id, "testprof@mycsu.edu")
    
    def test_search_functionality(self):
        """Test search functionality"""
        # Search by first name
        results = self.data_manager.search_students("Alice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].email_address, "student1@mycsu.edu")
        
        # Search by last name
        results = self.data_manager.search_students("Smith")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].email_address, "student2@mycsu.edu")
        
        # Search by email
        results = self.data_manager.search_students("student3")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].email_address, "student3@mycsu.edu")
    
    def test_sort_functionality(self):
        """Test sort functionality"""
        # Sort by name (ascending)
        sorted_students = self.data_manager.sort_students(key='name', reverse=False)
        self.assertEqual(sorted_students[0].first_name, "Alice")
        self.assertEqual(sorted_students[1].first_name, "Bob")
        self.assertEqual(sorted_students[2].first_name, "Charlie")
        
        # Sort by marks (descending)
        sorted_students = self.data_manager.sort_students(key='marks', reverse=True)
        self.assertEqual(sorted_students[0].marks, 95)
        self.assertEqual(sorted_students[1].marks, 92)
        self.assertEqual(sorted_students[2].marks, 85)
    
    def test_statistics_functions(self):
        """Test statistics functions"""
        # Test average score
        avg = self.data_manager.get_average_score("DATA200")
        self.assertEqual(avg, (95 + 85) / 2)
        
        # Test median score
        median = self.data_manager.get_median_score("DATA200")
        self.assertEqual(median, (95 + 85) / 2)
        
        # Test min score
        min_score = self.data_manager.get_min_score("DATA200")
        self.assertEqual(min_score, 85)
        
        # Test max score
        max_score = self.data_manager.get_max_score("DATA200")
        self.assertEqual(max_score, 95)
    
    def test_report_generation(self):
        """Test report generation"""
        # Test course report
        report = self.data_manager.generate_course_report("DATA200")
        self.assertEqual(report['course'].course_id, "DATA200")
        self.assertEqual(len(report['students']), 2)
        self.assertEqual(report['statistics']['average'], (95 + 85) / 2)
        
        # Test professor report
        report = self.data_manager.generate_professor_report("prof1@mycsu.edu")
        self.assertEqual(report['professor'].professor_id, "prof1@mycsu.edu")
        self.assertEqual(report['course'].course_id, "DATA200")
        self.assertEqual(len(report['students']), 2)
        
        # Test student report
        report = self.data_manager.generate_student_report("student1@mycsu.edu")
        self.assertEqual(report['student'].email_address, "student1@mycsu.edu")
        self.assertEqual(report['course'].course_id, "DATA200")
        self.assertEqual(report['professor'].professor_id, "prof1@mycsu.edu")
        self.assertTrue(report['performance']['above_average'])


class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        
        # Clear existing data
        self.data_manager.students = []
        
        # Generate 1000 test student records
        self.generate_test_students(1000)
        
    def tearDown(self):
        if os.path.exists('students.csv'):
            os.remove('students.csv')
    
    def generate_test_students(self, count):
        """Generate a large number of test student records"""
        courses = ["DATA200", "CS101", "MATH101", "ENG101", "PHYS101"]
        grades = ["A", "B", "C", "D", "F"]
        
        for i in range(count):
            email = f"student{i}@mycsu.edu"
            first_name = f"FirstName{i}"
            last_name = f"LastName{i}"
            course_id = random.choice(courses)
            grade = random.choice(grades)
            marks = random.uniform(60, 100)
            
            student = Student(email, first_name, last_name, course_id, grade, marks)
            self.data_manager.students.append(student)
        
        self.data_manager.save_students()
    
    def test_search_performance(self):
        """Test search performance with large dataset"""
        start_time = time.time()
        
        # Perform multiple searches
        for i in range(10):
            query = f"FirstName{random.randint(0, 999)}"
            results = self.data_manager.search_students(query)
        
        end_time = time.time()
        search_time = end_time - start_time
        
        print(f"10 searches on 1000 records took {search_time:.4f} seconds")
        # Just a sanity check that our search isn't extremely slow
        self.assertLess(search_time, 1.0)
    
    def test_sort_performance(self):
        """Test sort performance with large dataset"""
        # Test name sorting
        start_time = time.time()
        sorted_students = self.data_manager.sort_students(key='name')
        name_sort_time = time.time() - start_time
        
        # Test marks sorting
        start_time = time.time()
        sorted_students = self.data_manager.sort_students(key='marks')
        marks_sort_time = time.time() - start_time
        
        print(f"Sorting 1000 records by name took {name_sort_time:.4f} seconds")
        print(f"Sorting 1000 records by marks took {marks_sort_time:.4f} seconds")
        
        # Just a sanity check that our sorting isn't extremely slow
        self.assertLess(name_sort_time, 1.0)
        self.assertLess(marks_sort_time, 1.0)


if __name__ == "__main__":
    unittest.main() 