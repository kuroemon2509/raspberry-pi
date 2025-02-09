import RPi.GPIO as GPIO
import time

# use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False:
    start = time.time()

while GPIO.input(ECHO) == True:
    end = time.time()

sig_time = end - start

sound_speed = 343.21  # m/s
distance = sound_speed * sig_time / 2

print('Distance:', distance, 'm')

GPIO.cleanup()
