midterms = [80, 91, 78]
finale = [98, 89, 53]
students = ['Dan', 'Ang', 'kate']

local_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finale)}

print(local_grades)