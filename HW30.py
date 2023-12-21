class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.last_name}, {self.first_name}, {self.age} years old, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record book: {self.record_book}'


class MaxCapacityError(Exception):
    pass


class Group:

    max_student = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_student:
            raise ValueError('Group capacity exceeded')
        self.group.add(student)

    def delete_student(self, last_name):
        remove_student = self.find_student(last_name)
        if remove_student:
            self.group.remove(remove_student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def full_group(self):
        return len(self.group) >= self.max_student

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

try:
    for i in range(11):
        gr.add_student(st1)
except MaxCapacityError as e:
    print(e)

print(gr)