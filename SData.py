class School(object):
    def __init__(self,name="宇宙无敌最大的小学"):
        self.name = name
        self.terchers = None
        self.classrooms = None

    def __str__(self):
        return self.name

class Teacher(object):
    def __init__(self):
        self.name = "teacher"
        self.ID = "0000"
        self.ctable = None
        self.jobs = []

class ClassRoom(object):
    def __init__(self,grade=0,number=0):
        self.name = "{0}年级{1}班".format(grade,number)
        self.grade = 0
        self.number = 0
        self.ctable = None

    def __str__(self):
        return self.name

class ClassTable(object):
    def __init__(self):
        self.owner = None

class Lesson(object):
    def __init__(self,name=""):
        self.name = name
        self.teacher = None
        self.classroom = None

    def __str__(self):
        return self.name  
