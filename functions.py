import numpy as np 
def student_total_marks(subject_1,subject_2,subject_3):
    student_mark_list = [subject_1,subject_2,subject_3]
    total_marks = np.array(student_mark_list)
    return np.sum(total_marks)

def student_average_marks(subject_1,subject_2,subject_3):
    total_marks = student_total_marks(subject_1,subject_2,subject_3)
    return round(total_marks/3)

def student_grade(subject_1,subject_2,subject_3):
    total_marks = student_total_marks(subject_1,subject_2,subject_3)
    average_marks = student_average_marks(subject_1,subject_2,subject_3)
    if total_marks > 275 or average_marks > 90:
        return 'S'
    elif average_marks > 75:
        return 'A'
    elif average_marks > 50:
        return 'B'
    elif average_marks >= 35:
        return 'C'
    elif average_marks < 35 :
        return "FAIL"
    
def student_pass_fail(subject_1,subject_2,subject_3):
    if subject_1 < 35 or subject_2 < 35 or subject_3 < 35 :
        return "FAIL"
    return "PASS"


    