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
    def __init__(self, exp, variables):
        self.variables = variables
        self.exp = exp
        self.precedence = {'+': 0, '-': 0, '*': 5, '/': 5, '%': 10, '^': 15}
        self.tokens = list(self.precedence.keys())
        self.tokens.append('(')
        self.tokens.append(')')
        self.rpn = self.CreateRPN(self.exp)

    def CreateRPN(self, exp):
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
                    # space at the start incase the symbol follows from a number, numbers wont have spaces because theyre not in the token array
                    newExp += f' {char} '
                else:
                    newExp += char  # its a number
            exp = newExp  # ready to repeat for the next character

            newExp = ''
        tokenised = exp.split(' ')  # do the split
        newTokenised = []
        # remove the unecessary blank characters from subsequent symbols, ie ')*' ->' )  * ' which makes a mess when split
        for t in tokenised:
            if t != '':
                newTokenised.append(t)
        tokenised = newTokenised
        print(tokenised)

        # shunting yard algorithm
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

    def compileToAssembly(self, instructionSet, currentAddress):
        s = Stack()
        instructions = []
        for char in self.rpn:
            if char not in self.tokens:
                s.push(char)
            else:
                print(s.isEmpty())
                x = s.pop()
                y = s.pop()
                print(x, y)
                intermediate = Variable(currentAddress, 0)
                self.variables[f'~{currentAddress}'] = intermediate
                code, errors = self.cnvtToAssembly(
                    x, y, intermediate, char, instructionSet)
                print(code)
                if errors != []:
                    return None, errors, None
                instructions.append(code)
                s.push(f'~{currentAddress}')
                currentAddress += 1
        return instructions, [], currentAddress

    def formatOperand(self, x):
        try:
            x = int(x)
            x = f'#{x}'
            return x
        except ValueError:
            if x in list(self.variables.keys()):
                var = self.variables[x]
                print(var)
                x = f'{var.addr}'
                return x
            else:
                # error, it means that the variable doesnt exist
                return None

    def cnvtSymbol(self, symbol, instructionSet):
        return instructionSet[symbol]

    def cnvtToAssembly(self, op1, op2, outputVariable, symbol, instructionSet):
        '''args: '''
        errors = []
        formattedOp1 = self.formatOperand(op1)
        if formattedOp1 == None:
            errors.append(f'{op1} is undefined')
            return None, errors
        formattedOp2 = self.formatOperand(op2)
        if formattedOp2 == None:
            errors.append(f'{op2} is undefined')
            return None, errors

        output = outputVariable.addr

        assemblyAcronym = self.cnvtSymbol(symbol, instructionSet)
        return [assemblyAcronym, formattedOp1, formattedOp2, output], []


if __name__ == '__main__':
    #t = Tree('(3+5)/4', None)
    # print(CreateRPN('5+2*5+6'))
    # print(CreateRPN('( ( 1  + 2 ) / 3 ) ^ 4'))
    # print(CreateRPN('( ( 10  + 2 ) / 13 ) ^ 4'))
    # r1 = RPN('( ( a + 2 ) / 3 ) ^ 4', {'a': Variable(0, 10)})
    r1 = RPN('(2+2)*4',{})
    print(r1.rpn)

    # r1 = RPN('2 + 2 ', {})
    # output = Variable(100, 0)
    # print(r1.compileToAssembly({'+': 'ADD', '-': 'SUB', '*': 'MULT',
    #                             '/': 'DIV', '^': 'EXP', '%': 'MOD', '=': 'STR'}, 0))
