
class Student:
    def __init__(self,name = 'nonana'):
        self.name = name

    def __int__(self):
        return f'hello, my neme is {self.name}'
    def __del__(self):
        print('Im granduater))')

stud= Student ('Andriy')
print(stud)



















#class Student:
#     amount_of_students = 0
#     def __init__(self,height=0, name='noname',mark=0):
#         self.height = height
#         self.name = name
#         self.mark = mark
#         print('ЗРІССТСССТТТ',self.name,':',self.height)
#         Student.amount_of_students += 1
#     def growUp(self):
#             self.height += 10000000000000000000000
#     def growmark(self):
#             self.mark += 1
#
#
#
# maxym = Student(height=10000000000000000000001000000000000000000000000000000001)
# maria = Student()
#
# print(Student.amount_of_students)
# print('мАКСА ЗРІСТ',maxym.height)
# print('мАРІЇ ЗРІСТ',maria.height)
#
# print(maxym.mark)
# maxym.growmark()
# print(maxym.mark)

