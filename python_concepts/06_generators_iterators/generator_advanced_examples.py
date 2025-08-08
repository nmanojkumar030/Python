from random import choice

names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
majors = ["Math", "Engineering", "Comp. Science", "Arts", "Business"]


def people_list(numbers):
    result = []
    for n in range(numbers):
        person = {"id": n, "name": choice(names), "major": choice(majors)}
        result.append(person)
    return result


output = people_list(1000000)
print(output)


def people_list_generator(numbers):
    for n in range(numbers):
        person = {"id": n, "name": choice(names), "major": choice(majors)}
        yield person


output = people_list_generator(1000000)
print(output)
