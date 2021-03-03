import vlc
from gpiozero import Button

music = vlc.MediaPlayer("file:///home/pi/catberry/sound/hbsong.mp3")

def handleBtnStartPress():
    global music
    print("Play")
    music.play()

def handleBtnPausePress():
    global music
    print("Pause")
    music.pause()


def handleBtnStopPress():
    global music
    print("Stop")
    music.stop()



btnStart = Button(5)
btnPause = Button(6)
btnStop = Button(19)

btnStart.when_pressed = handleBtnStartPress
btnPause.when_pressed = handleBtnPausePress
btnStop.when_pressed = handleBtnStopPress


while True:
    continue
