from bluedot import BlueDot
from gpiozero import AngularServo
from signal import pause

wheel = AngularServo(20)
turn = AngularServo(21)

bd = BlueDot()

def move(pos):
    if pos.top:
        wheel.angle = 90
    elif pos.bottom:
        wheel.angle = -90
    elif pos.left:
        turn.angle = -90
    elif pos.right:
        turn.angle = 90
    elif pos.middle:
        turn.angle = 0
        wheel.angle = -10


bd.when_pressed = move
bd.when_moved = move

pause()
