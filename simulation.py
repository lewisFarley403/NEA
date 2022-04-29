from compiler import Variable, RPN


class RAM:
    def __init__(self, size=100):
        self.size = size
        self.block = self.createMemoryBlock(size)

    def write(self, variable):
        if variable.addr > self.size:
            # writing over the ram space
            pass
        else:
            self.block[variable.addr] = variable.value

    def read(self, addr):
        return Variable(addr, self.block[addr])


class CPU:
    def __init__(self, RAM):
        self.ram = RAM
        # special registers
        self.acc = 0
        self.pc = 0  # might need to change this because the process may not start at addr 0

        # --------------------------------------------------------------------------------
        self.instructionSet = {
            '+': 'ADD', '-': 'SUB', '*': 'MULT', '/': 'DIV', '^': 'EXP', '%': 'MOD', '=': 'STR'}

    def readRAM(self, addr):
        self.ram.read(addr)

    def getNumbers(self, op):
        if op.find('#') != -1:
            return float(op.replace('#', ''))
        else:
            op = self.readRAM(float(op))

    def add(self, op1, op2):
        x = self.getNumbers(op1)  # they could be pointing to an address
        y = self.getNumbers(op2)
        return x+y

    def sub(self, op1, op2):
        pass

    def div(self, op1, op2):
        pass

    def mult(self, op1, op2):
        pass

    def passAssemblyLine(self, code):
        operator = code[0]
        operand_1 = code[1]
        operand_2 = code[2]
        for symbol, assembly in self.instructionSet.items():
            if assembly == operator:
                # carry out the correct operations

                if symbol == '+':
                    print('in +')
                    answer = self.add(operand_1, operand_2)
                    return answer
                elif symbol == '-':
                    answer = self.sub(operand_1, operand_2)
                elif symbol == '*':
                    answer = self.mult(operand_1, operand_2)


class Simulation:
    def __init__(self, code, variables, currentAddress):

        self.operators = {'assignment': '=', 'block': ':'}
        self.lines = code.split('\n')

        self.variables = variables
        self.instructionSet = {'+': 'ADD', '-': 'SUB', '*': 'MULT',
                               '/': 'DIV', '^': 'EXP', '%': 'MOD', '=': 'STR'}
        self.currentAddress = currentAddress
        self.lineNumber = 0
        self.currentLine = self.lines[self.lineNumber]

    def parse(self):
        varExp = self.currentLine.split('=')
        assembly, runTimeErrors, currentAddress = RPN(
            varExp[-1]).compileToAssembly(self.instructionSet, self.currentAddress)
        var = varExp[0]
        if runTimeErrors:
            pass  # needs implementing
        else:
            self.lineNumber += 1
            self.currentLine = self.lines[self.lineNumber]

            return assembly


if __name__ == '__main__':
    c = CPU(None)
    print(c.passAssemblyLine(['ADD', '#3', '#4', '0']))
