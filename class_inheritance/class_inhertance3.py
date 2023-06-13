class Member:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Hi, my name is {self.name}'


class Student(Member):
    def __init__(self, name: str, reason: str):
        super().__init__(name)
        self.reason = reason


class Instructor(Member):
    def __init__(self, name: str, bio: str, skills: list = []):
        super().__init__(name)
        self.bio = bio
        self.skills = skills

    def add_skill(self, skill: str):
        self.skills.append(skill)


class Workshop:
    def __init__(self, date: str, subject: str, instructors: list = [],
                 students: list = []):
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students

    def add_participant(self, participant: Member):
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        else:
            self.students.append(participant)

    def __str__(self):
        text = f'Workshop - {self.date} - {self.subject} \n\n' \
               f'Students \n'
        students = ''
        for i, student in enumerate(self.students, 1):
            students += f'{i}. {student.name} - {student.reason} \n'
        text += f"{students} \n Instructors \n"
        instructors = ''
        for i, instructor in enumerate(self.instructors, 1):
            instructors += f'{i}. {instructor.name} - ' +\
                           ', '.join(instructor.skills) + '\n' +\
                            f'\t {instructor.bio} \n'
        text += instructors
        return text


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python"
                                       " and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
print(workshop)
