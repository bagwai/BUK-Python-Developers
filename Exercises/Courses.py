import random
#this program design to be assigning diffrent courses to diffrent lectures 
courses_set = ["PHY1234", "PHY1123", "PHY1122", "PHY1302", "PHY1239", "PHY1433", "PHY2234", "PHY2123", "PHY2122", "PHY2302", "PHY2239", "PHY2433", "PHY3234", "PHY3123", "PHY3122", "PHY3302", "PHY3239", "PHY3433","PHY4234", "PHY4123", "PHY4122", "PHY4302", "PHY4239", "PHY4433"] 
while(True):
 print(":::::::::::::::Welcome to Physics Department Course allocation system ::::::::::::::::::::")
 print("Press C to quit the program :") 
 lecture = str(input("Please Lecturer provide your name: ")) 
 if (lecture == "c" or lecture == "C"):
     exit()
 else: 
     #x = len(courses_set) #
     #print(x) 
    for i in courses_set: 
        random.shuffle(courses_set) 
        courses1 = courses_set[0] 
        courses2 = courses_set[1] 
        courses3 = courses_set[2] 
        courses4 = courses_set[3] 
        print("Lecture's Name is :" + lecture) 
        print("The lecturer's courses are: " , courses1 , " " , courses2 , " " , courses3 , " " , courses4)             
        lecture = str(input("Please provide your name: "))

