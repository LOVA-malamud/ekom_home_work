grades = [85, 90, 78, 92, 88]
backup_grades = grades.copy()  # shallow
grades.clear()
print('grades', grades)
print('backup grades', backup_grades)
backup_grades += [95, 100]
print('backup_grades ',backup_grades)
backup_grades.extend({95, 100})
print('backup_grades ',backup_grades)
