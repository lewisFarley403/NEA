const boxFill = 100;
const textFill = 1;
class Sim {
  constructor(assembly, w, ram, x, y) {
    this.ram = ram;
    this.assembly = assembly;
    this.sign = loadImage("bus stop.png");

    this.values = { PC: 0, ACC: 0, MDR: 0, MAR: 0, register: {} };
    this.width = (1 / 2) * w;
    this.x = x;
    this.y = y;
    this.drawCpu();
  }
  setWidth(w) {
    this.width = 0.5 * w;
  }

  drawCpu() {
    // this.width = this.this.width
    fill(100);

    rect(this.x + 0, this.y + height / 2, this.width, height / 2);
    rect(this.x + 0, this.y + height / 2, this.width / 4, height / 4); //mdr
    fill(textFill);
    textAlign(CENTER, CENTER);
    // text('MDR',0.5*this.width/4,height/2+0.5*height/4)
    text(
      `MDR\n${this.values.MDR}`,
      ...this.findTextXY(0, height / 2, this.width / 4, height / 4)
    );

    fill(boxFill);
    rect(
      this.x + this.width / 4,
      this.y + height / 2,
      this.width / 4,
      height / 4
    );
    fill(textFill);
    text(
      `PC\n${this.values.PC}`,
      ...this.findTextXY(this.width / 4, height / 2, this.width / 4, height / 4)
    );

    //blank
    //mdr
    fill(boxFill);
    this.marAddr = { x: this.x + 3 * (this.width / 4), y: this.y + height / 2 };
    rect(
      this.x + 3 * (this.width / 4),
      this.y + height / 2,
      this.width / 4,
      height / 4
    );
    fill(textFill);
    text(
      `MAR\n${this.values.MAR}`,
      ...this.findTextXY(
        3 * (this.width / 4),
        height / 2,
        this.width / 4,
        height / 4
      )
    );

    //bottom row
    fill(boxFill);
    rect(this.x + 0, this.y + height * (7 / 8), this.width / 4, height / 8);
    fill(textFill);
    text(
      `Acc\n${this.values.ACC}`,
      ...this.findTextXY(0, height * (7 / 8), this.width / 4, height / 8)
    );

    fill(boxFill);
    rect(
      this.x + this.width / 4,
      this.y + height * (7 / 8),
      this.width / 2,
      height / 8
    );
    fill(textFill);
    text(
      "CU",
      ...this.findTextXY(
        this.width / 4,
        height * (7 / 8),
        this.width / 2,
        height / 8
      )
    );

    fill(boxFill);
    rect(
      this.x + this.width * (3 / 4),
      this.y + height * (7 / 8),
      this.width / 4,
      height / 8
    );
    fill(textFill);
    text(
      "ALU",
      ...this.findTextXY(
        this.width * (3 / 4),
        height * (7 / 8),
        this.width / 4,
        height / 8
      )
    );
  }
  findTextXY(bx, by, bw, bh) {
    return [this.x + bx + bw / 2, this.y + by + bh / 2];
  }
  show() {
    this.drawCpu();
  }
  executeCode() {
    for (instruction of this.assembly) {
      this.executeInstruction(instruction);
    }
  }
  executeInstruction(instruction) {
    //expands the instruction
    var opcode = instruction[0];
    var op1 = instruction[1];
    var op2 = instruction[2];
    var ouputRegister = instruction[3];
    //decides what to do with the opcodes
    switch (opcode) {
      case "ADD":
        this.values.ACC = op1 + op2;
        break;
      case "SUB":
        this.values.ACC = op1 - op2;
        break;
      case "MUL":
        this.values.ACC = op1 * op2;
        break;

      case "DIV":
        this.values.ACC = op1 / op2;
        break;
      case "EXP":
        this.values.ACC = Math.pow(op1, op2);
        break;
    }
    this.values.register[ouputRegister] = this.values.ACC;
  }
  fetchValue(address) {
    console.log(this.marAddr);
    var a = new FetchAnimation(null, this.marAddr, { x: 0, y: 0 }, 1);
    console.log(a);
    return a;
  }
}
