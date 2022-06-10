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
        console.log(e.target.value);
        console.log("changed");
      });
      ram.push(inp);
    }
  }
  var input = createElement("textarea");
  input.attribute("rows", "10");
  input.attribute("cols", "50");
  input.attribute("style", "overflow:auto;resize:none");

  input.position(0, 0);
  createButton("submit")
    .mousePressed(() => {
      sim.assembly = input.value();
      console.log(input.value());
      console.log("pressed the button ready to send");
      console.log("in the then block");
      var assembly = new RPN(trim(input.value()), {});
      var instructions = assembly.compileToAssembly(
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
      console.log(instructions);
      console.log(assembly);

      for (var i = 0; i < instructions[0].length; i++) {
        var instruction = instructions[0][i];
        console.log(`looping ${instruction}`);
        ram[i].value(instruction);
      }
      console.log(assembly);
      // sim.assembly = assembly;
      sim.executeInstruction(sim.assembly);
    })
    .position(0, height - 50);
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
