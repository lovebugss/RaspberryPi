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
    def __init__(self, in1=20, in2=21, in3=19, in4=26, ena=16, enb=13, CarSpeedControl=50):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb
        # 设置pwm引脚和频率为2000hz
        self.pwm_ENA = GPIO.PWM(self.ENA, 2000)
        self.pwm_ENB = GPIO.PWM(self.ENB, 2000)
        self.pwm_ENA.start(0)
        self.pwm_ENB.start(0)
        self.CarSpeedControl = CarSpeedControl

        GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW)

    def run(self):
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

    def back(self):
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

    def left(self):
        '''
        左
        :return:
        '''
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(self.CarSpeedControl)
        self.pwm_ENB.ChangeDutyCycle(self.CarSpeedControl)

    def right(self):
        '''
        右
        :return:
        '''
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(self.CarSpeedControl)
        self.pwm_ENB.ChangeDutyCycle(self.CarSpeedControl)

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
