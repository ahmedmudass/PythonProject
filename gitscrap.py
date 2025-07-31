import os.path
import pandas
from pydriller import Repository

url = input("Please Enter Repository Link : ")
committername, committeremail, date, projectname, commitmsg = [],[],[],[],[]
print(f"Fetching {url}")

for a in Repository(url).traverse_commits():
    committername.append(a.author.name)
    committeremail.append(a.author.email)
    date.append(a.committer_date)
    projectname.append(a.project_name)
    commitmsg.append(a.msg)
print("Fetching Completed")

github_dict = {
    "Project Name" : projectname,
    "Name" : committername,
    "Email" : committeremail,
    "Message" : commitmsg,
    "Date" : date
}

github_df = pandas.DataFrame(github_dict)

filename = input("Enter Filename : ")
if os.path.exists(f"{filename}.csv"):
    print(f"{filename} Already Exist, Please Choose Different Name")
else:
    github_df.to_csv(f"{filename}.csv",index=False)
    print("File Created Successfully")
