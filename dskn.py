print('lesson4')


class Student:
    first_name: str
    second_name: str
    stat: str
    age: int

    def __init__(self, second_name: str, first_name: str, stat: str, age: int):
        self.first_name = first_name
        self.second_name = second_name
        self.stat = stat
        self.age = age

    def __str__(self):
        student_info = f'{self.second_name} {self.first_name}, возраст {self.age}, пол {self.stat}'
        return f'{student_info}\n'


class SchoolChild:
    first_name: str
    second_name: str
    activity: str

    def __init__(self, first_name: str, second_name: str):
        self.first_name = first_name
        self.second_name = second_name
        self.activity = 'studying'

    def __str__(self):
        person_info = f'{self.second_name} {self.first_name}, '
        return f'{person_info}основная деятельность: {self.activity}'


class Teacher:
    first_name: str
    second_name: str
    subject: str

    def __init__(self, first_name: str, second_name: str, subject: str):
        self.first_name = first_name
        self.second_name = second_name
        self.subject = subject

    def __str__(self):
        return f'{self.second_name} {self.first_name}, преподает: {self.subject}'


class HeadManager:
    first_name: str
    second_name: str
    stat: str
    age: int
    activity: str

    def __init__(self, first_name: str, second_name: str, stat: str, age: int):
        self.first_name = first_name
        self.second_name = second_name
        self.stat = stat
        self.age = age
        self.activity = 'management'

    def __str__(self):
        person_info = f'{self.second_name} {self.first_name}, возраст {self.age}, пол {self.stat}, '
        return f'{person_info}основная деятельность: {self.activity}'


ChernikovGerman = SchoolChild('Черников', 'Герман')
print(ChernikovGerman)

PetrovIvan = Teacher('Петров', 'Иван', 'Математика')
print(PetrovIvan)

IvanovSergey = HeadManager('Иванов', 'Сергей', 'male', 45)
print(IvanovSergey)

