people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
jobs = ['accountant','developer','designer','QA Tester']

print (list(zip(people,ages, jobs)))

for person, age, job in zip(people,ages, jobs):
    print(person)
    print(age)
    print(job)

for position in range(len(people)):
    person = people[position]
    age = ages[position]
    job = jobs[position]
    print(person, age, job)

