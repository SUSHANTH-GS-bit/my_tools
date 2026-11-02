import json
import os

# Sample student data
student = {
    "name": "Sushanth",
    "age": 20,
    "university": "Reva University",
    "course": "Artificial Intelligence and Data Science",
    "skills": ["Python", "C", "SQL", "Machine Learning"]
}

# 1. CREATE JSON FILE
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully!")

# 2. READ JSON FILE
with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent Details:")
print(json.dumps(data, indent=4))

# 3. UPDATE JSON DATA
data["age"] = 21
data["skills"].append("Data Science")

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nStudent details updated successfully!")

# 4. DELETE JSON FILE
# Uncomment the following lines to delete the file

# os.remove("student.json")
# print("JSON file deleted successfully!")
