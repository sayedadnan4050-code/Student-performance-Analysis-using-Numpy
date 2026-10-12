# Student Grades Analysis using NumPy

## 📌 Project Overview

This project uses Python and NumPy to generate random student grades and calculate the maximum, minimum, and average marks for each student and subject.

## 🚀 Features

- Generate a 10 × 8 array of random grades between 80 and 99.
- Calculate maximum marks.
- Calculate minimum marks.
- Calculate average marks.
- Use NumPy functions for efficient calculations.

## 🛠️ Technologies Used

- Python
- NumPy

## 📥 Installation

Install NumPy using pip:

```bash
pip install numpy
```

## 💻 Code

```python
import numpy as np

# Generate a 10x8 array of random grades
grades = np.random.randint(80, 100, size=(10, 8))

print("Grades:\n", grades)

# Maximum marks
student_max = np.max(grades, axis=0)
subject_max = np.max(grades, axis=1)

print("student_max:", student_max)
print("subject_max:", subject_max)

# Minimum marks
student_min = np.min(grades, axis=0)
subject_min = np.min(grades, axis=1)

print("student_min:", student_min)
print("subject_min:", subject_min)

# Average marks
student_avg = np.mean(grades, axis=0)
subject_avg = np.mean(grades, axis=1)

print("student_avg:", student_avg)
print("subject_avg:", subject_avg)
```

## ▶️ How to Run

1. Install Python on your computer.
2. Install NumPy using `pip install numpy`.
3. Save the Python code in a file named `grades_analysis.py`.
4. Open your terminal in the project folder.
5. Run the program:

```bash
python grades_analysis.py
```

## 📊 Understanding the Output

The program generates 10 rows and 8 columns of random grades.

- **Grades:** Displays the generated marks.
- **Maximum marks:** Finds the maximum value in each column (`axis=0`) and each row (`axis=1`).
- **Minimum marks:** Finds the minimum value in each column and each row.
- **Average marks:** Calculates the mean of each column and each row.

### Understanding `axis`

| Axis | Meaning |
|---|---|
| `axis=0` | Performs calculations column-wise |
| `axis=1` | Performs calculations row-wise |

**Note:** In this code, `axis=0` calculates statistics for each column, while `axis=1` calculates statistics for each row. If rows represent students and columns represent subjects, the variable names `student_max` and `subject_max` should be swapped to match their actual meanings.

## 🎯 Learning Objectives

- Understand NumPy arrays.
- Practice random number generation.
- Learn array operations using `np.max()`, `np.min()`, and `np.mean()`.
- Understand the use of the `axis` parameter.

## 👨‍💻 Author

Created as a Python and NumPy practice project.
