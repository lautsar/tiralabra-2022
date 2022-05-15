import queue
import re

def main():
    while True:
        lauseke = input("Lauseke: ")

        if lauseke == 'q':
            break

        shunting_yard(lauseke)

def shunting_yard(lauseke):
    input = lauseke.split()
    output = []
    operator_stack = []


    for token in input:
        if re.findall("^[0-9]+$", token):
            #print("numero")
            output.append(token)
        elif token == '+' or token == '-':
            #print('operaattori')
            while len(operator_stack) > 0:
                if operator_stack[len(operator_stack)-1] != '(':
                    output.append(operator_stack.pop())
                else:
                    break
            
            operator_stack.append(token)
        elif token == '(':
            #print('vasen sulku')
            operator_stack.append(token)
        elif token == ')':
            #print('oikea sulku')
            if len(operator_stack) == 0:
                print('väärä määrä sulkuja')

            while len(operator_stack) > 0 and operator_stack[len(operator_stack)-1] != '(':
                output.append(operator_stack.pop())

            if len(operator_stack) > 0 and operator_stack[len(operator_stack)-1] == '(':
                operator_stack.pop()

        else:
            print('virhe')
    
        print(f"{output} ja {operator_stack}")
    
    for token in operator_stack:
        operator = operator_stack.pop()
        if operator == '(':
            print('väärä määrä sulkuja')
            break
        else:
            output.append(token)
        
    print(output)
    evaluate(output)
    #print(operator_stack)

def evaluate(output):
    stack = []

    for token in output:
        if re.findall("^[0-9]+$", token):
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(int(a) + int(b))
            elif token == '-':
                stack.append(int(b) - int(a))
            else:
                print('jotain meni pieleen')
        
        print(stack)
    
    #print(stack)



if __name__ == "__main__":
    main()