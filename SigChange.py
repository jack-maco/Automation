import csv
import subprocess

filename = "PITDataContract.csv"
Asignature = open("HOSig_AllCorpEmployees.html", "r")
Csignature = open("HOSig_CareTeams.html", 'r')

fields = []
rows= []

with open(filename, 'r+') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

    print("Total:", csvreader.line_num - 1)
    Asign = Asignature.read()
    Csign = Csignature.read()
    r = open("current.txt", "r")

for x in rows:
    if (x[4] == "AllCorp"):
        Sign = Asign
    elif (x[4] == "Care"):
        Sign = Csign
    else:
        print("Data Error @", x[0])
        print(type(x[4]))
        break
    Sign = Sign.replace("{FullName}", x[0])
    Sign = Sign.replace("{Title}", x[1])
    if x[2]:
        Sign = Sign.replace("{Phone}", x[2])
    else:
        Sign = Sign.replace("<br><span style=\"white-space:pre-wrap\">{Phone}", "")
    Sign = Sign.replace("{Email@honorcare.com}", x[5])
    with open("current.txt", 'w') as current:
        print(Sign, file=current)
    subprocess.call(["gam", "user", x[3], "signature", "file", "current.txt"])
    current.close()