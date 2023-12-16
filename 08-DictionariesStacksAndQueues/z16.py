import json as j

with open('studenci.json', 'r') as s:
    data = j.load(s)

    limited_data = []

    for student in data:
        limited_info = {
            'name': f'{student["name"]} {student["surname"]}',
            'student_id': student['id']
        }
        limited_data.append(limited_info)

    with open('limited.json', 'w') as l:
        j.dump(limited_data, l, indent=4)
