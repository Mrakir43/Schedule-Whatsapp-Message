from PyQt5.QtWidgets import QApplication,QWidget, \
    QPushButton,QHBoxLayout,QVBoxLayout,QStyle,QSlider,QFileDialog
from PyQt5.QtGui import QIcon,QPalette
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt,QUrl
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Player.ico"))
        self.setWindowTitle("GPlayer")
        self.setGeometry(350,100,700,500)
        p=self.palette()
        p.setColor(QPalette.Window,Qt.GlobalColor.red)
        self.setPalette(p)
        self.create_palyer()
    def create_palyer(self):
        self.mediaPlayer=QMediaPlayer(None,QMediaPlayer.VideoSurface)
        videowidget= QVideoWidget()
        self.openBtn=QPushButton("Open Video")
        self.openBtn.clicked.connect(self.open_file)
        self.playBtn=QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.clicked.connect(self.play_video)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)

        hbox=QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self.openBtn)
        vbox=QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)
        self.mediaPlayer.setVideoOutput(videowidget)
        self.setLayout(vbox)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        
    def open_file(self):
        filename,_ = QFileDialog.getOpenFileName(self,"Open Video")
        if filename!="":
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state()==QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play() 
    def mediastate_changed(self,state):
        if self.mediaPlayer.state()==QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            elf.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            

    def position_changed(self,position):
        self.slider.setValue(position)
    
    def duration_changed(self,duration):
        self.slider.setRange(0,duration)
app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())