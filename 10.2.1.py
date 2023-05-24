list_names = []
def get_student_names(student_names):
    for names in student_names.values():
        list_names.append(names)
    list_names.sort()
    return list_names


print(get_student_names({
    "Студент 1": "Артем",
    "Студент 2": "Иван",
    "Студент 3": "Роман"
}))
