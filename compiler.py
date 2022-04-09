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


def CreateRPN(exp):
    # https://www.andreinc.net/2010/10/05/converting-infix-to-rpn-shunting-yard-algorithm
    # tokens = ['+', '-', '*', '/', '^', '%']
    exp = exp.replace(' ', '')
    #print('exp ', exp)
    precedence = {'+': 0, '-': 0, '*': 5, '/': 5, '%': 10, '^': 15}
    tokens = list(precedence.keys())
    tokens.append('(')
    tokens.append(')')
    print(tokens)

    pattern = ''
    for t in tokens:
        pattern += f'/{t}|'

    print(pattern[:-1])

    x = re.finditer(pattern[:-1], exp)
    e = exp
    for i, m in enumerate(x):
        # print(m.string)
        print((m.start(0), m.end(0)))
        exp = exp[:m.end(0)+i]+' '+exp[m.end(0)+i:]
        if m.start(0) != m.end(0):
            exp = exp[:m.start(0)+i]+' '+exp[m.start(0)+i:]
        print(exp+'\n')
        tokenised = exp.split(' ')
        tokenised.pop(0)
        # tokenised.pop(-1)
    print(tokenised)

    # splitString = ''
    # for t in tokens:
    #     splitString += f'\\{t}|'
    # splitString = splitString[:-1]
    # # this will split on all the opporators, but also remove them
    # tokenised = re.split(splitString, exp)
    # # print(tokenised)
    # ops = re.split('[1-9A-Za-z]*', exp)  # split on all numbers but remove them
    # x = []
    # # merge the lists together
    # for op in ops:
    #     if op != '':
    #         x.append(op)
    # ops = x
    # count = 0
    # for i in range(1, len(tokenised), 1):
    #     # + count to offset the fact that the array is changing a it is itterated
    #     tokenised.insert(i+count, ops[count])
    #     count += 1
    # splitString = ''
    # for t in tokens:
    #     splitString += f'\\{t}|'
    # re.findall(splitString, exp)
    # print(tokenised)
    # shunting algorithm
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
        output.append(x)
    return output


class Tree:
    def __init__(self, rootExpression, parent, create=True):
        self.root = Node(rootExpression, True, parent)
        self.tokens = ['*', '/', '+', '-', ]  # (?!\()\+(?!\))  '(.*\)'
        if create == True:
            self.create()

    def parseExpression(self, exp):
        '''using regular expressions allows the split to be smarter than using regular split methods'''
        print(exp)
        for op in self.tokens[::-1]:
            # print(op)
            if op == exp:
                print(f'{op} == {exp}')
                return exp, False
            x = re.search(f'\{op}', exp, 2)
            # only match the sign if it isnt enclosed in ()
            #x = re.search(f'(?!\()[a-zA-Z1-9]+\{op}[a-zA-Z1-9]+(?!\))', exp, 2)
            # x = re.search(f'(?!\()\{op}(?!\))', exp, 2)
            if x == None:
                continue
            print(f'found operator {op} for {exp}')
            s = x.start()

            e = x.end()

            try:
                brackets = re.search(r'\(.*\)', exp)

                if brackets.span()[0] < s < brackets.span()[-1]:
                    continue
            except AttributeError:
                pass

            middle = x.string[s:e]
            # middle = middle.replace('(', '')
            # middle = middle.replace(')', '')
            # res = [x.string[:s], middle, x.string[e:]]
            res = []
            if x.string[:s] != '':
                res.append(x.string[:s])
            if middle != '':
                res.append(middle)
            if x.string[e:] != '':
                res.append(x.string[e:])
            print(f'returned normally split on the {op},{exp}')
            return res, True
        noBracket = exp.replace('(', '')
        noBracket = noBracket.replace(')', '')
        if noBracket != exp:
            res = self.parseExpression(noBracket)
            if res[1] == True:
                print(f'res {res}')

                return res
        print(f'returning {exp} and False')
        return exp, False
    # def parseExpression(self, exp):

    #     for token in self.tokens[::-1]:
    #         if exp == token:
    #             return exp, False

    #         if len(exp.split(token)) != 1:
    #             print(f'{token} found in the exp, {exp}')
    #             tokens = exp.split(token)
    #             tokens.insert(1, token)
    #             return tokens, True
    #     return exp, False

    def create(self):
        #print('creating ', self.root.value)
        x, _ = self.parseExpression(self.root.value)
        if len(x) != 1:
            for term in x:
                #print('added ', term)
                self.root.addSubtree(term)

    def traverse(self):
        # left walk
        deepLeft = self.traverseDown(0)
        deepRight = self.traverseDown(-1)
        toCalculate = [deepRight, deepLeft]
        print('LEFT RIGHT')
       # print(f'deep left :: {deepLeft}\ndeep right :: {deepRight}')
        root = deepRight
        while root != self.root.value:
            print('VALUES :')
            print(root.children[0].value)
            print(root.children[1].value)
            print(root.children[2].value)
            try:
                res = self.calculate(
                    root.children[0].value, root.children[1].value, root.children[2].value)
                root.value = res
                if root.parent == None:
                    print(f'{root.value} has a non parent')
                    break

                root = root.parent
            except ValueError:
                x = toCalculate[0]
                toCalculate.pop(0)
                toCalculate.append(x)
                root = toCalculate[0]

    def __repr__(self):
        root = self.root
        string = f'{root.value}'
        while True:
            pass

    def calculate(self, op1, operator, op2):
        #print(f'op1 ="{op1}", op2={op2}')
        # op1 = op1.strip()
        # op2 = op2.strip()
        if operator == '+':
            return float(op1)+float(op2)
        elif operator == '-':
            return float(op1)-float(op2)
        elif operator == '*':
            return float(op1)*float(op2)
        elif operator == '/':
            return float(op1)/float(op2)

    def traverseDown(self, index):
        root = self.root
        while True:
            # print(root)
            kids = root.children
            if len(kids) != 0:
                root = kids[index]
            else:
                if root.parent == None:
                    print(root.value, 'has a none parent')
                    break
                print(root.parent)
                return root.parent


class Node:
    def __init__(self, value, needsExpanding, parent):
        self.parent = parent
        self.value = value
        self.children = []
        self.needsExpanding = needsExpanding
        self.forCalculating = []

    def addChild(self, value, needsExpanding):
        print('adding child ', self)
        self.children.append(Node(value, needsExpanding, self))

    def addSubtree(self, value):
        tree = Tree(value, self)
        self.children.append(tree.root)

    def __repr__(self):
        return f'/{self.value}, {self.children}\\'


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


class Interpretter:
    def __init__(self, line, variables, flag):
        self.operators = {'assignment': '=', 'block': ':'}
        self.line = line
        self.variables = variables

    def parse(self):
        flags = []
        if self.line.find('if') != -1:  # if the line is selection
            pass


class ConditionTree (Tree):
    def __init__(self, condition):
        super().__init__(condition, create=False)
        self.tokens = []


if __name__ == '__main__':
    #t = Tree('(3+5)/4', None)
    # print(CreateRPN('5+2*5+6'))
    print(CreateRPN('( ( 1  + 2 ) / 3 ) ^ 4'))
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
