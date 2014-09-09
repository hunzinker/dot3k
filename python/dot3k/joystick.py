import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LEFT  = 17
RIGHT = 22
UP    = 27
DOWN  = 9
BUTTON= 4

BOUNCE= 300

def on(buttons):
    buttons = buttons if isinstance(buttons, list) else [buttons]
    
    def register(handler):
        for button in buttons:
            GPIO.remove_event_detect(button)
            GPIO.add_event_detect(button, GPIO.FALLING, callback=handler, bouncetime=BOUNCE)
    
    return register

def repeat(button, handler, delay = 0.1, ramp = 1.0):
    time.sleep(delay)
    while(GPIO.input(button) == 0):
        handler()
        time.sleep(delay)
        delay*=ramp

up    = GPIO.setup(UP,    GPIO.IN, pull_up_down=GPIO.PUD_UP)
down  = GPIO.setup(DOWN,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
left  = GPIO.setup(LEFT,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
right = GPIO.setup(RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
button= GPIO.setup(BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(UP,   GPIO.FALLING,callback=callback_up,   bouncetime=BOUNCE)
#GPIO.add_event_detect(DOWN, GPIO.FALLING,callback=callback_down, bouncetime=BOUNCE)
#GPIO.add_event_detect(LEFT, GPIO.FALLING,callback=callback_left, bouncetime=BOUNCE)
#GPIO.add_event_detect(RIGHT,GPIO.FALLING,callback=callback_right,bouncetime=BOUNCE)
#GPIO.add_event_detect(BTN,  GPIO.FALLING,callback=callback_button,  bouncetime=BOUNCE)