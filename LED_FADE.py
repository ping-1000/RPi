
import RPi.GPIO as GPIO
from time import sleep

ledpin = [12,32,35]				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
# ~ GPIO.setup(ledpin,GPIO.OUT)
# ~ pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
			#start PWM of required Duty Cycle 
            
def s_color(pin1):
    GPIO.setup(pin1,GPIO.OUT)
    pi_pwm = GPIO.PWM(pin1,1000)
    pi_pwm.start(0)	
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.0075)
    sleep(0.7)
    
    for duty in range(100,-1,-1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.0075)
    sleep(0)
def d_color(pin1,pin2):
    GPIO.setup(pin1,GPIO.OUT)
    GPIO.setup(pin2,GPIO.OUT)
    pi_pwm = GPIO.PWM(pin1,1000)
    pi_pwm2 = GPIO.PWM(pin2,1000)
    pi_pwm.start(0)	
    pi_pwm2.start(0)	
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.0075)
    sleep(0.7)
    
    for duty in range(100,-1,-1):
        pi_pwm.ChangeDutyCycle(duty)
        pi_pwm2.ChangeDutyCycle(duty)
        sleep(0.0075)
    sleep(0.1)
    
def t_color(pin1,pin2,pin3):
    GPIO.setup(pin1,GPIO.OUT)
    GPIO.setup(pin2,GPIO.OUT)
    GPIO.setup(pin3,GPIO.OUT)
    pi_pwm = GPIO.PWM(pin1,1000)
    pi_pwm2 = GPIO.PWM(pin2,1000)
    pi_pwm3 = GPIO.PWM(pin3,1000)
    pi_pwm.start(0)	
    pi_pwm2.start(0)	
    pi_pwm3.start(0)	
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm3.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.0075)
    sleep(0.7)
    
    for duty in range(100,-1,-1):
        pi_pwm.ChangeDutyCycle(duty)
        pi_pwm2.ChangeDutyCycle(duty)
        pi_pwm3.ChangeDutyCycle(duty)
        sleep(0.0075)
    sleep(0.1)

while True:
    s_color(ledpin[0])
    s_color(ledpin[1])
    s_color(ledpin[2])
    
    t_color(ledpin[0],ledpin[1],ledpin[2])
    
    d_color(ledpin[0],ledpin[1])
    d_color(ledpin[0],ledpin[2])
    d_color(ledpin[1],ledpin[2])
