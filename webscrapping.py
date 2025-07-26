import pandas
import requests
from bs4 import BeautifulSoup

web_url = "https://hospitals.aku.edu/pakistan/patientservices/Pages/findadoctor.aspx"
response = requests.get(web_url)

data_lao = BeautifulSoup(response.text,"html.parser")
div_lao = data_lao.find_all("div",class_="g-mb-15")

p = data_lao.find_all("p")
DoctorName,Speciality = [],[]

for lala in div_lao:
    h4kolao = lala.find_all("h4")
    divspeciality = lala.find_all("div",class_="ProfileSpeciality")
    for h4 in h4kolao:
        print(h4.text)
        DoctorName.append(h4.text)
        for sp_div in divspeciality:
            em_lao = sp_div.find_all("em")
            for em in em_lao:
                print(em.text)
                Speciality.append(em.text)

Doctor_Data = {
    "DoctorName" : DoctorName,
    "Speciality" : Speciality
}

df = pandas.DataFrame(Doctor_Data)
print(df)
df.to_csv("Doctors_Data.csv",index=False)
