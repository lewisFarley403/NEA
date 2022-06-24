class Animation {
  constructor(sprite) {
    this.frameNumber = 0;
    this.running = true;
    this.sprite = sprite;
  }
}
class FetchAnimation extends Animation {
  constructor(sprite, startPos, stopPos, speed) {
    super(sprite);
    this.startCoord = createVector(startPos.x, startPos.y);
    this.stopCoord = createVector(stopPos.x, stopPos.y);
    this.stopCoord.sub(this.startCoord);
    this.movementVector = this.stopCoord;

    this.movementVector.normalize();

    this.movementVector = this.movementVector.mult(speed);
    console.log(this.movementVector);

    this.positionAtFrame = (frame) => {
      return this.startCoord.add(this.movementVector.mult(frame));
    };
  }
  drawFrame() {
    // console.log("an draw");
    var frameVector = this.positionAtFrame(this.frame);
    // console.log(frameVector.x, frameVector.y);
    rect(frameVector.x, frameVector.y, 10, 10);
    this.frame++;
  }
}
