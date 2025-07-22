student={
    "name":"Alice",
    "age":20,
    "course":"CSBS"
    }
print("name:",student["name"])
print("age:",student["age"])
print("course:",student["course"])
print("city:",student.get("city","not available"))
student["marks"]=85
student["city"]="chennai"
print("after adding city:",student)

student["marks"]=90
print("after updating marks:",student)
del student["age"]
print("after deleting age:",student)
print("keys:",student.keys())
print("values:",student.values())
print("items:",student.items())
print("name:",student["name"])
print("course:",student["course"])
print("marks:",student["marks"])
print("city:",student["city"])
