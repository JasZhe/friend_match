import csv
from person import Person

people = []

with open('Friend Match.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        row = row[1:]
        del row[-2:]
        if line_count > 0:
            people.append(Person(row))
        line_count += 1

for person in people:
    print(person.info[0] + ' matches:')
    person.find_matches(people)
    person.print_scores()
    print()
