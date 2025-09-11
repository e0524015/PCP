students = {
    "E0524015": "HEMA",
    "E0524023": "AADILA",
    "E0524017": "RAMYA",
    "E0524012": "LAKSHA"
}
print("Students in dictionary:")
for student_id, student_name in students.items():
    print(f"ID={student_id}, Name={student_name}")

search_id = "E0524012"
if search_id in students:
    print(f"Student found: ID={search_id}, Name={students[search_id]}")
else:
    print(f"Student with ID {search_id} not found.")