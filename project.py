def Saadain():
  while True:
      print("Type  a  operation :\naddition,\nsubtraction,\ndivision,\nmultiplication")
      operation=input("enter the operation : ")
      a =float(input("enter first no :"))
      b =float(input("enter second no :"))
      if operation == "addition":
          print("RESULT =",a+b)
      elif operation == "subtraction":
          print("RESULT =",a-b)
      elif operation == "division":
          if b==0 :
            print("error,b can't be zero")
          else :
            print("RESULT =",a/b)
      elif operation == "multiplication" :
          print("RESULT =",a*b)
      else:
          print("invalid operation")
      again =input("Do you want another calculation: (yes/no)\n")
      if again != "yes":
        print("Good Bye !")
        break
      
Saadain()


