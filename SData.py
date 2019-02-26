class School(object):
    def __init__(self):
        self.name = ""

class Teacher(object):
    def __init__(self):
        self.name = "teacher"
        self.ID = "0000"
        self.ctable = None
        self.jobs = []

class ClassRoom(object):
    def __init__(self):
        self.name = ""
        self.grade = 0
        self.number = 0
        self.ctable = None

class ClassTable(object):
    pass

class Lessons(object):
    pass
