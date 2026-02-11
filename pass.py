marks = [5, 88, 90, 27, 90]

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Total Students:", len(marks))
print("Number of Students Passed:", pass_count)
print("Number of Students Failed:", fail_count)
