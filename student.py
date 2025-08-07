import firebase_admin
from firebase_admin import credentials, firestore


creden = credentials.Certificate("C:\\Users\\asp\\PycharmProjects\\PythonProject\\studb.json")
firebase_admin.initialize_app(creden)

db = firestore.client()

print("Connection with Firebase database...")

naam = input("Enter Your Name : ")
father_name = input("Enter Your Father Name : ")
phone_number = int(input("Enter Your Phone : "))
adress = input("Enter Your Address : ")
english_marks = int(input("Enter Your English Marks : "))
urdu_marks = int(input("Enter Your Urdu Marks : "))
maths_marks = int(input("Enter Your Math Marks : "))


total_marks = english_marks + urdu_marks + maths_marks
max_total = 300
percentage = round((total_marks / max_total) * 100, 2)

fetch_student = db.collection("Studentdata").document()
fetch_student.set({
    "Name": naam,
    "Fathername": father_name,
    "Phone": phone_number,
    "Address": adress,
    "English": english_marks,
    "Urdu": urdu_marks,
    "Math": maths_marks,
    "Total": total_marks,
    "Percentage": percentage
})

print("Student Data Add Successfully.")