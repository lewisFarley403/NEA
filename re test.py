import re
exp = '5*(6+3)*4/3'
x = re.search('\(.*\)', '5*(6+3)*4/3')
x = re.search('\+', '5*(6+3)*4/3')

s = x.start()
e = x.end()
brackets = re.search(r'\(.*\)', exp)
# print([x.string[:s], x.string[s+1:e-1].replace(), x.string[e:]])
# print(brackets.span())
middle = x.string[s:e]
# middle = middle.replace('(', '')
# middle = middle.replace(')', '')
# res = [x.string[:s], middle, x.string[e:]]
if brackets.span()[0] < s < brackets.span()[-1]:
    pass
res = []
if x.string[:s] != '':
    res.append(x.string[:s])
if middle != '':
    res.append(middle)
if x.string[e:] != '':
    res.append(x.string[e:])
# ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__',
#     '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'end', 'endpos', 'expand',
#  'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']

splitString = '\+|\-|\*|\/|\%'

x = re.findall(splitString, exp)
for i in x:
    print(i)
precedence = {'+': 0, '-': 0, '*': 5, '/': 5, '%': 10, '^': 15}
tokens = list(precedence.keys())
tokens.append('(')
tokens.append(')')
pattern = ''
for t in tokens:
    pattern += f'/{t}|'

x = re.finditer(pattern[:-1], exp)
e = exp
for i, m in enumerate(x):
    # print(m.string)
    # print((m.start(0), m.end(0)))
    exp = exp[:m.end(0)+i]+' '+exp[m.end(0)+i:]
    t = exp.split(' ')
    t.pop(0)
    tokens.pop(-1)
    print(tokens)
