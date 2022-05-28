class Student:
    def __init__(self, name = "", age = 0, tracks = [""], score = 0.0):
        self.name = str(name)
        self.age = int(age)
        self.tracks = []

        if(isinstance(tracks, list)):
            self.tracks = self.tracks + tracks
        else:
            self.tracks.append(tracks)


        self.score = float(score)
    

    # getters
    def get_name(self):
        print("Name:", self.name)
        return self.name

    def get_age(self):
        print("Age:", self.age)
        return self.age

    def get_tracks(self):
        print("Tracks:", self.tracks)
        return self.tracks

    def get_score(self):
        print("Score:", self.score)
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
        self.tracks = []

        if(isinstance(tracks, list)):
            self.tracks = self.tracks + tracks
        else:
            self.tracks.append(tracks)


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
Bob.get_score()
