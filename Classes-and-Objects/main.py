class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def __str__(self):
        return self.name

    def change_name(self, name):

        if isinstance(name, str):
            self.name = name
            return 'Name changed successfully :)'
        return 'New name should be an instance of str.'

    def change_age(self, age):

        if isinstance(age, int):
            self.age = age
            return 'Age changed successfully :)'
        return 'New Age should be an Integer'

    def add_track(self, new_track):

        if isinstance(new_track, str):
            self.tracks.append(new_track)
            return 'New track added :)'
        return 'Opps! tracks are list of string'

    def get_score(self):
        return f'Your score is {round(self.score, 2)}'


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

Kuhmasii = Student(name='Kuhmasii', age=21, tracks=[
                   'Backend', 'Frontend', 'AI'], score=100.00)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

Kuhmasii.change_name('KUHMASII')
Kuhmasii.change_age(22)
Kuhmasii.add_track('Product Management')
Kuhmasii.get_score()
