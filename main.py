import pandas as pd 
import functions as fn
data = pd.read_csv('students.csv')
for i in range(0,20):
    sub1=data.loc[i,'Java']
    sub2=data.loc[i,'Python']
    sub3=data.loc[i,'C++']
    print(sub1,sub2,sub3)
    res=fn.student_total_marks(sub1,sub2,sub3)
    print(res)
    print(fn.student_average_marks(sub1,sub2,sub3))
    print(fn.student_grade(sub1,sub2,sub3))
    print()