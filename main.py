import pandas as pd
import functions as fn

data = pd.read_csv('students.csv')
# Calculate total marks
data['Total'] = data['Python'] + data['Java'] + data['C++']

# Class performance
def class_performance_summary():
    total_students = len(data)
    average_marks = data['Total'].mean()
    highest_marks = data['Total'].max()
    lowest_marks = data['Total'].min()
    passed = 0
    failed = 0
    for i in range(len(data)):
        result = fn.student_pass_fail(
            data.loc[i, 'Python'],
            data.loc[i, 'Java'],
            data.loc[i, 'C++']
        )
        if result == "PASS":
            passed += 1
        else:
            failed += 1

    subject_average = data[['Python', 'Java', 'C++']].mean()
    best_subject = subject_average.idxmax()

    print("===== CLASS PERFORMANCE SUMMARY =====")
    print("Total Students      :", total_students)
    print("Class Average Marks :", round(average_marks, 2))
    print("Highest Total Marks :", highest_marks)
    print("Lowest Total Marks  :", lowest_marks)
    print("Students Passed     :", passed)
    print("Students Failed     :", failed)
    print("Best Subject        :", best_subject)


# Highest marks in each subject
def subject_wise_max():
    print("\n===== SUBJECT-WISE MAXIMUM MARKS =====")

    for subject in ['Python', 'Java', 'C++']:
        index = data[subject].idxmax()
        name = data.loc[index, 'Name']
        marks = data.loc[index, subject]
        print(subject, ":", name, "-", marks)


# Average marks in each subject
def subject_wise_average():
    print("\n===== SUBJECT-WISE AVERAGE MARKS =====")

    for subject in ['Python', 'Java', 'C++']:
        average = data[subject].mean()
        print(subject, ":", round(average, 2))


# Lowest marks in each subject
def subject_wise_low():
    print("\n===== SUBJECT-WISE MINIMUM MARKS =====")

    for subject in ['Python', 'Java', 'C++']:
        index = data[subject].idxmin()
        name = data.loc[index, 'Name']
        marks = data.loc[index, subject]
        print(subject, ":", name, "-", marks)


# Top-performing students
def top_performer_students(column, number):
    top_students = data.nlargest(number, column)
    print(top_students)


# Attendance analysis
def attendance_analysis():
    average_attendance = data['Attendance'].mean()
    print("\nAverage Attendance:", round(average_attendance, 2))

    print("\nStudents Below 75% Attendance:")
    below_75 = data[data['Attendance'] < 75]
    print(below_75[['Roll_No', 'Name', 'Attendance']])

# Display student grades and results
def assign_student_results():
    grades = []
    results = []
    for i in range(len(data)):
        python = data.loc[i, 'Python']
        java = data.loc[i, 'Java']
        cpp = data.loc[i, 'C++']
        result = fn.student_pass_fail(python, java, cpp)
        if result == "FAIL":
            grade = "FAIL"
        else:
            grade = fn.student_grade(python, java, cpp)
        grades.append(grade)
        results.append(result)

    data['Grade'] = grades
    data['Pass_Fail'] = results

    print("\n===== STUDENT RESULTS =====")
    print(data[['Roll_No', 'Name', 'Total', 'Grade', 'Pass_Fail']])

class_performance_summary()

subject_wise_max()
subject_wise_average()
subject_wise_low()

print("\n===== TOP 3 PERFORMERS =====")
top_performer_students('Total', 3)

attendance_analysis()
assign_student_results()
