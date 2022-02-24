import board
import adafruit_dht
import drivers
import RPi.GPIO as GPIO
import time
#
display = drivers.Lcd()

d = adafruit_dht.DHT11(board.D4)

d.measure()
t1=d.temperature

display.lcd_display_string("Temp : "+str(t1), 1)#

GPIO.setmode(GPIO.BCM)
fan = 14
heat = 15
GPIO.setup(fan, GPIO.OUT)
GPIO.setup(heat, GPIO.OUT)
check = 0
check001=0
i=0

while 1:
    try:
        d.measure()
        t = d.temperature
        file003 = open("/home/pi/iot_project/data_dht.txt", 'w')
        file003.write(str(t))
        file003.close()
        if t1 != t:
            display.lcd_display_string("Temp : "+str(t), 1)
            t1=t
    except RuntimeError:
        print('Failed')
    file = open("/home/pi/iot_project/data.txt", 'r')
    data = file.readline()
    data_want = int(data)
    file.close()
    file001 = open("/home/pi/iot_project/data_dht.txt", 'r')
    data001 = file001.readline()
    data_dht = int(data001)
    file001.close()
    if data_dht>data_want and check==0:
        i=0
        check001=0
        GPIO.output(fan, True)
        GPIO.output(heat, True)
        check = 1
        print ("fan on, i = ", i, ", check = ", check, ", check001 = ", check001)
    else:
        if check==1:
            if data_dht<=data_want-3:
                GPIO.output(fan, False)
                check=0
                check001=1
                print ("fan off, i = ", i, ", check = ", check, ", check001 = ", check001)
        elif check001 == 1:
            i+=1
            print ("heat on, i = ", i, ", check = ", check, ", check001 = ", check001)
            if i==6:
                GPIO.output(heat, False)
                i=0
                check001=0
                print ("heat off, i = ", i, ", check = ", check, ", check001 = ", check001)
    time.sleep(5)
