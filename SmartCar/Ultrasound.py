# -*- coding:UTF-8 -*-

import time
import logging
import RPi.GPIO as GPIO

logger = logging.getLogger()

# 设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)
# 忽略警告信息
GPIO.setwarnings(False)


class Ultrasound(object):
    '''
    超声波测距
    '''

    def __init__(self):
        self.EchoPin = 0
        self.TrigPin = 1
        GPIO.setup(self.EchoPin, GPIO.IN)
        GPIO.setup(self.TrigPin, GPIO.OUT)

    def test(self):
        GPIO.output(self.TrigPin, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.TrigPin, GPIO.LOW)
        while not GPIO.input(self.EchoPin):
            pass
        t1 = time.time()
        while GPIO.input(self.EchoPin):
            pass
        t2 = time.time()
        dis = ((t2 - t1) * 340 / 2) * 100
        logger.info("distance is %f " % dis)
        time.sleep(0.0001)
        return dis


if __name__ == '__main__':
    ultrasound = Ultrasound()
    dis = ultrasound.test()
    print(dis)
