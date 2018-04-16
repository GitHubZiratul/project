import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.QtWidgets import QGridLayout , QLabel, QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication,QSize
from PyQt5 import QtGui
import pygame

class Multi(QMainWindow, QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(400,0,700,1000)
		self.form_1()
		self.setCentralWidget(self.firstWindow)

		self.setWindowTitle('QUEST')
		self.setWindowIcon(QIcon('mxeb2NK.png'))

		self.show()	

	def form_1(self):
		self.firstWindow = QWidget(self)
		self.fon = QPushButton('', self.firstWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))
		
		Quit = QPushButton('', self.firstWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

		self.text1 = QPushButton('', self.firstWindow)
		self.text1.move(100,200) 
		self.text1.setGeometry(80,100,600,110)
		self.text1.setIcon(QIcon('text1.png'))
		self.text1.setFlat(True)
		self.text1.setIconSize(QSize(450,700))

		self.text1_1 = QPushButton('', self.firstWindow)
		self.text1_1.move(100,200) 
		self.text1_1.setGeometry(80,180,600,110)
		self.text1_1.setIcon(QIcon('text1_1.png'))
		self.text1_1.setFlat(True)
		self.text1_1.setIconSize(QSize(450,700))

		self.text1_2 = QPushButton('', self.firstWindow)
		self.text1_2.move(100,200) 
		self.text1_2.setGeometry(80,250,600,110)
		self.text1_2.setIcon(QIcon('text1_2.png'))
		self.text1_2.setFlat(True)
		self.text1_2.setIconSize(QSize(450,700))

		self.osmkar = QPushButton('', self.firstWindow)
		self.osmkar.clicked.connect(self.next)
		self.osmkar.move(100,200) 
		self.osmkar.setGeometry(45,600,300,70)
		self.osmkar.setIcon(QIcon('osmkar.png'))
		self.osmkar.setIconSize(QSize(250,60))
		self.osmkar.setFlat(True)

		self.osmkom = QPushButton('', self.firstWindow)		
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(400,600,300,70)
		self.osmkom.setIcon(QIcon('osmkom.png'))
		self.osmkom.setIconSize(QSize(250,60))
		self.osmkom.setFlat(True)
		self.osmkom.clicked.connect(self.next7)

		self.povolosps = QPushButton('', self.firstWindow)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(250,700,300,70)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(250,60))
		self.povolosps.setFlat(True)
		self.povolosps.clicked.connect(self.next9)

	def form_2(self):
		self.secondWindow = QWidget(self)

		self.fon = QPushButton('', self.secondWindow)
		self.fon.setIcon(QIcon('telefon.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.telefon = QPushButton('', self.secondWindow)
		self.telefon.move(100,200) 
		self.telefon.setGeometry(80,100,600,110)
		self.telefon.setIcon(QIcon('telefon.png'))
		self.telefon.setFlat(True)
		self.telefon.setIconSize(QSize(450,700))

		self.telefon2 = QPushButton('', self.secondWindow)
		self.telefon2.move(100,200) 
		self.telefon2.setGeometry(80,180,600,110)
		self.telefon2.setIcon(QIcon('telefon2.png'))
		self.telefon2.setFlat(True)
		self.telefon2.setIconSize(QSize(450,700))

		self.tel_deistv1 = QPushButton('', self.secondWindow)		
		self.tel_deistv1.move(100,200) 
		self.tel_deistv1.setGeometry(45,600,300,70)
		self.tel_deistv1.setIcon(QIcon('tel_deistv1.png'))
		self.tel_deistv1.setIconSize(QSize(250,60))
		self.tel_deistv1.setFlat(True)
		self.tel_deistv1.clicked.connect(self.next1)
		self.tel_deistv1.clicked.connect(self.ring)
		
		self.tel_deistv2 = QPushButton('', self.secondWindow)		
		self.tel_deistv2.move(100,200) 
		self.tel_deistv2.setGeometry(400,600,300,70)
		self.tel_deistv2.setIcon(QIcon('tel_deistv2.png'))
		self.tel_deistv2.setIconSize(QSize(250,60))
		self.tel_deistv2.setFlat(True)
		self.tel_deistv2.clicked.connect(self.fonarik)
		self.tel_deistv2.clicked.connect(self.next4)

		Quit = QPushButton('', self.secondWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_3(self):
		self.thirdWindow = QWidget(self)
			
		self.fon = QPushButton('', self.thirdWindow)
		self.fon.setIcon(QIcon('telefon.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.zvonok = QPushButton('', self.thirdWindow)
		self.zvonok.move(100,200) 
		self.zvonok.setGeometry(80,180,600,110)
		self.zvonok.setIcon(QIcon('zvonok.png'))
		self.zvonok.setFlat(True)
		self.zvonok.setIconSize(QSize(450,700))

		self.police = QPushButton('', self.thirdWindow)		
		self.police.move(100,200) 
		self.police.setGeometry(45,600,300,70)
		self.police.setIcon(QIcon('police.png'))
		self.police.setIconSize(QSize(250,60))
		self.police.setFlat(True)
		self.police.clicked.connect(self.next3)

		self.roditeli = QPushButton('', self.thirdWindow)		
		self.roditeli.move(100,200) 
		self.roditeli.setGeometry(400,600,300,70)
		self.roditeli.setIcon(QIcon('roditeli.png'))
		self.roditeli.setIconSize(QSize(250,60))
		self.roditeli.setFlat(True)
		self.roditeli.clicked.connect(self.next2)
		self.roditeli.clicked.connect(self.gudok)

		Quit = QPushButton('', self.thirdWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_4(self):
		self.fourthWindow= QWidget(self)
				
		self.fon = QPushButton('', self.fourthWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.niktonepodoshol = QPushButton('', self.fourthWindow)
		self.niktonepodoshol.move(100,200) 
		self.niktonepodoshol.setGeometry(80,180,600,110)
		self.niktonepodoshol.setIcon(QIcon('niktonepodoshol.png'))
		self.niktonepodoshol.setFlat(True)
		self.niktonepodoshol.setIconSize(QSize(450,700))

		self.telefonoff = QPushButton('', self.fourthWindow)
		self.telefonoff.move(100,200) 
		self.telefonoff.setGeometry(80,250,600,110)
		self.telefonoff.setIcon(QIcon('telefonoff.png'))
		self.telefonoff.setFlat(True)
		self.telefonoff.setIconSize(QSize(450,700))

		self.eattel = QPushButton('', self.fourthWindow)		
		self.eattel.move(100,200) 
		self.eattel.setGeometry(180,500,400,90)
		self.eattel.setIcon(QIcon('eattel.png'))
		self.eattel.setIconSize(QSize(250,60))
		self.eattel.setFlat(True)
		self.eattel.clicked.connect(self.next8)

		self.osmkom = QPushButton('', self.fourthWindow)		
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(180,600,400,90)
		self.osmkom.setIcon(QIcon('osmkom.png'))
		self.osmkom.setIconSize(QSize(400,100))
		self.osmkom.setFlat(True)
		self.osmkom.clicked.connect(self.next7)

		self.povolosps = QPushButton('', self.fourthWindow)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(200,700,400,90)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(400,100))
		self.povolosps.setFlat(True)
		self.povolosps.clicked.connect(self.next5)

		Quit = QPushButton('', self.fourthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_5(self):
		self.fifthWindow= QWidget(self)

		self.fon = QPushButton('', self.fifthWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))	

		self.objas = QPushButton('', self.fifthWindow)
		self.objas.move(100,200) 
		self.objas.setGeometry(80,180,600,110)
		self.objas.setIcon(QIcon('objas.png'))
		self.objas.setFlat(True)
		self.objas.setIconSize(QSize(600,700))

		self.telefonoff = QPushButton('', self.fifthWindow)
		self.telefonoff.move(100,200) 
		self.telefonoff.setGeometry(80,250,600,110)
		self.telefonoff.setIcon(QIcon('telefonoff.png'))
		self.telefonoff.setFlat(True)
		self.telefonoff.setIconSize(QSize(450,700))

		self.osmkom = QPushButton('', self.fifthWindow)		
		self.osmkom.move(100,200) 
		self.osmkom.setGeometry(180,600,400,90)
		self.osmkom.setIcon(QIcon('osmkom.png'))
		self.osmkom.setIconSize(QSize(400,100))
		self.osmkom.setFlat(True)
		self.osmkom.clicked.connect(self.next7)

		self.povolosps = QPushButton('', self.fifthWindow)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(200,700,400,90)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(400,100))
		self.povolosps.setFlat(True)
		self.povolosps.clicked.connect(self.next5)

		self.eattel = QPushButton('', self.fifthWindow)		
		self.eattel.move(100,200) 
		self.eattel.setGeometry(180,500,400,90)
		self.eattel.setIcon(QIcon('eattel.png'))
		self.eattel.setIconSize(QSize(250,60))
		self.eattel.setFlat(True)
		self.eattel.clicked.connect(self.next8)

		Quit = QPushButton('', self.fifthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_6(self):
		self.sixthWindow= QWidget(self)

		self.fon = QPushButton('', self.sixthWindow)
		self.fon.setIcon(QIcon('2513350045.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.objas = QPushButton('', self.sixthWindow)
		self.objas.move(100,200) 
		self.objas.setGeometry(80,180,600,110)
		self.objas.setIcon(QIcon('itak.png'))
		self.objas.setFlat(True)
		self.objas.setIconSize(QSize(600,700))

		self.telefonoff = QPushButton('', self.sixthWindow)
		self.telefonoff.move(100,200) 
		self.telefonoff.setGeometry(80,250,600,110)
		self.telefonoff.setIcon(QIcon('dver1.png'))
		self.telefonoff.setFlat(True)
		self.telefonoff.setIconSize(QSize(450,700))

		self.govorsdver = QPushButton('', self.sixthWindow)
		self.govorsdver.move(100,200) 
		self.govorsdver.setGeometry(80,500,600,110)
		self.govorsdver.setIcon(QIcon('govorsdver.png'))
		self.govorsdver.setFlat(True)
		self.govorsdver.setIconSize(QSize(400,500))
		self.govorsdver.clicked.connect(self.next11)

		self.opendoor = QPushButton('', self.sixthWindow)		
		self.opendoor.move(100,200) 
		self.opendoor.setGeometry(180,600,400,90)
		self.opendoor.setIcon(QIcon('opendoor.png'))
		self.opendoor.setIconSize(QSize(400,100))
		self.opendoor.setFlat(True)
		self.opendoor.clicked.connect(self.next13)
		self.opendoor.clicked.connect(self.dver)

		self.povolosps = QPushButton('', self.sixthWindow)
		self.povolosps.move(100,200) 
		self.povolosps.setGeometry(200,700,400,90)
		self.povolosps.setIcon(QIcon('povolosps.png'))
		self.povolosps.setIconSize(QSize(400,100))
		self.povolosps.setFlat(True)
		self.povolosps.clicked.connect(self.next5)

		Quit = QPushButton('', self.sixthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_7(self):
		self.seventhWindow= QWidget(self)	

		self.fon = QPushButton('', self.seventhWindow)
		self.fon.setIcon(QIcon('nakolenyah.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.molba = QPushButton('', self.seventhWindow)
		self.molba.move(100,200) 
		self.molba.setGeometry(80,180,600,110)
		self.molba.setIcon(QIcon('molba.png'))
		self.molba.setFlat(True)
		self.molba.setIconSize(QSize(600,700))

		self.osmkom1 = QPushButton('', self.seventhWindow)		
		self.osmkom1.move(100,200) 
		self.osmkom1.setGeometry(70,600,300,70)
		self.osmkom1.setIcon(QIcon('osmkom1.png'))
		self.osmkom1.setIconSize(QSize(300,70))
		self.osmkom1.setFlat(True)
		self.osmkom1.clicked.connect(self.next7)

		self.molba2 = QPushButton('', self.seventhWindow)
		self.molba2.move(100,200) 
		self.molba2.setGeometry(80,250,600,110)
		self.molba2.setIcon(QIcon('molba2.png'))
		self.molba2.setFlat(True)
		self.molba2.setIconSize(QSize(450,700))	

		self.molba3 = QPushButton('', self.seventhWindow)		
		self.molba3.move(100,200) 
		self.molba3.setGeometry(400,600,300,70)
		self.molba3.setIcon(QIcon('molba3.png'))
		self.molba3.setIconSize(QSize(250,60))
		self.molba3.setFlat(True)
		self.molba3.clicked.connect(self.next6)

		Quit = QPushButton('', self.seventhWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_8(self):
		self.eighthWindow= QWidget(self)	

		self.fon = QPushButton('', self.eighthWindow)
		self.fon.setIcon(QIcon('cwetokakacii.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.text1 = QPushButton('', self.eighthWindow)
		self.text1.move(100,200) 
		self.text1.setGeometry(80,100,600,110)
		self.text1.setIcon(QIcon('molba1_2.png'))
		self.text1.setFlat(True)
		self.text1.setIconSize(QSize(450,700))

		self.text1_1 = QPushButton('', self.eighthWindow)
		self.text1_1.move(100,200) 
		self.text1_1.setGeometry(80,180,600,110)
		self.text1_1.setIcon(QIcon('molba2_2.png'))
		self.text1_1.setFlat(True)
		self.text1_1.setIconSize(QSize(450,700))

		self.text1_2 = QPushButton('', self.eighthWindow)
		self.text1_2.move(100,200) 
		self.text1_2.setGeometry(80,250,600,110)
		self.text1_2.setIcon(QIcon('molba3_2.png'))
		self.text1_2.setFlat(True)
		self.text1_2.setIconSize(QSize(450,700))


		self.restart = QPushButton('', self.eighthWindow)
		self.restart.move(100,200) 
		self.restart.setGeometry(80,500,600,110)
		self.restart.setIcon(QIcon('restart.png'))
		self.restart.setFlat(True)
		self.restart.setIconSize(QSize(450,700))
		self.restart.clicked.connect(self.back)

		Quit = QPushButton('', self.eighthWindow)
		Quit.move(300,775) 
		Quit.setIcon(QIcon('exit.png'))
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(100,200) 
		Quit.setGeometry(80,600,600,110)		
		Quit.setFlat(True)
		Quit.setIconSize(QSize(450,700))

	def form_9(self):
		self.ninthWindow= QWidget(self)

		self.fon = QPushButton('', self.ninthWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(100000,10000000))

		self.osmotr = QPushButton('', self.ninthWindow)
		self.osmotr.move(100,200) 
		self.osmotr.setGeometry(80,180,600,110)
		self.osmotr.setIcon(QIcon('osmotr.png'))
		self.osmotr.setFlat(True)
		self.osmotr.setIconSize(QSize(600,700))

		self.oshup = QPushButton('', self.ninthWindow)
		self.oshup.move(50,200) 
		self.oshup.setGeometry(50,500,600,110)
		self.oshup.setIcon(QIcon('oshup.png'))
		self.oshup.setFlat(True)
		self.oshup.setIconSize(QSize(450,700))
		self.oshup.clicked.connect(self.next10)

		Quit = QPushButton('', self.ninthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_10(self):
		self.tenthWindow= QWidget(self)

		self.fon = QPushButton('', self.tenthWindow)
		self.fon.setIcon(QIcon('cwetokakacii.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.restart = QPushButton('', self.tenthWindow)
		self.restart.move(100,200) 
		self.restart.setGeometry(80,500,600,110)
		self.restart.setIcon(QIcon('restart.png'))
		self.restart.setFlat(True)
		self.restart.setIconSize(QSize(450,700))
		self.restart.clicked.connect(self.back)

		self.death1 = QPushButton('', self.tenthWindow)
		self.death1.move(100,200) 
		self.death1.setGeometry(80,100,600,110)
		self.death1.setIcon(QIcon('death1.png'))
		self.death1.setFlat(True)
		self.death1.setIconSize(QSize(450,700))

		self.death2 = QPushButton('', self.tenthWindow)
		self.death2.move(100,200) 
		self.death2.setGeometry(80,180,600,110)
		self.death2.setIcon(QIcon('death2.png'))
		self.death2.setFlat(True)
		self.death2.setIconSize(QSize(450,700))

		self.death3 = QPushButton('', self.tenthWindow)
		self.death3.move(100,200) 
		self.death3.setGeometry(80,250,600,110)
		self.death3.setIcon(QIcon('death3.png'))
		self.death3.setFlat(True)
		self.death3.setIconSize(QSize(450,700))

		Quit = QPushButton('', self.tenthWindow)
		Quit.move(300,775) 
		Quit.setIcon(QIcon('exit.png'))
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(100,200) 
		Quit.setGeometry(80,600,600,110)		
		Quit.setFlat(True)
		Quit.setIconSize(QSize(450,700))

	def form_11(self):
		self.eleventhWindow= QWidget(self)	

		self.fon = QPushButton('', self.eleventhWindow)
		self.fon.setIcon(QIcon('nakolenyah.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.molba = QPushButton('', self.eleventhWindow)
		self.molba.move(100,200) 
		self.molba.setGeometry(80,180,600,110)
		self.molba.setIcon(QIcon('molba.png'))
		self.molba.setFlat(True)
		self.molba.setIconSize(QSize(600,700))

		self.osmkom1 = QPushButton('', self.eleventhWindow)		
		self.osmkom1.move(100,200) 
		self.osmkom1.setGeometry(70,600,300,70)
		self.osmkom1.setIcon(QIcon('osmkom1.png'))
		self.osmkom1.setIconSize(QSize(300,70))
		self.osmkom1.setFlat(True)
		self.osmkom1.clicked.connect(self.next7)

		self.molba2 = QPushButton('', self.eleventhWindow)
		self.molba2.move(100,200) 
		self.molba2.setGeometry(80,250,600,110)
		self.molba2.setIcon(QIcon('molba2.png'))
		self.molba2.setFlat(True)
		self.molba2.setIconSize(QSize(450,700))	

		self.osmkar = QPushButton('', self.eleventhWindow)
		self.osmkar.clicked.connect(self.next)
		self.osmkar.move(100,200) 
		self.osmkar.setGeometry(200,700,300,70)
		self.osmkar.setIcon(QIcon('osmkar1.png'))
		self.osmkar.setIconSize(QSize(250,60))
		self.osmkar.setFlat(True)

		self.molba3 = QPushButton('', self.eleventhWindow)		
		self.molba3.move(100,200) 
		self.molba3.setGeometry(400,600,300,70)
		self.molba3.setIcon(QIcon('molba3.png'))
		self.molba3.setIconSize(QSize(250,60))
		self.molba3.setFlat(True)
		self.molba3.clicked.connect(self.next6)

		Quit = QPushButton('', self.eleventhWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_12(self):
		self.twelfthWindow= QWidget(self)	

		self.fon = QPushButton('', self.twelfthWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.nashupdver = QPushButton('', self.twelfthWindow)
		self.nashupdver.move(100,200) 
		self.nashupdver.setGeometry(110,180,600,110)
		self.nashupdver.setIcon(QIcon('nashupdver.png'))
		self.nashupdver.setFlat(True)
		self.nashupdver.setIconSize(QSize(600,700))

		self.opendoor = QPushButton('', self.twelfthWindow)
		self.opendoor.move(100,200) 
		self.opendoor.setGeometry(80,400,600,110)
		self.opendoor.setIcon(QIcon('opendoor.png'))
		self.opendoor.setFlat(True)
		self.opendoor.setIconSize(QSize(600,700))
		self.opendoor.clicked.connect(self.next13)
		self.opendoor.clicked.connect(self.dver)

		self.vibit = QPushButton('', self.twelfthWindow)
		self.vibit.move(100,200) 
		self.vibit.setGeometry(80,500,600,110)
		self.vibit.setIcon(QIcon('vibit.png'))
		self.vibit.setFlat(True)
		self.vibit.setIconSize(QSize(600,700))
		self.vibit.clicked.connect(self.next13)

		self.govorsdver = QPushButton('', self.twelfthWindow)
		self.govorsdver.move(100,200) 
		self.govorsdver.setGeometry(80,600,600,110)
		self.govorsdver.setIcon(QIcon('govorsdver.png'))
		self.govorsdver.setFlat(True)
		self.govorsdver.setIconSize(QSize(400,500))
		self.govorsdver.clicked.connect(self.next11)

		Quit = QPushButton('', self.twelfthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_13(self):
		self.thirteenthWindow = QWidget(self)	

		self.fon = QPushButton('', self.thirteenthWindow)
		self.fon.setIcon(QIcon('fon2.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.srsly = QPushButton('', self.thirteenthWindow)
		self.srsly.move(100,200) 
		self.srsly.setGeometry(110,180,600,110)
		self.srsly.setIcon(QIcon('srsly.png'))
		self.srsly.setFlat(True)
		self.srsly.setIconSize(QSize(600,700))

		self.opendoor = QPushButton('', self.thirteenthWindow)
		self.opendoor.move(100,200) 
		self.opendoor.setGeometry(80,400,600,110)
		self.opendoor.setIcon(QIcon('opendoor.png'))
		self.opendoor.setFlat(True)
		self.opendoor.setIconSize(QSize(600,700))
		self.opendoor.clicked.connect(self.next13)
		self.opendoor.clicked.connect(self.dver)

		self.prodolrazg = QPushButton('', self.thirteenthWindow)
		self.prodolrazg.move(100,200) 
		self.prodolrazg.setGeometry(80,600,600,110)
		self.prodolrazg.setIcon(QIcon('prodolrazg.png'))
		self.prodolrazg.setFlat(True)
		self.prodolrazg.setIconSize(QSize(400,500))
		self.prodolrazg.clicked.connect(self.next12)

	def form_14(self):
		self.fourteenthWindow = QWidget(self)	

		self.fon = QPushButton('', self.fourteenthWindow)
		self.fon.setIcon(QIcon('cwetokakacii.jpeg'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.negoditsya = QPushButton('', self.fourteenthWindow)
		self.negoditsya.move(100,200) 
		self.negoditsya.setGeometry(110,180,600,110)
		self.negoditsya.setIcon(QIcon('negoditsya.png'))
		self.negoditsya.setFlat(True)
		self.negoditsya.setIconSize(QSize(600,700))

		self.kisl = QPushButton('', self.fourteenthWindow)
		self.kisl.move(100,200) 
		self.kisl.setGeometry(110,230,600,110)
		self.kisl.setIcon(QIcon('kisl.png'))
		self.kisl.setFlat(True)
		self.kisl.setIconSize(QSize(600,700))

		self.nochance = QPushButton('', self.fourteenthWindow)
		self.nochance.move(100,200) 
		self.nochance.setGeometry(110,280,600,110)
		self.nochance.setIcon(QIcon('nochance.png'))
		self.nochance.setFlat(True)
		self.nochance.setIconSize(QSize(600,700))

		self.noexit = QPushButton('', self.fourteenthWindow)
		self.noexit.move(100,200) 
		self.noexit.setGeometry(110,330,600,110)
		self.noexit.setIcon(QIcon('noexit.png'))
		self.noexit.setFlat(True)
		self.noexit.setIconSize(QSize(600,700))

	def form_15(self):

		self.fifteenthWindow = QWidget(self)	

		self.fon = QPushButton('', self.fifteenthWindow)
		self.fon.setIcon(QIcon('Komn.png'))
		self.fon.setGeometry(0,-100,700,1000)
		self.fon.setIconSize(QSize(700,1000))

		self.voshel = QPushButton('', self.fifteenthWindow)
		self.voshel.move(100,200) 
		self.voshel.setGeometry(110,180,600,110)
		self.voshel.setIcon(QIcon('voshel.png'))
		self.voshel.setFlat(True)
		self.voshel.setIconSize(QSize(600,700))

		self.lyk_dver_stol = QPushButton('', self.fifteenthWindow)
		self.lyk_dver_stol.move(100,200) 
		self.lyk_dver_stol.setGeometry(110,230,600,110)
		self.lyk_dver_stol.setIcon(QIcon('lyk_dver_stol.png'))
		self.lyk_dver_stol.setFlat(True)
		self.lyk_dver_stol.setIconSize(QSize(600,700))

		self.opendoor = QPushButton('', self.fifteenthWindow)
		self.opendoor.move(100,200) 
		self.opendoor.setGeometry(80,400,600,110)
		self.opendoor.setIcon(QIcon('opendoor.png'))
		self.opendoor.setFlat(True)
		self.opendoor.setIconSize(QSize(600,700))
		self.opendoor.clicked.connect(self.next16)
		self.opendoor.clicked.connect(self.dver)

		self.book = QPushButton('', self.fifteenthWindow)
		self.book.move(100,200) 
		self.book.setGeometry(80,500,600,110)
		self.book.setIcon(QIcon('book.png'))
		self.book.setFlat(True)
		self.book.setIconSize(QSize(600,700))
		self.book.clicked.connect(self.next14)

		self.openlyk = QPushButton('', self.fifteenthWindow)
		self.openlyk.move(100,200) 
		self.openlyk.setGeometry(80,600,600,110)
		self.openlyk.setIcon(QIcon('openlyk.png'))
		self.openlyk.setFlat(True)
		self.openlyk.setIconSize(QSize(400,500))

		Quit = QPushButton('', self.fifteenthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))
		
	def form_16(self):
		self.sixteenthWindow = QWidget(self)

		self.ogma = QPushButton('', self.sixteenthWindow)
		self.ogma.setIcon(QIcon('ogma.png'))
		self.ogma.setGeometry(0,-100,700,1000)
		self.ogma.setIconSize(QSize(700,1000))	

		self.castspell = QPushButton('', self.sixteenthWindow)
		self.castspell.move(100,200) 
		self.castspell.setGeometry(80,400,600,110)
		self.castspell.setIcon(QIcon('castspell.png'))
		self.castspell.setFlat(True)
		self.castspell.setIconSize(QSize(600,700))
		self.castspell.clicked.connect(self.next15)
		
		self.shvirnutbook = QPushButton('', self.sixteenthWindow)
		self.shvirnutbook.move(100,200) 
		self.shvirnutbook.setGeometry(80,500,600,110)
		self.shvirnutbook.setIcon(QIcon('shvirnutbook.png.png'))
		self.shvirnutbook.setFlat(True)
		self.shvirnutbook.setIconSize(QSize(600,700))

		Quit = QPushButton('', self.sixteenthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))
		
	def form_17(self):
		self.seventhWindow = QWidget(self)

		self.peri = QPushButton('', self.seventhWindow)
		self.peri.setIcon(QIcon('peri.jpeg'))
		self.peri.setGeometry(0,-100,700,1000)
		self.peri.setIconSize(QSize(700,1000))	

		self.strmesto = QPushButton('', self.seventhWindow)
		self.strmesto.move(100,200) 
		self.strmesto.setGeometry(110,180,600,110)
		self.strmesto.setIcon(QIcon('strmesto.png'))
		self.strmesto.setFlat(True)
		self.strmesto.setIconSize(QSize(600,700))

		self.parti = QPushButton('', self.seventhWindow)
		self.parti.move(100,200) 
		self.parti.setGeometry(110,230,600,110)
		self.parti.setIcon(QIcon('parti.png'))
		self.parti.setFlat(True)
		self.parti.setIconSize(QSize(600,700))

		self.konct = QPushButton('', self.seventhWindow)
		self.konct.move(100,200) 
		self.konct.setGeometry(110,290,600,110)
		self.konct.setIcon(QIcon('konct.png'))
		self.konct.setFlat(True)
		self.konct.setIconSize(QSize(600,700))

		self.parenek1 = QPushButton('', self.seventhWindow)
		self.parenek1.move(100,200) 
		self.parenek1.setGeometry(110,350,600,110)
		self.parenek1.setIcon(QIcon('parenek1.png'))
		self.parenek1.setFlat(True)
		self.parenek1.setIconSize(QSize(600,700))

		self.prepodi = QPushButton('', self.seventhWindow)
		self.prepodi.move(100,200) 
		self.prepodi.setGeometry(110,410,600,110)
		self.prepodi.setIcon(QIcon('prepodi.png'))
		self.prepodi.setFlat(True)
		self.prepodi.setIconSize(QSize(600,700))

		self.parenek2 = QPushButton('', self.seventhWindow)
		self.parenek2.move(100,200) 
		self.parenek2.setGeometry(110,470,600,110)
		self.parenek2.setIcon(QIcon('parenek2.png'))
		self.parenek2.setFlat(True)
		self.parenek2.setIconSize(QSize(600,700))

		self.parenek3 = QPushButton('', self.seventhWindow)
		self.parenek3.move(100,200) 
		self.parenek3.setGeometry(110,530,600,110)
		self.parenek3.setIcon(QIcon('parenek3.png'))
		self.parenek3.setFlat(True)
		self.parenek3.setIconSize(QSize(600,700))

		Quit = QPushButton('', self.seventhWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))
		
	def form_18(self):
		self.eighteenthWindow = QWidget(self)

		self.rusalk = QPushButton('', self.eighteenthWindow)
		self.rusalk.setIcon(QIcon('rusalk.png'))
		self.rusalk.setGeometry(0,-100,700,1000)
		self.rusalk.setIconSize(QSize(700,1000))	

		self.rusalk1 = QPushButton('', self.eighteenthWindow)
		self.rusalk1.move(100,200) 
		self.rusalk1.setGeometry(110,100,600,110)
		self.rusalk1.setIcon(QIcon('rusalk1.png'))
		self.rusalk1.setFlat(True)
		self.rusalk1.setIconSize(QSize(600,700))

		self.pogziv = QPushButton('', self.eighteenthWindow)
		self.pogziv.move(100,200) 
		self.pogziv.setGeometry(110,180,600,110)
		self.pogziv.setIcon(QIcon('pogziv.png'))
		self.pogziv.setFlat(True)
		self.pogziv.setIconSize(QSize(600,700))

		self.prohod1 = QPushButton('', self.eighteenthWindow)
		self.prohod1.move(100,200) 
		self.prohod1.setGeometry(110,260,600,110)
		self.prohod1.setIcon(QIcon('prohod1.png'))
		self.prohod1.setFlat(True)
		self.prohod1.setIconSize(QSize(600,700))

		self.mama1 = QPushButton('', self.eighteenthWindow)
		self.mama1.move(100,200) 
		self.mama1.setGeometry(20,600,700,110)
		self.mama1.setIcon(QIcon('mama1.png'))
		self.mama1.setFlat(True)
		self.mama1.setIconSize(QSize(700,700))

		self.proiti1 = QPushButton('', self.eighteenthWindow)
		self.proiti1.move(100,200) 
		self.proiti1.setGeometry(80,640,600,110)
		self.proiti1.setIcon(QIcon('proiti.png'))
		self.proiti1.setFlat(True)
		self.proiti1.setIconSize(QSize(400,700))
		self.proiti1.clicked.connect(self.next20)

		self.razd = QPushButton('', self.eighteenthWindow)
		self.razd.move(100,200) 
		self.razd.setGeometry(80,700,600,110)
		self.razd.setIcon(QIcon('razd.png'))
		self.razd.setFlat(True)
		self.razd.setIconSize(QSize(600,700))
		self.razd.clicked.connect(self.next17)

		self.sprositvihod = QPushButton('', self.eighteenthWindow)
		self.sprositvihod.move(100,200) 
		self.sprositvihod.setGeometry(80,800,600,110)
		self.sprositvihod.setIcon(QIcon('sprositvihod.png'))
		self.sprositvihod.setFlat(True)
		self.sprositvihod.setIconSize(QSize(600,700))
		self.sprositvihod.clicked.connect(self.next18)

		Quit = QPushButton('', self.eighteenthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_19(self):
		self.nineteenthhWindow = QWidget(self)

		self.rusalk = QPushButton('', self.nineteenthhWindow)
		self.rusalk.setIcon(QIcon('1670.jpeg'))
		self.rusalk.setGeometry(0,-100,700,1000)
		self.rusalk.setIconSize(QSize(700,1000))	

		self.provelivrem = QPushButton('', self.nineteenthhWindow)
		self.provelivrem.move(100,200) 
		self.provelivrem.setGeometry(110,100,600,110)
		self.provelivrem.setIcon(QIcon('provelivrem.png'))
		self.provelivrem.setFlat(True)
		self.provelivrem.setIconSize(QSize(600,700))

		self.sjeli = QPushButton('', self.nineteenthhWindow)
		self.sjeli.move(100,200) 
		self.sjeli.setGeometry(110,180,600,110)
		self.sjeli.setIcon(QIcon('sjeli.png'))
		self.sjeli.setFlat(True)
		self.sjeli.setIconSize(QSize(600,700))

		Quit = QPushButton('', self.nineteenthhWindow)
		Quit.move(300,775) 
		Quit.setIcon(QIcon('exit.png'))
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(100,200) 
		Quit.setGeometry(80,600,600,110)		
		Quit.setFlat(True)
		Quit.setIconSize(QSize(450,700))

		self.restart = QPushButton('', self.nineteenthhWindow)
		self.restart.move(100,200) 
		self.restart.setGeometry(80,500,600,110)
		self.restart.setIcon(QIcon('restart.png'))
		self.restart.setFlat(True)
		self.restart.setIconSize(QSize(450,700))
		self.restart.clicked.connect(self.back)

	def form_20(self):
		self.twentiethWindow = QWidget(self)

		self.rusalk = QPushButton('', self.twentiethWindow)
		self.rusalk.setIcon(QIcon('rusalk.png'))
		self.rusalk.setGeometry(0,-100,700,1000)
		self.rusalk.setIconSize(QSize(700,1000))

		self.uhod = QPushButton('', self.twentiethWindow)
		self.uhod.move(100,200) 
		self.uhod.setGeometry(110,100,600,110)
		self.uhod.setIcon(QIcon('uhod.png'))
		self.uhod.setFlat(True)
		self.uhod.setIconSize(QSize(600,700))

		self.glos = QPushButton('', self.twentiethWindow)
		self.glos.move(100,200) 
		self.glos.setGeometry(110,180,600,110)
		self.glos.setIcon(QIcon('glos.png'))
		self.glos.setFlat(True)
		self.glos.setIconSize(QSize(600,700))

		self.sorre = QPushButton('', self.twentiethWindow)
		self.sorre.move(100,200) 
		self.sorre.setGeometry(80,500,600,110)
		self.sorre.setIcon(QIcon('sorre.png'))
		self.sorre.setFlat(True)
		self.sorre.setIconSize(QSize(600,500))
		self.sorre.clicked.connect(self.next19)
		
		self.podvoh1 = QPushButton('', self.twentiethWindow)		
		self.podvoh1.move(100,200) 
		self.podvoh1.setGeometry(180,600,400,90)
		self.podvoh1.setIcon(QIcon('podvoh1.png'))
		self.podvoh1.setIconSize(QSize(600,100))
		self.podvoh1.setFlat(True)
		self.podvoh1.clicked.connect(self.next17)

		Quit = QPushButton('', self.twentiethWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))
		
	def form_21(self):
		self.twenty_firstWindow = QWidget(self)

		self.rusalk = QPushButton('', self.twenty_firstWindow)
		self.rusalk.setIcon(QIcon('rusalk.png'))
		self.rusalk.setGeometry(0,-100,700,1000)
		self.rusalk.setIconSize(QSize(700,1000))

		self.rasist = QPushButton('', self.twenty_firstWindow)
		self.rasist.move(100,200) 
		self.rasist.setGeometry(110,100,600,110)
		self.rasist.setIcon(QIcon('rasist.png'))
		self.rasist.setFlat(True)
		self.rasist.setIconSize(QSize(600,700))

		self.rasist1 = QPushButton('', self.twenty_firstWindow)
		self.rasist1.move(100,200) 
		self.rasist1.setGeometry(80,600,600,110)
		self.rasist1.setIcon(QIcon('rasist1.png'))
		self.rasist1.setFlat(True)
		self.rasist1.setIconSize(QSize(600,700))

		self.rasist2 = QPushButton('', self.twenty_firstWindow)
		self.rasist2.move(100,200) 
		self.rasist2.setGeometry(80,640,600,110)
		self.rasist2.setIcon(QIcon('rasist2.png'))
		self.rasist2.setFlat(True)
		self.rasist2.setIconSize(QSize(400,700))
			
		self.srydami = QPushButton('', self.twenty_firstWindow)
		self.srydami.move(100,200) 
		self.srydami.setGeometry(80,700,600,110)
		self.srydami.setIcon(QIcon('srydami.png'))
		self.srydami.setFlat(True)
		self.srydami.setIconSize(QSize(600,700))
		self.srydami.clicked.connect(self.next20)

		self.godbyeloxi = QPushButton('', self.twenty_firstWindow)
		self.godbyeloxi.move(100,200) 
		self.godbyeloxi.setGeometry(80,800,600,110)
		self.godbyeloxi.setIcon(QIcon('godbyeloxi.png'))
		self.godbyeloxi.setFlat(True)
		self.godbyeloxi.setIconSize(QSize(600,700))
		self.godbyeloxi.clicked.connect(self.next20)

		Quit = QPushButton('', self.twenty_firstWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_22(self):
		self.twenty_secondWindow = QWidget(self)
		
		self.whiteroom = QPushButton('', self.twenty_secondWindow)
		self.whiteroom.setIcon(QIcon('whiteroom.png'))
		self.whiteroom.setGeometry(0,-100,700,1000)
		self.whiteroom.setIconSize(QSize(700,1000))

		self.peshera = QPushButton('', self.twenty_secondWindow)
		self.peshera.move(100,200) 
		self.peshera.setGeometry(80,100,600,110)
		self.peshera.setIcon(QIcon('peshera.png'))
		self.peshera.setFlat(True)
		self.peshera.setIconSize(QSize(450,700))

		self.konm2 = QPushButton('', self.twenty_secondWindow)
		self.konm2.move(100,200) 
		self.konm2.setGeometry(80,180,600,110)
		self.konm2.setIcon(QIcon('konm2.png'))
		self.konm2.setFlat(True)
		self.konm2.setIconSize(QSize(450,700))

		self.nedel = QPushButton('', self.twenty_secondWindow)		
		self.nedel.move(100,200) 
		self.nedel.setGeometry(45,600,300,70)
		self.nedel.setIcon(QIcon('nedel.png'))
		self.nedel.setIconSize(QSize(450,700))
		self.nedel.setFlat(True)
		self.nedel.clicked.connect(self.next21)

		self.apatia = QPushButton('', self.twenty_secondWindow)		
		self.apatia.move(100,200) 
		self.apatia.setGeometry(400,600,300,70)
		self.apatia.setIcon(QIcon('apatia.png'))
		self.apatia.setIconSize(QSize(300,70))
		self.apatia.setFlat(True)
		self.apatia.clicked.connect(self.next21)

		self.sdelat = QPushButton('', self.twenty_secondWindow)
		self.sdelat.move(100,200) 
		self.sdelat.setGeometry(250,700,300,70)
		self.sdelat.setIcon(QIcon('sdelat.png'))
		self.sdelat.setIconSize(QSize(250,60))
		self.sdelat.setFlat(True)
		self.sdelat.clicked.connect(self.next22)

		Quit = QPushButton('', self.twenty_secondWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))
		
	def form_23(self):
		self.twenty_thirdWindow = QWidget(self)

		self.whiteroom = QPushButton('', self.twenty_thirdWindow)
		self.whiteroom.setIcon(QIcon('whiteroom.png'))
		self.whiteroom.setGeometry(0,-100,700,1000)
		self.whiteroom.setIconSize(QSize(700,1000))

		self.gameover = QPushButton('', self.twenty_thirdWindow)
		self.gameover.move(100,200) 
		self.gameover.setGeometry(80,100,600,110)
		self.gameover.setIcon(QIcon('gameover.png'))
		self.gameover.setFlat(True)
		self.gameover.setIconSize(QSize(450,700))

		Quit = QPushButton('', self.twenty_thirdWindow)
		Quit.move(300,775) 
		Quit.setIcon(QIcon('exit.png'))
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(100,200) 
		Quit.setGeometry(80,600,600,110)		
		Quit.setFlat(True)
		Quit.setIconSize(QSize(450,700))

		self.restart = QPushButton('', self.twenty_thirdWindow)
		self.restart.move(100,200) 
		self.restart.setGeometry(80,500,600,110)
		self.restart.setIcon(QIcon('restart.png'))
		self.restart.setFlat(True)
		self.restart.setIconSize(QSize(450,700))
		self.restart.clicked.connect(self.back)

	def form_24(self):
		self.twenty_fourthWindow = QWidget(self)

		self.whiteroom = QPushButton('', self.twenty_fourthWindow)
		self.whiteroom.setIcon(QIcon('whiteroom.png'))
		self.whiteroom.setGeometry(0,-100,700,1000)
		self.whiteroom.setIconSize(QSize(700,1000))

		self.gim = QPushButton('', self.twenty_fourthWindow)
		self.gim.move(100,200) 
		self.gim.setGeometry(80,100,600,110)
		self.gim.setIcon(QIcon('gim.png'))
		self.gim.setFlat(True)
		self.gim.setIconSize(QSize(450,700))

		self.prohod = QPushButton('', self.twenty_fourthWindow)
		self.prohod.move(100,200) 
		self.prohod.setGeometry(80,180,600,110)
		self.prohod.setIcon(QIcon('prohod.png'))
		self.prohod.setFlat(True)
		self.prohod.setIconSize(QSize(450,700))

		self.idti1 = QPushButton('', self.twenty_fourthWindow)		
		self.idti1.move(100,200) 
		self.idti1.setGeometry(45,600,300,70)
		self.idti1.setIcon(QIcon('idti1.png'))
		self.idti1.setIconSize(QSize(250,60))
		self.idti1.setFlat(True)
		self.idti1.clicked.connect(self.next23)

		self.idti2 = QPushButton('', self.twenty_fourthWindow)		
		self.idti2.move(100,200) 
		self.idti2.setGeometry(400,600,300,70)
		self.idti2.setIcon(QIcon('idti2.png'))
		self.idti2.setIconSize(QSize(250,60))
		self.idti2.setFlat(True)
		self.idti2.clicked.connect(self.next23)
		
		self.idti3 = QPushButton('', self.twenty_fourthWindow)
		self.idti3.move(100,200) 
		self.idti3.setGeometry(250,700,300,70)
		self.idti3.setIcon(QIcon('idti3.png'))
		self.idti3.setIconSize(QSize(250,60))
		self.idti3.setFlat(True)
		self.idti3.clicked.connect(self.next23)

		Quit = QPushButton('', self.twenty_fourthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_25(self):
		self.twenty_fifthWindow = QWidget(self)

		self.whiteroom = QPushButton('', self.twenty_fifthWindow)
		self.whiteroom.setIcon(QIcon('whiteroom.png'))
		self.whiteroom.setGeometry(0,-100,700,1000)
		self.whiteroom.setIconSize(QSize(700,1000))

		self.nelep = QPushButton('', self.twenty_fifthWindow)
		self.nelep.move(100,200) 
		self.nelep.setGeometry(80,100,600,110)
		self.nelep.setIcon(QIcon('nelep.png'))
		self.nelep.setFlat(True)
		self.nelep.setIconSize(QSize(450,700))

		self.ewe1 = QPushButton('', self.twenty_fifthWindow)
		self.ewe1.move(100,200) 
		self.ewe1.setGeometry(80,180,600,110)
		self.ewe1.setIcon(QIcon('ewe1.png'))
		self.ewe1.setFlat(True)
		self.ewe1.setIconSize(QSize(450,700))

		self.deistw1 = QPushButton('', self.twenty_fifthWindow)		
		self.deistw1.move(100,200) 
		self.deistw1.setGeometry(45,600,300,70)
		self.deistw1.setIcon(QIcon('deistw1.png'))
		self.deistw1.setIconSize(QSize(250,60))
		self.deistw1.setFlat(True)
		self.deistw1.clicked.connect(self.next24)

		self.deistw2 = QPushButton('', self.twenty_fifthWindow)		
		self.deistw2.move(100,200) 
		self.deistw2.setGeometry(400,600,300,70)
		self.deistw2.setIcon(QIcon('deistw2.png'))
		self.deistw2.setIconSize(QSize(250,60))
		self.deistw2.setFlat(True)
		self.deistw2.clicked.connect(self.next25)
		
		self.deistw3 = QPushButton('', self.twenty_fifthWindow)
		self.deistw3.move(100,200) 
		self.deistw3.setGeometry(250,700,300,70)
		self.deistw3.setIcon(QIcon('deistw3.png'))
		self.deistw3.setIconSize(QSize(250,60))
		self.deistw3.setFlat(True)
		self.deistw3.clicked.connect(self.next24)

		Quit = QPushButton('', self.twenty_fifthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))


	def form_26(self):
		self.twenty_sixthWindow = QWidget(self)

		self.nope = QPushButton('', self.twenty_sixthWindow)
		self.nope.setIcon(QIcon('nope.png'))
		self.nope.setGeometry(0,-100,700,1000)
		self.nope.setIconSize(QSize(700,1000))

		self.jopa = QPushButton('', self.twenty_sixthWindow)
		self.jopa.move(100,200) 
		self.jopa.setGeometry(80,100,800,200)
		self.jopa.setIcon(QIcon('jopa.png'))
		self.jopa.setFlat(True)
		self.jopa.setIconSize(QSize(800,700))

		self.no1 = QPushButton('', self.twenty_sixthWindow)		
		self.no1.move(100,200) 
		self.no1.setGeometry(45,600,300,70)
		self.no1.setIcon(QIcon('no1.png'))
		self.no1.setIconSize(QSize(250,60))
		self.no1.setFlat(True)
		self.no1.clicked.connect(self.back)		

		self.no2 = QPushButton('', self.twenty_sixthWindow)		
		self.no2.move(100,200) 
		self.no2.setGeometry(400,600,300,70)
		self.no2.setIcon(QIcon('no2.png'))
		self.no2.setIconSize(QSize(250,60))
		self.no2.setFlat(True)
		self.no2.clicked.connect(self.back)

		self.no3 = QPushButton('', self.twenty_sixthWindow)
		self.no3.move(100,200) 
		self.no3.setGeometry(250,700,300,70)
		self.no3.setIcon(QIcon('no3.png'))
		self.no3.setIconSize(QSize(250,60))
		self.no3.setFlat(True)
		self.no3.clicked.connect(self.back)

		Quit = QPushButton('', self.twenty_sixthWindow)
		Quit.move(300,775) 
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(0,0) 
		Quit.setGeometry(650,0,50,50)
		Quit.setIcon(QIcon('power1.png'))
		Quit.setFlat(True)
		Quit.setIconSize(QSize(50,50))

	def form_27(self):
		self.twenty_seventhWindow = QWidget(self)

		self.nope = QPushButton('', self.twenty_seventhWindow)
		self.nope.setIcon(QIcon('466235-victory.jpeg'))
		self.nope.setGeometry(0,-100,700,1000)
		self.nope.setIconSize(QSize(700,1000))

		self.molodec = QPushButton('', self.twenty_seventhWindow)
		self.molodec.move(100,200) 
		self.molodec.setGeometry(40,100,600,200)
		self.molodec.setIcon(QIcon('molodec.png'))
		self.molodec.setFlat(True)
		self.molodec.setIconSize(QSize(600,700))

		self.restart = QPushButton('', self.twenty_seventhWindow)
		self.restart.move(100,200) 
		self.restart.setGeometry(80,500,600,110)
		self.restart.setIcon(QIcon('restart.png'))
		self.restart.setFlat(True)
		self.restart.setIconSize(QSize(450,700))
		self.restart.clicked.connect(self.back)

		Quit = QPushButton('', self.twenty_seventhWindow)
		Quit.move(300,775) 
		Quit.setIcon(QIcon('exit.png'))
		Quit.clicked.connect(QCoreApplication.instance().quit)
		Quit.resize(Quit.sizeHint())
		Quit.move(100,200) 
		Quit.setGeometry(80,600,600,110)		
		Quit.setFlat(True)
		Quit.setIconSize(QSize(450,700))

	def back(self):
		self.form_1()
		self.setCentralWidget(self.firstWindow)

	def next(self):
		self.form_2()
		self.setCentralWidget(self.secondWindow)

	def next1(self):
		self.form_3()
		self.setCentralWidget(self.thirdWindow)

	def next2(self):
		self.form_4()
		self.setCentralWidget(self.fourthWindow)

	def next3(self):
		self.form_5()
		self.setCentralWidget(self.fifthWindow)

	def next4(self):
		self.form_6()
		self.setCentralWidget(self.sixthWindow)

	def next5(self):
		self.form_7()
		self.setCentralWidget(self.seventhWindow)

	def next6(self):
		self.form_8()
		self.setCentralWidget(self.eighthWindow)

	def next7(self):
		self.form_9()
		self.setCentralWidget(self.ninthWindow)

	def next8(self):
		self.form_10()
		self.setCentralWidget(self.tenthWindow)

	def next9(self):
		self.form_11()
		self.setCentralWidget(self.eleventhWindow)

	def next10(self):
		self.form_12()
		self.setCentralWidget(self.twelfthWindow)

	def next11(self):
		self.form_13()
		self.setCentralWidget(self.thirteenthWindow)

	def next12(self):
		self.form_14()
		self.setCentralWidget(self.fourteenthWindow)

	def next13(self):
		self.form_15()
		self.setCentralWidget(self.fifteenthWindow)

	def next14(self):
		self.form_16()
		self.setCentralWidget(self.sixteenthWindow)

	def next15(self):
		self.form_17()
		self.setCentralWidget(self.seventhWindow)

	def next16(self):
		self.form_18()
		self.setCentralWidget(self.eighteenthWindow)

	def next17(self):
		self.form_19()
		self.setCentralWidget(self.nineteenthhWindow)

	def next18(self):
		self.form_20()
		self.setCentralWidget(self.twentiethWindow)

	def next19(self):
		self.form_21()
		self.setCentralWidget(self.twenty_firstWindow)

	def next20(self):
		self.form_22()
		self.setCentralWidget(self.twenty_secondWindow)

	def next21(self):
		self.form_23()
		self.setCentralWidget(self.twenty_thirdWindow)

	def next22(self):
		self.form_24()
		self.setCentralWidget(self.twenty_fourthWindow)	

	def next23(self):
		self.form_25()
		self.setCentralWidget(self.twenty_fifthWindow)

	def next24(self):
		self.form_26()
		self.setCentralWidget(self.twenty_sixthWindow)

	def next25(self):
		self.form_27()
		self.setCentralWidget(self.twenty_seventhWindow)
		
	def dver(self):
		pygame.init()
		pygame.mixer.music.load('skrip-dveri-dver-zahlopyvaetsya.mp3')
		pygame.mixer.music.play()	

	def ring(self):
		pygame.init()
		pygame.mixer.music.load('Zvuk-nabor_nomera_telef.mp3')
		pygame.mixer.music.play()	

	def gudok(self):
		pygame.init()
		pygame.mixer.music.load('04337.mp3')
		pygame.mixer.music.play()

	def fonarik(self):
		pygame.init()
		pygame.mixer.music.load('Fonarik.mp3')
		pygame.mixer.music.play()		

	def closeEvent(self, event):

		reply = QMessageBox.question(self, 'Подтверждение',
			"Вы действительно хотите выйти ?", QMessageBox.Yes |
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
		
app = QApplication(sys.argv)
my_window = Multi()
sys.exit(app.exec_())
ex = Multi()



