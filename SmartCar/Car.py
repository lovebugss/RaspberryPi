# -*- coding:UTF-8 -*-
'''
小车
'''
import time
import RPi.GPIO as GPIO

# 设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)
# 忽略警告信息
GPIO.setwarnings(False)


class Car(object):
    IN1 = 20
    IN2 = 21
    IN3 = 19
    IN4 = 26
    ENA = 16
    ENB = 13
    CarSpeedControl = 50

    def __init__(self):
        '''
        初始化
        :param in1:
        :param in2:
        :param in3:
        :param in4:
        :param ena:
        :param enb:
        :param CarSpeedControl:
        '''
        GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW)
        # 设置pwm引脚和频率为2000hz
        self.pwm_ENA = GPIO.PWM(self.ENA, 2000)
        self.pwm_ENB = GPIO.PWM(self.ENB, 2000)
        self.pwm_ENA.start(0)
        self.pwm_ENB.start(0)

        GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW)

    def run(self, seconds=0):
        '''
        前进
        :return:
        '''
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(self.CarSpeedControl)
        self.pwm_ENB.ChangeDutyCycle(self.CarSpeedControl)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def back(self, seconds=0):
        '''
        后退
        :return:
        '''
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(self.CarSpeedControl)
        self.pwm_ENB.ChangeDutyCycle(self.CarSpeedControl)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def left(self, seconds=0):
        '''
        左
        :return:
        '''
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(self.CarSpeedControl)
        self.pwm_ENB.ChangeDutyCycle(self.CarSpeedControl)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def right(self, seconds=0):
        '''
        右
        :return:
        '''
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(self.CarSpeedControl)
        self.pwm_ENB.ChangeDutyCycle(self.CarSpeedControl)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def stop(self):
        '''
        停止
        :return:
        '''
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)


if __name__ == '__main__':
    car = Car()
    car.run()
    time.sleep(5)
    car.stop()
    time.sleep(2)
    car.left()
    time.sleep(2)
