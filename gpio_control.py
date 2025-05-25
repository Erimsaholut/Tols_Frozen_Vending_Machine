import RPi.GPIO as GPIO
import time

RELAY_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)

time.sleep(3)

GPIO.output(RELAY_PIN, GPIO.HIGH)

GPIO.cleanup()