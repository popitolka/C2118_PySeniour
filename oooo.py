print('lesson3')


class StudySubject:
    name: str
    hours: int
    level: str

    def __init__(self, name: str, hours: int, level: str):
        self.name = name
        self.hours = hours
        self.level = level

    def __str__(self):
        return f'{self.name} {self.level}, количество часов {self.hours}'


class Audience:
    day: str
    time_day: int
    teacher: str

    def __init__(self, day: str, time_day: int, teacher: str):
        self.day = day
        self.time_day = time_day
        self.teacher = teacher

    def __str__(self):
        return f'День: {self.day}, время: {self.time_day} ч, преподаватель: {self.teacher}'


class Student:
    first_name: str
    second_name: str
    age: int
    is_offline: bool
    study_subject: StudySubject
    audience: Audience

    def __init__(self, second_name: str, first_name: str, age: int, study_subject: StudySubject, audience: Audience, is_offline=True):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.is_offline = is_offline
        self.study_subject = study_subject
        self.audience = audience

    def __str__(self):
        study_type = 'offline' if self.is_offline else 'online'
        student_info = f'{self.second_name} {self.first_name}, возраст {self.age}, тип обучения: {study_type}'
        return f'{student_info}\n{self.study_subject}\n{self.audience}'


C2118 = Audience('Saturday', 9, 'Polishko Konstantin')
py_senior = StudySubject('Python', 18, 'Senior')
ChernikovGerman = Student('Черников', "Герман", 15, py_senior, C2118)

print(ChernikovGerman)