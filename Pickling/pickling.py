import pickle

#class --> 1.store student data,2.display student data

class Student:
    def __init__(self, sname, sroll_no, smarks, saddr):
        self.sname = sname
        self.sroll_no = sroll_no
        self.smarks = smarks
        self.saddr = saddr

    def display(self):
        print("========STUDENT DATA =========")
        print("Student Name:",self.sname)
        print("Student Roll No:",self.sroll_no)
        print("Student Marks:",self.smarks)
        print("Student Address:",self.saddr)

obj = Student('Joan',2,75,'Mumbai')


#pickling ---> dump
with open("student_data.dat","wb") as f:
    pickle.dump(obj,f)
    print("pickling is done!")

#unpickling -----> load
with open("student_data.dat","rb") as f:
    s = pickle.load(f)
    print("unpickling is done!")
    s.display()




    