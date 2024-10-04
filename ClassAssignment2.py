sf=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
class Assignment2():
    def Subfields():
        print("Sub-fields in AI are:")
        for Subfield in sf:
            print(Subfield)
    def OddEven():
        Number=int(input("Enter The Number: "))
        if((Number%2)==1):
            print(Number," is Odd Number")
        else:
            print(Number," is Even Number")
    def Elegible():
        Gender=input("Enter Your Gender: ")
        Age=int(input("Enter Your Age: "))
        if(Gender=="Male" and Age>=21):
            print("ELEGIBLE")
        elif(Gender=="Female" and Age>=18):
                print("ELEGIBLE")
        else:
            print("NOT ELEGIBLE")
    def percentage():
        Subject1=int(input("Subject1= "))
        Subject2=int(input("Subject2= "))
        Subject3=int(input("Subject3= "))
        Subject4=int(input("Subject4= "))
        Subject5=int(input("Subject5= "))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=Total/5
        print("Total : ", Total)
        print("Percentange: ", Percentage)
    def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        Area=(Height*Breadth)/2
        print("Area Of Triangle: ",Area)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth1=int(input("Breadth1: "))
        Perimeter=Height1+Height2+Breadth1
        print("Perimeter of Triangle: ",Perimeter)