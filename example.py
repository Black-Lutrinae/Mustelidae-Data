from db.interface import Interface

model = Interface('example')
model.connect()

persons = []

for i in range(10):
    person = {
        'name': str(i)*5,
        'age': i**2,
        'money': i ** 5
    }
    persons.append(person)

persons_ids = model.set(persons, multiple=True)

print(persons_ids)

model.disconnect()