import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mybd"
)

db_info = con.cursor()

print("------ User Input ------")

Name = input("Enter Your Name : ")
Guardian_Name = input("Enter Your Guardian_Name : ")
Father_Phone_Nmbr = input("Enter Your Father Phone Number : ")
Address = input("Enter Your Address : ")

query = "INSERT INTO `studend`(`Name`, `Guardian_Name`, `Father_Phone_Nmbr`, `Address`) VALUES (%s,%s,%s,%s)"
value = (Name,Guardian_Name,Father_Phone_Nmbr,Address )

run = db_info.execute(query,value)
con.commit()

print(f"{Name} Data Has Been Saved Successfully")

con.close()
