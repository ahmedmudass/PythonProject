courses = ["Html","Css","Java","React","Python",".Net","Ms Office","Flutter","TypeScript","Nodejs"]
print(courses[6])
print(courses[-3])
print(courses[-1])
print(courses[2:6])
print(courses)

print(f"Size Of List : {len(courses)}")

courses.append("Python")
print(f"After Append {courses}")

courses.append("Hadoop")
print(f"After Append {courses}")

courses.insert(6 ,"PWD")
print(f"After Insert {courses}")

courses.insert(9 ,"Data Analytics")
print(f"After Insert {courses}")

print(f"Size Of List : {len(courses)}")

more_courses = ["MongoDb","Flutter","Nodejs","Vuejs"]
courses.extend(more_courses)
print(f"After Extend {courses}")

print(f"Size Of List : {len(courses)}")

courses.remove("Html")
print(f"After Removing Html : {courses}")

courses.pop()
print(f"After pop : {courses}")

print(f"Size Of List : {len(courses)}")

courses.sort()
print(f"Ascending order : {courses}")

courses.sort(reverse=True)
print(f"Disscending order : {courses}")

more_courses = ["Urdu","IOT","Networking"]
courses.extend(more_courses)
print(f"After Extend {courses}")

print(f"Size Of List : {len(courses)}")

courses.clear()
print(f"After Clearing List : {courses}")
print(f"Size Of List : {len(courses)}")

