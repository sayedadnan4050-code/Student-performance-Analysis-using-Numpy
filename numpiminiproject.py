import numpy as np 

#Genrate a 5x5 array of random grades between 80 and 99 
grades = np.random.randint(80, 100, size=(10, 8))

print("Grades:\n", grades)

#Maximum marks 
student_max = np.max(grades, axis=0)
subject_max = np.max(grades, axis=1)

print("student_max:", student_max)
print("subject_max:", subject_max)

#Minimum marks 
student_min = np.min(grades, axis=0)
subject_min = np.min(grades, axis=1)

print("student_min:", student_min)
print("subject_min:", subject_min)

#Average marks 
student_avg = np.mean(grades, axis=0)
subject_avg = np.mean(grades, axis=1)

print("student_avg:", student_avg)
print("subject_avg:", subject_avg)