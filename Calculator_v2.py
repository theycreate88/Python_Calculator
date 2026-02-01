
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
    
    try:
        command=int(input("1.Calculate\n2.History\n3.Clear History\n4.Exit\nEnter Command: "))
        
    except ValueError:
            print("Invalid Input!")
            continue
        
    if(command==1):
        expression=input("Enter Expression: ").split()
        if(expression.__len__()!=3):
            print("FORMAT ERROR!")
            continue
        try:  
            num1=float(expression[0])
            num2=float(expression[2])
        
        except ValueError:
            print("\n\tOnly Numeric Values are Acceptable!\n")
            continue
   
        operator=expression[1]
        
        if(operator=="+"):
            result=add(num1,num2)


        elif(operator=="-"):
            result=subtract(num1,num2)
         
        elif(operator=="*"):
            result=product(num1,num2)
            
        elif(operator=="/"):
            if(num2==0):
                print("Dividing by ZERO is not Allowed!")
                continue
            result=divide(num1,num2)
         
        elif(operator=="%"):
            if(num2==0):
                print("Modulus by ZERO is not Allowed!")
                continue
            result=modulus(num1,num2)

        else:   
            print("Invalid Operator!")
            continue
        
        print(f"\t{num1} {operator} {num2} = {result}")
    
        file=open("theycreate_Calculator_v2.txt","a")
        file.write(f"\t{num1} {operator} {num2} = {result}\n--------------------------------------------------\n")
        file.close()

    elif(command==2):
        try:   
            file=open("theycreate_Calculator_v2.txt","r")
            lines=file.readlines()
      
            if len(lines)==0:
                print("\n\tNO HISTORY AVAILABLE!\n")
                file.close()           
            else:
                print("================= H I S T O R Y ====================\n")  
       
                for line in lines:
                    print(line,end="")
                file.close()
        except FileNotFoundError:
            print("\n\tNO HISTORY AVAILABLE!\n")
        
        
    elif(command==3):
        open("theycreate_Calculator_v2.txt", "w").close()
        print("HISTORY CLEARED")
        
    elif(command==4):
        print("--- THANKS FOR USING theycreate's Calculator version 2.0 ---")
        break
        
        
        
    
    
        
        
         
      