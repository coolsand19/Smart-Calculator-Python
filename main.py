import re

print("Making calculator...")

def main():
    c = 0
    while(True):
        if  c != 0:
            print("Hello again!")
        print("Welcome to Smart Calculator")
        sentence = input("Enter your query for calculation: ")
        l1 = sentence.split()
        if len(l1)==1 and (l1[0] == 'false' or l1[0] == 'False' or l1[0] == 'exit' or l1[0] == 'quit'):
           print("Thanks...")
           break
        ans = makeEquation(l1)
        if ans is None:
            print("Could not parse the input!. Please enter a valid equation.\n")
            print("Type exit, quit or false to end the program")
            continue
        print(f"Answer: {ans}\n")
        print("Type exit, quit or false to end the program")
        c = 1


def Add(a,b):
    return a+b

def Subtract(a,b):
    return a-b

def Multiply(a,b):
    return a*b  

def Divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:            
        return "Error! Division by zero."
def Modulus(a,b):
    try:
        return a%b
    except ZeroDivisionError:            
        return "Error! Division by zero."
    
def parse_equation(equation):
     # This regex captures: operand1, operator, operand2
    neq = ""
    chars = []
    for ch in equation:
        if not ch.isalpha():
            chars.append(ch);
    neq = "".join(chars)
    match = re.match(r'^\s*([-\d.]+)\s*([+\-*/xX÷%])\s*([-\d.]+)\s*$', neq)
    if match:
        operand1 = float(match.group(1))
        operator = match.group(2)
        operand2 = float(match.group(3))
        return operand1, operator, operand2
    else:
        return None
    

def makeEquation(l1):
    operator = None
    oprd1 = None
    oprd2 = None
    if len(l1) == 1:
        result = parse_equation(l1[0])
        if result is None:
            return None
        oprd1,operator,oprd2 = result
    else:
        for r in l1:
            r = r.lower()
            if r in ('+', 'plus', 'add', 'addition'):
                operator = '+'
            elif r in ('-', 'minus', 'subtract', 'subtraction', 'sub', 'difference'):
                operator = '-'
            elif r in ('*', 'x', 'X', 'times', 'multiply', 'multiplication','product'):
                operator = '*'
            elif r in ('/', '÷', 'divide', 'division','divided', 'by'):
                operator = '/'
            elif r in ('%', 'mod', 'modulus'):
                operator = '%'
            else:
                try:
                    num = float(r)
                    if oprd1 is None:
                        oprd1 = num
                    elif oprd2 is None:
                        oprd2 = num
                except ValueError:
                    continue
    if operator != None and oprd1 and oprd2 is not None:
        if operator == '+':
            return Add(oprd1, oprd2)
        elif operator == '-':
            return Subtract(oprd1, oprd2)
        elif operator == '*':
            return Multiply(oprd1, oprd2)
        elif operator == '/':
            return Divide(oprd1, oprd2)
        elif operator == '%':   
            return Modulus(oprd1, oprd2)


if __name__ == "__main__":
    main()

   

