
class Batch:

    # constructor
    def __init__(self):
        self.batch_name = ''
        self.students = []
        self.batch_timings = ''
        self.recording_url = ''

a = Batch()
a.batch_name = "Python fullstack batch 20"
a.students = ["Vivek", "Tejas"]
a.batch_timings = "Morning 7:00am"
a.recording_url = "https://www.googlemeet.com/example"


b = Batch()
b.batch_name = "Java fullstack batch 22"
b.students = ["Parikshit", "Suraj"]
b.batch_timings = "Morning 11:00am"
b.recording_url = "https://www.googlemeet.com/example"
print()