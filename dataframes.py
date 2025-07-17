import pandas as pa
Rishta_Profile = {
    "Name" : ["Hamza","Abdul Rehman","Bilal","Moheeb","Sohaib"],
    "Gender" : ["M","M","M","M","M"],
    "Preferred_Caste" : ["Syed", "Bihari", "Rajput", "Mughal", "Pathan"],
    "Preferred_Area" : ["Lahore", "Karachi", "DHA", "Rawalpindi", "Multan"],
    "Profession" : ["Engineer", "Doctor", "Software Developer", "Teacher", "Businessman"],
    "No_Of_Sibling" : [3,5,8,4,2]
}

df_Rishta = pa.DataFrame(Rishta_Profile)
df_Rishta["Age"] = [21,32,28,26,35]
df_Rishta["Matital_Status"] = ["Single","Widow","Divoce","Single","Widow"]
df_Rishta["Nationality"] = ["Pakistani","Pakistani","Pakistani","Pakistani","Pakistani"]

print(df_Rishta[df_Rishta["Preferred_Caste"] == "Pathan"])
print(df_Rishta[df_Rishta["No_Of_Sibling"] > 2])
print(df_Rishta[df_Rishta["Preferred_Area"] == "DHA"])
print(df_Rishta[(df_Rishta["Preferred_Area"] == "Nazimabad") & (df_Rishta["Gender"] == "f")])

del df_Rishta["Profession"]

print(df_Rishta)
