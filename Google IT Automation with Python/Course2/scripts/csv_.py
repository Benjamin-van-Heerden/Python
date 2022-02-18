import csv
import os

f = open("csv_file.txt")
csv_f = csv.reader(f)

for row in csv_f:
    name, idt, first, last = row
    print(name, idt, first, last)

f.close()

hosts = [["work.local", "192.1.1"], ["local", "111.1.1"]]
with open("hosts.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(hosts)

keys = ["name", "id", "First name", "Last name"]
with open("csv_file.txt", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['name']}")
        with open("new_csv.csv", "a") as users:
            writer = csv.DictWriter(users, fieldnames=keys)
            if os.path.getsize("new_csv.csv") == 0:
                writer.writeheader()
            writer.writerow(row)


