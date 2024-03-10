#TO GET STUDENT DETAILS

class Student:
    def __init__(self):
        self.roll_no=input("Enter the roll number")
        self.name=input("Enter the name")
        self.phone_number=input("Enter the student phone number")
        self.address=input("Enter the student phone number")
        student_class=input("Enter the student class [ex:1,2,3,4,5,6,7,8,9,10]")
        
        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class=StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class]=new_class    
        self.student_class=StudentClass.classes[student_class]  
        print("\nStudnet added successfully")
        
    def getStudent(self):
        print("\n STUDENT DETAILS")
        print("\tRoll number:",self.roll_no)
        print("\t Name",self.name)
        print("\tPhoneNumber",self.phone_number)
        print("\t Address",self.address)
        print("\tClass",self.student_class.name)
        print("\t SchoolName:SREYAS")
              
                


class StudentClass:
    classes ={}
    def __init__(self,name):
        self.name=name
        StudentClass.classes[name]=self
        self.studentList=[]

def main():
    print("----welcome to sreyas school----")
    print("\t1)TO GET THE STUDENT DETAILS")
    print("\t2)TO ADD NEW STUDENT DETAILS")
    print("\t3)TO REMOVE STUDENT DETAILS")
    print("\t4)TO UPDATE STUDENT DETAILS")
    print("\t5)TO UPDATE STUDENT NAME")
    print("\t6)TO GET NUMBER OF STUDENT IN SCHOOL")
    print("\t7) TO GET ALL STUDENT DETAILS")
    print("\t8)TO GET ANY CLASS STUDENT DETAILS")
    
    option=input("ENTER ABOVE ANY OPTION:")
    print()
    
    if option=='1':
        roll_no=input("\tenter the roll number of a student")
        try:
            Student.student_dictionary[roll_no].getStudent()
        except:
            print("\t\tyou have entered the wrong roll number")    
        
    elif option=='2':
        new_student=Student()
        Student.student_dictionary[new_student.roll_no]=new_student
        
    elif option=='3':
        pass
    elif option=='4':
        pass
    elif option=='5':
        pass
    elif option=='6':
        pass
    elif option=='7':
        pass
    elif option=='8':
        pass
    
