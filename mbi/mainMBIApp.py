import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import mbi.MatrixManipulation as MatMan

fontBox = QFont("Times", 12)
fontLabels = QFont("Times", 10)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 650, 640)
        self.setWindowTitle("Matrix Calculations")
        self.xLabels = 50
        self.xBoxes = 180
        self.xSpinBoxes = 250
        self.result = []
        self.UI()

    def UI(self):

        self.panelMatrixDimentions()
        self.panelStatsLabels()

        # ************** Buttons **************
        btnEnter = QPushButton("Enter", self)
        btnEnter.move(self.xSpinBoxes, 520)
        btnEnter.setFont(fontLabels)
        btnEnter.clicked.connect(self.calculate)

        self.show()

    def calculate(self):
        dimA = [self.spinBoxAr.value(), self.spinBoxAc.value()]
        dimB = [self.spinBoxAc.value(), self.spinBoxBc.value()]
        print(f"A: {dimA}, B: {dimB}")

        mm = MatMan.MM()
        mm.setMatrices(dimA, dimB)
        C = mm.quickDotMult()

        for i in range(5):
            temp = "N/A"
            if i == 0:
                self.result.append(C)
                print(f"i: {i} => resulting matrix dot-multiplied: {C}")
            elif i == 1:
                if self.cummProdCheckBox.isChecked():
                    temp = mm.cummulativeProd(C, int(self.minStatSpinBox.value()))
                    self.result.append(temp)
                else:
                    self.result.append(temp)
                print(f"i: {i} => cummProd: {temp}")
            elif i == 2:
                if self.minStatCheckBox.isChecked():
                    temp = mm.statMin(C, int(self.minStatSpinBox.value()))
                    self.result.append(temp)
                else:
                    self.result.append(temp)
                print(f"i: {i} => min: {temp}")
            elif i == 3:
                if self.maxStatCheckBox.isChecked():
                    temp = mm.statMax(C, int(self.maxStatSpinBox.value()))
                    self.result.append(temp)
                else:
                    self.result.append(temp)
                print(f"i: {i} => max: {temp}")
            elif i == 4:
                if self.meanStatCheckBox.isChecked():
                    temp = mm.statMean(C, int(self.meanStatSpinBox.value()))
                    self.result.append(temp)
                else:
                    self.result.append(temp)
                print(f"i: {i} => mean: {temp}")

    def panelMatrixDimentions(self):
        self.matrixLabel = QLabel("Specify the dimentions of matrices A and B to multiply", self)
        self.labelAr = QLabel("Rows of A:", self)
        self.labelAc = QLabel("Cols of A: ", self)
        self.labelBr = QLabel("Rows of B - same as cols of A", self)
        self.labelBc = QLabel("Cols of B: ", self)

        yStart = 100
        step = 35

        self.matrixLabel.move(self.xLabels, yStart - step)
        self.labelAr.move(self.xLabels, yStart)
        self.labelAc.move(self.xLabels, yStart + step)
        self.labelBr.move(self.xLabels, yStart + 2 * step)
        self.labelBc.move(self.xLabels, yStart + 3 * step)

        self.matrixLabel.setFont(fontLabels)
        self.labelAr.setFont(fontLabels)
        self.labelAc.setFont(fontLabels)
        self.labelBr.setFont(fontLabels)
        self.labelBc.setFont(fontLabels)

        # spinBoxesMatrixDimentions(self):

        self.spinBoxAr = QSpinBox(self)
        self.spinBoxAc = QSpinBox(self)
        self.spinBoxBc = QSpinBox(self)

        self.spinBoxAr.move(self.xBoxes, yStart)
        self.spinBoxAc.move(self.xBoxes, yStart + step)
        self.spinBoxBc.move(self.xBoxes, yStart + 3 * step)

        self.spinBoxAr.setRange(1, 10)
        self.spinBoxAc.setRange(1, 10)
        self.spinBoxBc.setRange(1, 10)

        self.spinBoxAr.setFont(fontBox)
        self.spinBoxAc.setFont(fontBox)
        self.spinBoxBc.setFont(fontBox)

    def panelStatsLabels(self):
        self.mainStatLabel = QLabel("Choose stats to calculate: whole matrix: -1; row-wise: 0; col-wise: 1", self)
        self.cummProdLabel = QLabel("Cummulative Product: ", self)
        self.minStatLabel = QLabel("Minimum: ", self)
        self.maxStatLabel = QLabel("Maximum: ", self)
        self.meanStatLabel = QLabel("Mean: ", self)

        self.cummProdCheckBox = QCheckBox(self)
        self.minStatCheckBox = QCheckBox(self)
        self.maxStatCheckBox = QCheckBox(self)
        self.meanStatCheckBox = QCheckBox(self)

        self.minStatSpinBox = QSpinBox(self)
        self.maxStatSpinBox = QSpinBox(self)
        self.meanStatSpinBox = QSpinBox(self)

        yStart = 300
        step = 35

        self.mainStatLabel.move(self.xLabels, yStart)
        self.cummProdLabel.move(self.xLabels, yStart + step)
        self.minStatLabel.move(self.xLabels, yStart + 2 * step)
        self.maxStatLabel.move(self.xLabels, yStart + 3 * step)
        self.meanStatLabel.move(self.xLabels, yStart + 4 * step)

        self.cummProdCheckBox.move(self.xBoxes, yStart + step)
        self.minStatCheckBox.move(self.xBoxes, yStart + 2 * step)
        self.maxStatCheckBox.move(self.xBoxes, yStart + 3 * step)
        self.meanStatCheckBox.move(self.xBoxes, yStart + 4 * step)

        self.minStatSpinBox.move(self.xSpinBoxes, yStart + 2 * step)
        self.maxStatSpinBox.move(self.xSpinBoxes, yStart + 3 * step)
        self.meanStatSpinBox.move(self.xSpinBoxes, yStart + 4 * step)

        self.minStatSpinBox.setRange(-1, 1)
        self.maxStatSpinBox.setRange(-1, 1)
        self.meanStatSpinBox.setRange(-1, 1)

        self.mainStatLabel.setFont(fontLabels)
        self.minStatLabel.setFont(fontLabels)
        self.maxStatLabel.setFont(fontLabels)
        self.meanStatLabel.setFont(fontLabels)

        self.minStatSpinBox.setFont(fontBox)
        self.maxStatSpinBox.setFont(fontBox)
        self.meanStatSpinBox.setFont(fontBox)

    # def calculateMin(self):
    #     self.getMatrices()

    # def panelSaveFile(self):
    #     self.fileName.move(self.xLabels, 220)
    #     self.fileName.setFont(fontLabels)
    #     self.fileName.setPlaceholderText("File name")
    #
    #     self.boxSaveFile.move(self.xBoxes + 50, 220)
    # self.btnSaveFile.clicked.connect(self.getMatrices())

    # self.fileDialog = QFileDialog


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

# if self.boxSaveFile.isChecked():
#     print("boxFileName is checked")
#     if len(self.fileName.text()) > 0:
#         print(f"Saving into file {self.fileName.text()}")
#         self.boxSaveFile.setChecked(False)
#         self.fileName.clear()
#         self.warningNoFileName.close()
#         self.openFile(self)
#     else:
#         print("No file name specified")
#         self.warningNoFileName.move(self.xBoxes + 50 + 70, 220)
#         self.warningNoFileName.setStyleSheet("background-color:red")
# ******* Warnings **************

# self.warningNoFileName.move(1000, 1000)
# self.warningNoFileName.setFont(fontLabels)

# ************** Boxes **********
#       def initUIElements(self):
#         self.fileName = QLineEdit(self)
#         self.boxSaveFile = QCheckBox("Save file?", self)
#         self.warningNoFileName = QLabel("No file name specified!!", self)
