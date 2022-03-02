from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26
LED = [17, 27, 22]


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
for pin in LED:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

app = Flask(__name__)

#create some routes
@app.route("/")
def index():
    return "Hello From Flask"

@app.route("/push-button")
def check_push_button_status():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Push Button Pressed"
    return "Push Button Not Pressed"

@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    if not led_pin in LED:
        return "Wrong GPIO pin" + str(led_pin)
    if led_state == 1:
        GPIO.output(led_pin, GPIO.HIGH)
    elif led_state == 0:
        GPIO.output(led_pin, GPIO.LOW)
    else:
        return "State must be 0 or 1"
    return("OK")

app.run(host="0.0.0.0")