def main():
    name=input("What is Your Name ?:")
    print(f"Hello Welcome:{name}")
    print("Select Options Below")
    print("1.Calculator ")
    print("2.Hotel Menu")
    print("3.Football Teams")
    print("4.Assets Calculator")
    opt=int(input("Enter Option:"))

    if opt == 1:
        result = calc()
        print(f"Result: {result}")
    elif opt == 2:
       result = menu()
       print(f"Result: {result}")
    elif opt == 3:
        return fteams()
    elif opt == 4:
        returnAcalc()
    else:
        return "Nothing Selected"
    
def calc():
    a=int(input("Enter Number 1:"))
    b=int(input("Enter Number 2:"))
    print("Operations")
    print("1.Add")
    print("2.Sub")
    print("3.Multiply")
    print("4.Divide")
    operand=input("Enter Operation:1/2/3/4/")

    if operand =='1':
        result=a+b
        return result
    elif operand == '2':
        result=a-b
        return result
    elif operand == '3':
       result=a*b
       return result
    elif operand == '4':
        result=a/b
        return result
    else :
        return "No  Valid operations found"
def menu():
    items=['Mukimo','Ugali Fry','Chapo Ndondo','Githeri Viazi','Chai','Kadhalika']
    for item in items:
        print(item)
        
        
    
main()