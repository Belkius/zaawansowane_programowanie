class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_mark = sum(self.marks) / len(self.marks)
        return average_mark > 50


student1 = Student(name="Anna", marks=[60, 70, 80])
student2 = Student(name="Jan", marks=[30, 40, 45])

print(f"Czy {student1.name} zdał/a? {student1.is_passed()}")
print(f"Czy {student2.name} zdał/a? {student2.is_passed()}")

