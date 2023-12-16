student_data={
    "student_id": 123456,
    "first_name": "Emma",
    "last_name": "Johnson",
    "age": 19,
    "gender": "Female",
    "is_international": False,
    "grades": {
        "math": 90,
        "english": 85,
        "science": 92,
        "history": 88
    },
    "courses": ["Mathematics", "English Literature", "Physics", "History"],
    "contact_info": {
        "email": "emma.j@example.com",
        "phone": "+1 (555) 123-4567",
        "address": {
            "street": "123 Main Street",
            "city": "Anytown",
            "state": "CA",
            "zip_code": "12345"
        }
    },
    "is_active": True
}
import json as j
with open('students.json','w') as f:
    j.dump(student_data, f, indent=4)