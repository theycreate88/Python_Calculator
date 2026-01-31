

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def product(a,b):
    return a*b

def divide(a,b):
    return a/b

def modulus(a,b):
    return a%b
    
    

while(True):
    while True:
            try:
                num1=float(input("Enter First Number: "))
                num2=float(input("Enter Second Number: "))
                break
            except ValueError:
                print("Please enter valid numbers only!")
    

    while(True):
        operator=input("Enter Operator (+ - * / %): ")

        if(operator=="+"):
            result=add(num1,num2)
            break

        elif(operator=="-"):
            result=subtract(num1,num2)
            break
        elif(operator=="*"):
            result=product(num1,num2)
            break
        elif(operator=="/"):
            if(num2==0):
                print("Dividing by ZERO is not Allowed!")
                continue
            result=divide(num1,num2)
            break
        elif(operator=="%"):
            if(num2==0):
                print("Modulus by ZERO is not Allowed!")
                continue
            result=modulus(num1,num2)
            break

        else:   
            print("Invalid Operator!")
        
    
    print(result)
    file=open("Baran_Calculator.txt","a")
    file.write(f"\t{num1} {operator} {num2} = {result}\n--------------------------------------------------\n")
    file.close()
 
  
    while(True):
        choice=input("Want to Calculate Again? (Yes/No)").strip().lower()
        
        if(choice=="yes"):
            break
           
        if(choice=="no"):
            print("Thanks For Using Baran's Calculator!")
            exit()
            
        else:
            print("Please type Yes or No only.")
           
    
        
        
        
         
      