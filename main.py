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
            break
        ans = makeEquation(l1)
        print(f"Answer: {ans}\n")
        print("Type exit, quit or false to end the program")
        c = 1


def add(a,b):
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
    
def parse_equation(equation):
     # This regex captures: operand1, operator, operand2
    match = re.match(r'^\s*([-\d.]+)\s*([+\-*/xX÷])\s*([-\d.]+)\s*$', equation)
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
            oprd1 = result[0]
            operator = result[1]    
            oprd2 = result[2]
        else:
            for r in l1:
                r = r.lower()
                if r in ('+', 'plus', 'add', 'addition'):
                    operator = '+'
                elif r in ('-', 'minus', 'subtract', 'subtraction', 'sub'):
                    operator = '-'
                elif r in ('*', 'x', 'X', 'times', 'multiply', 'multiplication'):
                    operator = '*'
                elif r in ('/', '÷', 'divide', 'division'):
                    operator = '/'
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
                return add(oprd1, oprd2)
            elif operator == '-':
                return Subtract(oprd1, oprd2)
            elif operator == '*':
                return Multiply(oprd1, oprd2)
            elif operator == '/':
                return Divide(oprd1, oprd2)


if __name__ == "__main__":
    main()

   

