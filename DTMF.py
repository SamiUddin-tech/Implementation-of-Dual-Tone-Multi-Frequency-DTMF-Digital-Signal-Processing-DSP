# importing libraries
import sounddevice as sd
import pyqtgraph as pg
from math import pi
from PyQt5.uic import loadUi
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# Sampling Frequency
Fs = 2000;
# Sampling Time
Ts = 1/Fs
# Time axis
t = np.arange(-0.2, 0.2, Ts)
# Dual Tone Multi Frequencies
f1 = 1209
f2 = 1336
f3 = 1444
f4 = 697
f5 = 770
f6 = 852
f7 = 941

Time_plot = pg.GraphicsLayoutWidget()
Freq_plot = pg.GraphicsLayoutWidget()

class DTMF(QMainWindow):
    def __init__(self):
        super(DTMF, self).__init__()
        loadUi('DSP Project - DTMF.ui', self)
        self.setFixedSize(761, 442)
        self.gridLayout.addWidget(Time_plot)
        self.gridLayout_2.addWidget(Freq_plot)
        self.Time = Time_plot.addPlot(title="Signal - Time Domain")
        self.Time.showGrid(x=True, y=True, alpha=1)
        self.Frequency = Freq_plot.addPlot(title="Signal - Frequency Domain")
        self.Frequency.showGrid(x=True, y=True, alpha=1)
        self.Time_Curve = self.Time.plot(pen='y')
        self.Freq_Curve = self.Frequency.plot(pen='y')
        self.Freq_Curve.setFftMode(True)

        self.pushButton.clicked.connect(self.Dial_1)
        self.pushButton_5.clicked.connect(self.Dial_2)
        self.pushButton_7.clicked.connect(self.Dial_3)
        self.pushButton_8.clicked.connect(self.Dial_4)
        self.pushButton_4.clicked.connect(self.Dial_5)
        self.pushButton_6.clicked.connect(self.Dial_6)
        self.pushButton_2.clicked.connect(self.Dial_7)
        self.pushButton_3.clicked.connect(self.Dial_8)
        self.pushButton_10.clicked.connect(self.Dial_9)
        self.pushButton_9.clicked.connect(self.Star)
        self.pushButton_11.clicked.connect(self.Zero)
        self.pushButton_12.clicked.connect(self.Hash)

    def Dial_1(self):
        signal = np.sin(2 * pi * f1 * t)
        signal1 = np.sin(2 * pi * f4 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Freq_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f1) + " and " + str(f4) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_2(self):
        signal = np.sin(2 * pi * f2 * t)
        signal1 = np.sin(2 * pi * f4 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f2) + " and " + str(f4) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_3(self):
        signal = np.sin(2 * pi * f3 * t)
        signal1 = np.sin(2 * pi * f4 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f3) + " and " + str(f4) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_4(self):
        signal = np.sin(2 * pi * f1 * t)
        signal1 = np.sin(2 * pi * f5 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f1) + " and " + str(f5) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_5(self):
        signal = np.sin(2 * pi * f2 * t)
        signal1 = np.sin(2 * pi * f5 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f2) + " and " + str(f5) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_6(self):
        signal = np.sin(2 * pi * f3 * t)
        signal1 = np.sin(2 * pi * f5 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f3) + " and " + str(f5) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_7(self):
        signal = np.sin(2 * pi * f1 * t)
        signal1 = np.sin(2 * pi * f6 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f1) + " and " + str(f6) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_8(self):
        signal = np.sin(2 * pi * f2 * t)
        signal1 = np.sin(2 * pi * f6 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f2) + " and " + str(f6) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Dial_9(self):
        signal = np.sin(2 * pi * f3 * t)
        signal1 = np.sin(2 * pi * f6 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f3) + " and " + str(f6) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Star(self):
        signal = np.sin(2 * pi * f1 * t)
        signal1 = np.sin(2 * pi * f7 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f1) + " and " + str(f7) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Zero(self):
        signal = np.sin(2 * pi * f2 * t)
        signal1 = np.sin(2 * pi * f7 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f2) + " and " + str(f7) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

    def Hash(self):
        signal = np.sin(2 * pi * f3 * t)
        signal1 = np.sin(2 * pi * f7 * t)
        signalx = signal + signal1
        self.Time_Curve.clear()
        self.Time_Curve.setData(signalx)
        self.Freq_Curve.setData(signalx)
        sd.play(signalx, Fs)
        S = "The Combination of Frequencies " + str(f3) + " and " + str(f7) + " is Pressed"
        QMessageBox.about(self, "Dual Tone", S)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DTMF()
    window.setWindowTitle('DSP Project - DTMF')
    window.show()
    sys.exit(app.exec_())