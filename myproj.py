#CST/16/COM/00543  Buhari Alhassan Ahmed Python programming
#This program will test if an individual is eligible for the Nigerian military recruitment.
#will test all these criterias from line 5 to line 12
Name=str (input("Your name:  "))    #Name and country should be treated as a noun,i.e first letter is capitalized
Nationality=str (input("Country:  "))
Age=int (input("Your age:  "))    #in numbers
Criminal_conviction=str(input("Convicted before?:  "))    #From line 7-10,if negative,the input should be just no
Medical_issues=str(input("Any medical issues?:  "))
Physical_disability=str(input("Any physical disability?:  "))
Psychological_issues=str(input("Any psychological issues?:  "))
Gender=str (input("Sex:  "))    #can be male or female
Height=float(input("Your Height(in meter):  "))    #must be a float,i.e with decimal eg-1.68

if Nationality=="Nigeria":
  print (Name.upper())    #prints out in uppercase
  if (Age >=18) and (Age<=22):    #ranges from 18-22
      print ("You are good")
      if Criminal_conviction=="no" and Medical_issues=="no" and Physical_disability=="no" and Psychological_issues=="no":
          print ("√")
          if Gender=="male" and Height >= 1.65:    #height test for male gender
              print ("you have 70% chance of being recruited")
              exit ()    #This function allows termination without proceeding to the next block
          if Gender=="female" and Height >=1.56:    #height test for female gender
              print ("you  have 70% chance of being recruited.")
              exit ()
          else:
              print ("but you did not fully meet up")
              exit ()
      else:
          print ("but you did not fully meet up" )
          exit ()
  else:
      print ("you are not within age range")
      exit ()
else:
  print("sorry, you are not a Nigerian ×")
  exit ()          
 

