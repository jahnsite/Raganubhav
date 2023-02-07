import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import multiprocessing
import json
import time
import sounddevice
import music21
import numpy as np
import pyaudio

index_to_note_table={
    -1:'-',
    1:'C4',
    2:'C#4',
    3:'D4',
    4:'D#4',
    5:'E4',
    6:'F4',
    7:'F#4',
    8:'G4',
    9:'G#4',
    10:'A4',
    11:'A#4',
    12:'B4'
}

class DataPacket:
    def __init__(self):
        self.data={
            "tempo": 100,
            "duration":0.1,
            1: '-',
            2: '-',
            3: '-',
            4: '-',
            5: '-',
            6: '-',
            7: '-',
            8: '-',
            }


class Ui_MainWindow(object):
    def __init__(self):
        self.data_packet = DataPacket()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.beat_list_1 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_1.setGeometry(QtCore.QRect(20, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_1.setFont(font)
        self.beat_list_1.setStyleSheet("")
        self.beat_list_1.setObjectName("beat_list_1")
        self.beat_list_1.addItem("-", -1)
        self.beat_list_1.addItem("Sa", 1)
        self.beat_list_1.addItem("Komal Re", 2)
        self.beat_list_1.addItem("Re", 3)
        self.beat_list_1.addItem("Komal Ga", 4)
        self.beat_list_1.addItem("Ga", 5)
        self.beat_list_1.addItem("Ma", 6)
        self.beat_list_1.addItem("Teevra Ma", 7)
        self.beat_list_1.addItem("Pa", 8)
        self.beat_list_1.addItem("Komal Dha", 9)
        self.beat_list_1.addItem("Dha", 10)
        self.beat_list_1.addItem("Komal Ni", 11)
        self.beat_list_1.addItem("Ni", 12)
        self.beat_list_1.addItem("Sa^", 13)
        self.beat_list_1.activated.connect(self.updateNoteList)

        self.beat_list_2 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_2.setGeometry(QtCore.QRect(160, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_2.setFont(font)
        self.beat_list_2.setStyleSheet("")
        self.beat_list_2.setObjectName("beat_list_2")
        self.beat_list_2.addItem("-", -1)
        self.beat_list_2.addItem("Sa", 1)
        self.beat_list_2.addItem("Komal Re", 2)
        self.beat_list_2.addItem("Re", 3)
        self.beat_list_2.addItem("Komal Ga", 4)
        self.beat_list_2.addItem("Ga", 5)
        self.beat_list_2.addItem("Ma", 6)
        self.beat_list_2.addItem("Teevra Ma", 7)
        self.beat_list_2.addItem("Pa", 8)
        self.beat_list_2.addItem("Komal Dha", 9)
        self.beat_list_2.addItem("Dha", 10)
        self.beat_list_2.addItem("Komal Ni", 11)
        self.beat_list_2.addItem("Ni", 12)
        self.beat_list_2.addItem("Sa^", 13)
        self.beat_list_2.activated.connect(self.updateNoteList)
        
        self.beat_list_3 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_3.setGeometry(QtCore.QRect(300, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_3.setFont(font)
        self.beat_list_3.setStyleSheet("")
        self.beat_list_3.setObjectName("beat_list_3")
        self.beat_list_3.addItem("-", -1)
        self.beat_list_3.addItem("Sa", 1)
        self.beat_list_3.addItem("Komal Re", 2)
        self.beat_list_3.addItem("Re", 3)
        self.beat_list_3.addItem("Komal Ga", 4)
        self.beat_list_3.addItem("Ga", 5)
        self.beat_list_3.addItem("Ma", 6)
        self.beat_list_3.addItem("Teevra Ma", 7)
        self.beat_list_3.addItem("Pa", 8)
        self.beat_list_3.addItem("Komal Dha", 9)
        self.beat_list_3.addItem("Dha", 10)
        self.beat_list_3.addItem("Komal Ni", 11)
        self.beat_list_3.addItem("Ni", 12)
        self.beat_list_3.addItem("Sa^", 13)
        self.beat_list_3.activated.connect(self.updateNoteList)
        
        self.beat_list_4 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_4.setGeometry(QtCore.QRect(430, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_4.setFont(font)
        self.beat_list_4.setStyleSheet("")
        self.beat_list_4.setObjectName("beat_list_4")
        self.beat_list_4.addItem("-", -1)
        self.beat_list_4.addItem("Sa", 1)
        self.beat_list_4.addItem("Komal Re", 2)
        self.beat_list_4.addItem("Re", 3)
        self.beat_list_4.addItem("Komal Ga", 4)
        self.beat_list_4.addItem("Ga", 5)
        self.beat_list_4.addItem("Ma", 6)
        self.beat_list_4.addItem("Teevra Ma", 7)
        self.beat_list_4.addItem("Pa", 8)
        self.beat_list_4.addItem("Komal Dha", 9)
        self.beat_list_4.addItem("Dha", 10)
        self.beat_list_4.addItem("Komal Ni", 11)
        self.beat_list_4.addItem("Ni", 12)
        self.beat_list_4.addItem("Sa^", 13)
        self.beat_list_4.activated.connect(self.updateNoteList)
        
        self.beat_list_5 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_5.setGeometry(QtCore.QRect(570, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_5.setFont(font)
        self.beat_list_5.setStyleSheet("")
        self.beat_list_5.setObjectName("beat_list_5")
        self.beat_list_5.addItem("-", -1)
        self.beat_list_5.addItem("Sa", 1)
        self.beat_list_5.addItem("Komal Re", 2)
        self.beat_list_5.addItem("Re", 3)
        self.beat_list_5.addItem("Komal Ga", 4)
        self.beat_list_5.addItem("Ga", 5)
        self.beat_list_5.addItem("Ma", 6)
        self.beat_list_5.addItem("Teevra Ma", 7)
        self.beat_list_5.addItem("Pa", 8)
        self.beat_list_5.addItem("Komal Dha", 9)
        self.beat_list_5.addItem("Dha", 10)
        self.beat_list_5.addItem("Komal Ni", 11)
        self.beat_list_5.addItem("Ni", 12)
        self.beat_list_5.addItem("Sa^", 13)
        self.beat_list_5.activated.connect(self.updateNoteList)
        
        self.beat_list_6 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_6.setGeometry(QtCore.QRect(680, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_6.setFont(font)
        self.beat_list_6.setStyleSheet("")
        self.beat_list_6.setObjectName("beat_list_6")
        self.beat_list_6.addItem("-", -1)
        self.beat_list_6.addItem("Sa", 1)
        self.beat_list_6.addItem("Komal Re", 2)
        self.beat_list_6.addItem("Re", 3)
        self.beat_list_6.addItem("Komal Ga", 4)
        self.beat_list_6.addItem("Ga", 5)
        self.beat_list_6.addItem("Ma", 6)
        self.beat_list_6.addItem("Teevra Ma", 7)
        self.beat_list_6.addItem("Pa", 8)
        self.beat_list_6.addItem("Komal Dha", 9)
        self.beat_list_6.addItem("Dha", 10)
        self.beat_list_6.addItem("Komal Ni", 11)
        self.beat_list_6.addItem("Ni", 12)
        self.beat_list_6.addItem("Sa^", 13)
        self.beat_list_6.activated.connect(self.updateNoteList)
        
        self.beat_list_7 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_7.setGeometry(QtCore.QRect(800, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_7.setFont(font)
        self.beat_list_7.setStyleSheet("")
        self.beat_list_7.setObjectName("beat_list_7")
        self.beat_list_7.addItem("-", -1)
        self.beat_list_7.addItem("Sa", 1)
        self.beat_list_7.addItem("Komal Re", 2)
        self.beat_list_7.addItem("Re", 3)
        self.beat_list_7.addItem("Komal Ga", 4)
        self.beat_list_7.addItem("Ga", 5)
        self.beat_list_7.addItem("Ma", 6)
        self.beat_list_7.addItem("Teevra Ma", 7)
        self.beat_list_7.addItem("Pa", 8)
        self.beat_list_7.addItem("Komal Dha", 9)
        self.beat_list_7.addItem("Dha", 10)
        self.beat_list_7.addItem("Komal Ni", 11)
        self.beat_list_7.addItem("Ni", 12)
        self.beat_list_7.addItem("Sa^", 13)
        self.beat_list_7.activated.connect(self.updateNoteList)
        
        self.beat_list_8 = QtWidgets.QComboBox(self.centralwidget)
        self.beat_list_8.setGeometry(QtCore.QRect(920, 330, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beat_list_8.setFont(font)
        self.beat_list_8.setStyleSheet("")
        self.beat_list_8.setObjectName("beat_list_8")
        self.beat_list_8.addItem("-", -1)
        self.beat_list_8.addItem("Sa", 1)
        self.beat_list_8.addItem("Komal Re", 2)
        self.beat_list_8.addItem("Re", 3)
        self.beat_list_8.addItem("Komal Ga", 4)
        self.beat_list_8.addItem("Ga", 5)
        self.beat_list_8.addItem("Ma", 6)
        self.beat_list_8.addItem("Teevra Ma", 7)
        self.beat_list_8.addItem("Pa", 8)
        self.beat_list_8.addItem("Komal Dha", 9)
        self.beat_list_8.addItem("Dha", 10)
        self.beat_list_8.addItem("Komal Ni", 11)
        self.beat_list_8.addItem("Ni", 12)
        self.beat_list_8.addItem("Sa^", 13)
        self.beat_list_8.activated.connect(self.updateNoteList)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateNoteList(self):
        self.data_packet.data.update({1:self.beat_list_1.currentData()})
        self.data_packet.data.update({2:self.beat_list_2.currentData()})
        self.data_packet.data.update({3:self.beat_list_3.currentData()})
        self.data_packet.data.update({4:self.beat_list_4.currentData()})
        self.data_packet.data.update({5:self.beat_list_5.currentData()})
        self.data_packet.data.update({6:self.beat_list_6.currentData()})
        self.data_packet.data.update({7:self.beat_list_7.currentData()})
        self.data_packet.data.update({8:self.beat_list_8.currentData()})

        print(self.data_packet.data)

        json_object = json.dumps(self.data_packet.data, indent=4)
 
        # Writing to sample.json
        with open("data_packet.json", "w") as outfile:
            outfile.write(json_object)
        

def startGUI():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def soundProcessing():
    print("In sound processing")

    with open('data_packet.json', 'r') as openfile:
        json_object = json.load(openfile)
        print(json_object)
        delay_time = 60/json_object.get("tempo")
        duration = json_object.get("duration")
        print(delay_time)
    while(True):
        for i in range(8):
            with open('data_packet.json', 'r') as openfile:
                json_object = json.load(openfile)
                delay_time = 60/json_object.get("tempo")
                duration = json_object.get("duration")
                print(json_object)
            
            notes=[]
            for j in range(1,9):
                notes.append(index_to_note_table.get(json_object.get(str(j))))

            frequencies=[]
            for n in notes:
                if n == '-':
                    frequencies.append(0)
                else:
                    note=music21.note.Note(n)
                    frequencies.append(note.pitch.frequency)
            
            print(frequencies)

            try:
                p = pyaudio.PyAudio()
                t = np.linspace(0, duration, int(duration * 48000), False)
                note = np.sin(2 * np.pi * frequencies[i] * t)
                stream = p.open(format=pyaudio.paFloat32,
                                channels=1,
                                rate=48000,
                                output=True)
                stream.write(note.astype(np.float32).tostring())
                stream.stop_stream()
                stream.close()
            except:
                pass
            
            time.sleep(delay_time-duration)

if __name__=="__main__":
    gui_process = multiprocessing.Process(target=startGUI)
    gui_process.start()

    sound_process = multiprocessing.Process(target=soundProcessing)
    sound_process.start()