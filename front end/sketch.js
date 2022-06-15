var sim;
var ram = [];
const ramSize = 16;

function setup() {
  //send axios request to get the program
  createCanvas(windowWidth, windowHeight);

  var itter = ceil(ramSize ** 1 / 2);
  for (var x = 0; x < itter; x++) {
    for (var y = 0; y < itter ** 1 / 2; y++) {
      var inp = createInput("0");
      inp.size(50);
      // position the element
      inp.position((3 * width) / 4 + y * 50, height / 2 + (x * 50) / 2);
      inp.attribute("id", `${x}${y}`);
      inp.changed((e) => {
        1 + 1;
        //place holder, the value of ram has changed
      });
      ram.push(inp);
    }
  }
  function translateMultiline(lines) {
    console.error(`lines of code ${lines}`);

    var register = 0; // the first free register to start storing variables to

    var variables = {}; //variables to be used in each line

    var instructions = [];

    for (var i = 0; i < lines.length; i++) {
      var line = lines[i];

      //RPN first line
      var lineRPN = new RPN(line, variables, register);
      var res = lineRPN.compileToAssembly({}, register);
      console.error(`${line} has this res ${res}`);
      console.error("rpn obj for this line :");
      console.error(lineRPN);
      console.error(`confirming variables is correct`);
      console.error(lineRPN.variables);
      register = res[2] + 1; //sets the next available register to the 1+ the last register used by that line

      variables = Object.assign(variables, lineRPN.variables); //merges the variables to use for the next line
      console.error(`variables after the merger ${variables}`);
      instructions = instructions.concat(res[0]); //merge the instructions
      console.error(instructions);
    }
    return instructions;
  }
  //sets up the code input area
  var input = createElement("textarea");
  input.attribute("rows", "10");
  input.attribute("cols", "50");
  input.attribute("style", "overflow:auto;resize:none");
  //------------------------------------------------------------------

  input.position(0, 0);
  createButton("Translate Program")
    .mousePressed(() => {
      sim.assembly = input.value();
      var afterMultiline = new RPN("", {});

      //splits the code into lines
      var inst = trim(input.value());
      inst = inst.split("\n");

      var outputRegister = 0;

      var assembly = translateMultiline(inst);
      console.log(assembly);
      // sim.assembly = assembly;
    })
    .position(0, 150);
  sim = new Sim(
    [
      [
        ["ADD", "#2", "#2", 0],
        ["DIV", "#3", "0", 1],
        ["EXP", "#4", "1", 2],
      ],
      [],
      3,
    ],
    width,
    ram,
    0,
    0
  );
}

function draw() {
  background(220);
  sim.show();
  // sim.values.MDR += 1;
  // ram[9].value(sim.values.MDR);
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  sim.setWidth(windowWidth);
}
