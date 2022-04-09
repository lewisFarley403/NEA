import re


class Stack:
    def __init__(self):
        self.stack = []

    def peek(self):
        if self.isEmpty() == True:
            return None
        return self.stack[-1]

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop(-1)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class RPN:
    def __init__(self,exp):
        self.exp = exp
        self.rpn =self.CreateRPN(exp)

    def CreateRPN(self,exp):
        # https://www.andreinc.net/2010/10/05/converting-infix-to-rpn-shunting-yard-algorithm
        # tokens = ['+', '-', '*', '/', '^', '%']
        exp = exp.replace(' ', '')
        #print('exp ', exp)
        precedence = self.precedence
        tokens = self.tokens
        newExp = ''
        # split on the spaces, 3+4-> 3 + 4 so that all the symbols and numbers can be tokenised
        for token in tokens:
            for char in exp:
                if char == token:
                    #space at the start incase the symbol follows from a number, numbers wont have spaces because theyre not in the token array
                    newExp +=f' {char} '
                else:
                    newExp+=char # its a number
            exp = newExp #ready to repeat for the next character

            newExp =''
        tokenised = exp.split(' ')#do the split
        newTokenised=[]
        #remove the unecessary blank characters from subsequent symbols, ie ')*' ->' )  * ' which makes a mess when split 
        for t in tokenised:
            if t !='':
                newTokenised.append(t)
        tokenised= newTokenised
        print(tokenised)

        #shunting yard algorithm
        s = Stack()
        output = []
        for i, t in enumerate(tokenised):
            if t == '(':
                s.push(t)
            elif t == ')':
                while s.peek() != '(':
                    x = s.pop()
                    if x != '(':
                        output.append(x)
                s.pop()
            elif t in tokens:
                while not s.isEmpty() and s.peek() in list(precedence.keys()):
                    if precedence[t] <= precedence[s.peek()]:
                        x = s.pop()
                        output.append(x)
                    else:
                        break
                s.push(t)

                # s.pop()
            else:
                output.append(t)
        while s.isEmpty() == False:
            x = s.pop()
            print(f'also adding {x}')
            output.append(x)
        return output

    def cnvtAssembly(self):
        s = Stack()
        for char in self.rpn:
            if char not in self.tokens:
                s.push(char)
            else:
                x=s.pop()
                try:
                    x = float(x)
                    op1 = f'#{x}'
                except ValueError:
                    op1 = f'{x}'
                y=s.pop()








class Variable:
    def __init__(self, addr, value):
        self.addr = addr
        self.value = value

    def getDenary(self):
        return self.value

    def getBinary(self):
        return bin(self.value).replace("0b", "")

    def getHex(self):
        return hex(self.value).replace('0x', '')

    def clear(self):
        self.value = 0
class RPN:
    def __init__(self,exp):
        self.exp = exp
        self.precedence = {'+': 0, '-': 0, '*': 5, '/': 5, '%': 10, '^': 15}
        self.tokens = list(self.precedence.keys())
        self.tokens.append('(')
        self.tokens.append(')')
    def CreateRPN(self,exp):
        # https://www.andreinc.net/2010/10/05/converting-infix-to-rpn-shunting-yard-algorithm
        # tokens = ['+', '-', '*', '/', '^', '%']
        exp = exp.replace(' ', '')
        #print('exp ', exp)
        precedence = self.precedence
        tokens = self.tokens
        newExp = ''
        # split on the spaces, 3+4-> 3 + 4 so that all the symbols and numbers can be tokenised
        for token in tokens:
            for char in exp:
                if char == token:
                    #space at the start incase the symbol follows from a number, numbers wont have spaces because theyre not in the token array
                    newExp +=f' {char} '
                else:
                    newExp+=char # its a number
            exp = newExp #ready to repeat for the next character

            newExp =''
        tokenised = exp.split(' ')#do the split
        newTokenised=[]
        #remove the unecessary blank characters from subsequent symbols, ie ')*' ->' )  * ' which makes a mess when split 
        for t in tokenised:
            if t !='':
                newTokenised.append(t)
        tokenised= newTokenised
        print(tokenised)

        #shunting yard algorithm
        s = Stack()
        output = []
        for i, t in enumerate(tokenised):
            if t == '(':
                s.push(t)
            elif t == ')':
                while s.peek() != '(':
                    x = s.pop()
                    if x != '(':
                        output.append(x)
                s.pop()
            elif t in tokens:
                while not s.isEmpty() and s.peek() in list(precedence.keys()):
                    if precedence[t] <= precedence[s.peek()]:
                        x = s.pop()
                        output.append(x)
                    else:
                        break
                s.push(t)

                # s.pop()
            else:
                output.append(t)
        while s.isEmpty() == False:
            x = s.pop()
            print(f'also adding {x}')
            output.append(x)
        return output


    

class Interpretter:
    def __init__(self, line, variables, flag):

        self.operators = {'assignment': '=', 'block': ':'}
        self.line = line
        self.variables = variables
        self.instructionSet = {'+':'ADD','-':'SUB','*':'MULT','/':'DIV','^':'EXP','%':'MOD','=':'STR'}

    def parse(self):
        flags = []
        if self.line.find('if') != -1:  # if the line is selection
            pass




if __name__ == '__main__':
    #t = Tree('(3+5)/4', None)
    # print(CreateRPN('5+2*5+6'))
    print(CreateRPN('( ( 1  + 2 ) / 3 ) ^ 4'))
    print(CreateRPN('( ( 10  + 2 ) / 13 ) ^ 4'))
    #t = Tree('5*(4+3)/4', None)
    # print(t.smartSplit(t.root.value))
    # print(t.parseExpression(t.root.value))
    # print(t.root)
    # print(t.smartSplit(t.root.value))
    #print('generating ', t.generateGraph(t.root))
    # print(t.root.children[1].parent)
    # t.traverse()
    # print(5*(4+3)*4/3)
    # print(t.root.children[-1].forCalculating)
# [/5, []\, /+, []\, /3*4, [/3, []\, /*, []\, /4, []\]\]
# [/5, []\, /+, []\, /3*4, [/3, []\, /*, []\, /4, []\]\]
