class Stack {
  //stack for rpn
  constructor() {
    this.items = [];
  }
  push(item) {
    this.items.push(item);
  }
  pop() {
    return this.items.pop();
  }
  peek() {
    return this.items[this.items.length - 1];
  }
  isEmpty() {
    return this.items.length == 0;
  }
  size() {
    return this.items.length;
  }
  clear() {
    this.items = [];
  }
}
class Variable {
  constructor(addr, value) {
    this.addr = addr;
    this.value = value;
  }
}
const InstructionSet = {
  "+": "ADD",
  "-": "SUB",
  "*": "MULT",
  "/": "DIV",
  "^": "EXP",
  "%": "MOD",
  "=": "STR",
};
class RPN {
  constructor(exp, variables, outputR) {
    this.exp = exp;
    this.isAssignment = true ? this.exp.includes("=") : false;
    this.variables = variables;
    this.previousInstructions = [];
    this.precedence = {
      "+": 0,
      "-": 0,
      "*": 5,
      "/": 5,
      "%": 10,
      "^": 15,
    };
    this.outputR = outputR;
    //defined by shunting yard algorithm
    this.tokens = Object.keys(this.precedence);
    //need to know special chars to identify the operators, cant use precdedence keys because () dont have precedence

    this.tokens.push("(");
    this.tokens.push(")");

    this.rpn = this.createRPN(this.exp); //create the correct order of operations
    this.instructions = this.compileToAssembly(InstructionSet, this.outputR);
  }
  setPreviousInstructions(instructions) {
    this.previousInstructions = instructions;
  }
  concat(otherRPN) {
    console.log(this.variables);
    // this.variables.concat(otherRPN.variables);
    this.variables = Object.assign(this.variables, otherRPN.variables);
    this.previousInstructions.concat(
      otherRPN.previousInstructions,
      otherRPN.instructions[0] //raw instructions
    ); //needs to be compiled to have .instructions. maybe make the instruction set global or standardise it so that it doesnt need to be passed as a parameter to everything
  }
  createRPN(exp) {
    let rpn = [];
    let stack = new Stack();
    for (let i = 0; i < exp.length; i++) {
      let token = exp[i];
      if (this.tokens.includes(token)) {
        //if the token isnt special char
        if (token == "(") {
          stack.push(token);
          //push bracket
        } else if (token == ")") {
          while (stack.peek() != "(") {
            //pop all the tokens until you find the opening bracket
            rpn.push(stack.pop());
          }
          stack.pop(); //pop off the bracket
        } else {
          while (
            !stack.isEmpty() &&
            this.precedence[token] <= this.precedence[stack.peek()]
          ) {
            rpn.push(stack.pop());
          }
          stack.push(token);
        }
      } else {
        rpn.push(token);
      }
    }
    while (!stack.isEmpty()) {
      rpn.push(stack.pop());
    }
    return rpn;
  }
  compileToAssembly(instructionSet, startRegister) {
    //args: instructionSet, startRegister
    //returns: assembly code, errors
    //instructionSet is a dict of instructions and their corresponding assembly acronym
    //startRegister is the register to start writing to
    instructionSet = InstructionSet;
    console.info("running at the beginning of the function");
    var s = new Stack();
    var instructions = [];
    for (var char of this.rpn) {
      if (!this.tokens.includes(char)) {
        console.info(`pushed ${char} to the stack`);
        s.push(char);
      } else {
        var x = s.pop();
        var y = s.pop();
        console.info(`x:y popped ${x}, ${y}`);

        var intermediate = `R${startRegister}`;
        startRegister++;
        var code, errors;
        console.info(`creating instruction ${char} ${x}, ${y}`);
        var y = this.cnvtInstruction(x, y, intermediate, char, instructionSet);
        code = y[0];
        errors = y[1];
        console.info(`code is ${code}`);
        if (errors.length > 0) {
          console.info(`errors are ${errors}`);
          return null, errors, null;
        }
        instructions.push(code);
        s.push(`R${startRegister - 1}`);
      }
    }

    if (this.isAssignment) {
      let identifier = this.exp.slice("=")[0];
      this.variables[identifier] = new Variable(`R${startRegister - 1}`, 0);
    }
    this.outputR = startRegister++;

    // console.log(instructions);
    return [instructions, [], startRegister];
  }
  cnvtInstruction(op1, op2, outputVariable, symbol, instructionSet) {
    //op1 and op2 are operands
    //outputVariable is the variable to write to
    //symbol is the operator
    //instructionSet is a dict of instructions and their corresponding assembly acronym
    var errors = [];
    console.log(`op1 is ${op1}`);
    var formattedOp1 = this.formatOperand(op1);
    if (formattedOp1 == null) {
      errors.push(`${op1} is undefined`);
      return null, errors;
    }
    var formattedOp2 = this.formatOperand(op2);
    if (formattedOp2 == null) {
      errors.append(`${op2} is undefined`);
      return None, errors;
    }
    var output = outputVariable;

    var assemblyAcronym = this.cnvtSymbol(symbol, instructionSet);
    return [[assemblyAcronym, formattedOp1, formattedOp2, output], []];
  }

  cnvtSymbol(symbol, instructionSet) {
    return instructionSet[symbol];
  }
  formatOperand(x) {
    //x is the operand
    //returns the operand in the correct format

    if (!isNaN(x)) {
      x = `#${x}`;
    } else {
      if (Object.keys(this.variables).includes(x)) {
        //if the variable is defined in the variable dict, read its memory address
        x = this.variables.x;
      } else {
        //panic
        console.log(`panic ${x}`);
      }
    }
    return x;
  }
}
var rpn = new RPN("(2+2)*4", {});
console.log(rpn.rpn);

var x = rpn.compileToAssembly(
  {
    "+": "ADD",
    "-": "SUB",
    "*": "MULT",
    "/": "DIV",
    "^": "EXP",
    "%": "MOD",
    "=": "STR",
  },
  0
);
print(x);
console.log(x);
