import sys
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QPushButton, QApplication, QLineEdit, QPlainTextEdit, QImage)
import math
from compiler import RPN
from pygameSim import VisualSimulation
from simulation import Simulation


class Window(QWidget):
    def __init__(self):
        self.ramSize = 25
        super().__init__()
        grid_layout = QGridLayout()
        self.visualSimulation = VisualSimulation(None)
        self.setLayout(grid_layout)
        ramBlockWidget = QWidget()
        self.ramBlock = QGridLayout()
        ramBlockWidget.setLayout(self.ramBlock)
        for x in range(int(math.sqrt(self.ramSize))):
            for y in range(int(math.sqrt(self.ramSize))):
                # line = QLineEdit(self)
                # make a new qlineedit with defalt text 0
                line = QLineEdit("0")
                self.ramBlock.addWidget(line, x, y)

        grid_layout.addWidget(ramBlockWidget)

        # used as a spacer so far, will replace with the simulation image from pygame
        self.pygameWindow = QImage(
            self.visualSimulation.size[0], self.visualSimulation.size[1], QImage.Format_RGB32)
        self.renderPygame()

        grid_layout.addWidget(QPushButton(self), 0, 1)
        # add image of simulation
        self.visualSimulation.drawCPU()
        grid_layout.addWidget(self.visualSimulation.show(), 0, 1)

        self.codeInputWidget = QWidget()
        self.codeInputGrid = QGridLayout()
        self.codeInputWidget.setLayout(self.codeInputGrid)
        self.codeEdit = QPlainTextEdit()
        self.codeInputGrid.addWidget(self.codeEdit, 0, 0, -1, -1)

        self.compileButton = QPushButton('Compile')
        self.compileButton.clicked.connect(self.onCompile)

        self.codeInputGrid.addWidget(self.compileButton, 1, 1)

        self.runButton = QPushButton('Run')
        self.codeInputGrid.addWidget(self.runButton, 1, 0)
        grid_layout.addWidget(self.codeInputWidget, 0, 2)

    def renderPygame(self):
        '''this function will render the pygame window as an image to the pygameWindow widget'''
        frame = self.visualSimulation.show()
        for x in range(self.visualSimulation.size[0]):
            for y in range(self.visualSimulation.size[1]):
                self.pygameWindow.setPixel(x, y, frame[x][y])

    def onCompile(self):
        '''when the compile button is pressed, this function is called
        it will convert the code from the codeEdit box into a list of assembly instruction 
        and store it in the codeList variable using simulation.parse'''
        code = self.codeEdit.toPlainText()
        self.simulation = Simulation(code, {}, 0)

        self.codeList = self.simulation.parse()

    def changeRam(self, x, y, value):
        '''this function will update the ram block in the window'''
        self.ramBlock.itemAtPosition(x, y).widget().setText(value)
        # refresh ui
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = Window()
    windowExample.show()
    sys.exit(app.exec_())
