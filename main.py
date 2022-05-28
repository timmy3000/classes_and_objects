class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name = "", age = 0, tracks = [""], score = 0.0):
        self.name = str(name)

        try:
            self.age = int(age)
        except Exception:
            return Exception

        self.tracks = list(tracks)

        try:
            self.score = float(score)
        except Exception:
            return Exception
    

    # getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_tracks(self):
        return self.tracks

    def get_score(self):
        return self.score


    # setters
    def change_name(self, name):
        self.name = str(name)

    def change_age(self, age):
        try:
            self.age = int(age)
        except Exception:
            return Exception

    def add_track(self, tracks):
        self.tracks = list(tracks)

    def change_score(self, score):
        try:
            self.score = float(score)
        except Exception:
            return Exception


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print("Score: " + str(Bob.get_score()))
