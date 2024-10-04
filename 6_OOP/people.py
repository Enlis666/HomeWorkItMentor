class PeopleList:
    def __init__(self):
        self.people = []


    def add_person(self, name):
        self.people.append(name)

    def __iter__(self):
        return iter(self.people)


people_list = PeopleList()
people_list.add_person("Алексей")
people_list.add_person("Мария")

for name in people_list:
    print(name)
