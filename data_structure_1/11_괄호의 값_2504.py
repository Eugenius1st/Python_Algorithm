import sys
sys.stdin = open("input.txt", "rt")

s = input()
stack = []

for x in s:
    if x =='(':
        stack.append('(')
    elif x == '[':
        stack.append('[')
    elif stack and x ==')':
        if stack[-1] == '(':
            stack.pop()
    elif stack and x == ']':
        if stack[-1] == '[':
            stack.pop()
    else:
        print(0)
        exit()
if stack:
    print(0)
    exit()

def plus():
    while len(stack)>1: 
        a, int1 = stack[-1]
        b, int2 = stack[-2]
        if a or b:
            break
        stack.pop()
        stack.pop()
        stack.append((None, int1+int2))

for x in s:
    if x == '(':
        stack.append(('(',2))
    elif x == '[':
        stack.append(('[',3))
    elif x == ')' or x == ']':
        lastB, lastN = stack.pop()
        if lastB != None: 
            stack.append((None, lastN)) 
        else: 
            a , b = stack.pop()
            stack.append((None, lastN * b))
        plus()
print(stack[-1][1])