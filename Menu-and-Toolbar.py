import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QMainWindow):

    def __init__(self):
        
        super(App, self).__init__()
        self.title='Histogram Equalization'
        self.label = QLabel(self)
        self.label2 = QLabel(self)
        self.label6 = QLabel(self)
        self.label7 = QLabel(self)
        self.label8 = QLabel(self)
        self.label9 = QLabel(self)
        global hist
        hist=np.zeros([256,1,3],dtype=np.uint32)
        K2=256
        T2=1
        B2=3
        global hist2
        hist2=np.zeros([K2,T2,B2],dtype=np.uint32)
        global imga
        Ai=427
        Bi=277
        Ci=3
        imga=np.zeros([Ai,Bi,Ci],dtype=np.uint8)
        global ter
        ter=np.zeros([1],dtype=np.uint8)
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle(self.title)
        mainMenu = self.menuBar()
        label3 = QLabel('Input', self)
        label3.move(50,75)

        label4 = QLabel('Target', self)
        label4.move(650,75)

        label5 = QLabel('Result', self)
        label5.move(1250,75)
        
        fileMenu = mainMenu.addMenu('File')
        button = QPushButton('Equalize Histogram', self)
        button.setToolTip('This is an example button')
        button.resize(125,30)
        button.move(0,25) 
        button.clicked.connect(self.on_click3)

        newAct = QAction('Open Input', self)
        newAct.triggered.connect(self.on_click)
        fileMenu.addAction(newAct)

        newAct2 = QAction('Open Target', self)
        newAct2.triggered.connect(self.on_click2)
        fileMenu.addAction(newAct2)

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        self.showMaximized()
