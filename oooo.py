print('lesson3')



class StudySubject:
    name: str
    hours: int
    level: str

    def __init__(self, name:str, hours: int, level:str):
        self.name = name
        self.hours = hours
        self.level = level

    def __str__(self):
       return f'{self.name} {self.level}, количество часов{self.hours}'


class Student:
    first_name: str
    second_name: str
    age: int
    is_offline: bool
    study_subject: StudySubject

    def __init__(self, second_name: str, first_name: str, age: int, study_subject: StudySubject, is_offline = True):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.is_offline = is_offline
        self.study_subject


    def __str__(self):

        study_type: str
        if self.is_offline:
            study_type = 'offline'
        else:
             study_type = 'online'



        study_info f'{self.first_name}{self.first_name}, возраст {self.age}'

        return f'{student_info}\n{self.study_subject}'

py_senior = StudySubject('Python', 18, 'Senior')

ChernikovGerman = Student('Черников', "Макар", 15, py_senior)
print(ChernikovGerman)