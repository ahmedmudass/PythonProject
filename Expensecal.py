name = input("Please Enter Your Name : ")
salary =  float(input("Enter Your Salary : "))

print("Expense Calculator")

groserybill = float(input("Enter Your Grosery Bill :"))
kebill = float(input("Enter Your KE Bill :"))
gasbill = float(input("Enter Your Gas Bill :"))
internet = float(input("Enter Your Internet Bill :"))
waterbill = float(input("Enter Your Water Bill :"))
jamedar = float(input("Enter Your Jamedar Bill :"))
supercard = float(input("Enter Your Super Card :"))
transport = float(input("Enter Your Transport Bill :"))
ownhouse = input("Do Your Live In Your Own House :")

if ownhouse.lower()=="no":
    rent = float(input("Enter Your House Rent :"))
else:
    rent = 0

married = input("Are You Married :")
if married.lower()=="yes":
    child = int(input("How Many Children Do You Have :"))
    if child > 0 :
        child_exp = float(input("Enter Your Child Expense :"))
    else:
        child_exp = 0
totalexpense = groserybill + kebill + gasbill + internet + waterbill + jamedar + supercard + transport + rent + child_exp
saving = salary - totalexpense
if salary > totalexpense :
    print(f"{name}.Your Saving Are {saving}.You Should Take Saving Plan Kindly Visit HBL.")
elif salary == totalexpense :
    print("Please You Should Take Major Steps To Increase Income.")
else:
    print("Please Decrease Your Expense.")
print(f"Salary : {salary}.Total Expense {totalexpense}")
print(f"Saving Is : {saving}")