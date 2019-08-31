# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)

# 忽略警告信息
GPIO.setwarnings(False)


class Light(object):
    '''
    三色灯
    '''
    # RGB三色灯引脚定义
    R, G, B = 22, 27, 24

    def __init__(self):
        '''
        初始化
        '''
        GPIO.setup(self.R, GPIO.OUT)
        GPIO.setup(self.G, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        self.pwmR = GPIO.PWM(self.R, 70)
        self.pwmG = GPIO.PWM(self.G, 70)
        self.pwmB = GPIO.PWM(self.B, 70)

        self.pwmR.start(0)
        self.pwmG.start(0)
        self.pwmB.start(0)

    def open(self):
        '''
        开灯
        :return:
        '''
        self.open_red()
        self.open_green()
        self.open_blue()

    def open_red(self):
        '''
        打开红色
        :return:
        '''
        self.pwmR.ChangeDutyCycle(100)

    def open_green(self):
        '''
        打开绿色
        :return:
        '''
        self.pwmG.ChangeDutyCycle(100)

    def open_blue(self):
        '''
        打开蓝色
        :return:
        '''
        self.pwmB.ChangeDutyCycle(100)

    def turn_red(self):
        '''
        关闭红色
        :return:
        '''
        self.pwmR.ChangeDutyCycle(0)

    def turn_green(self):
        '''
        关闭绿色
        :return:
        '''
        self.pwmG.ChangeDutyCycle(0)

    def turn_blue(self):
        '''
        关闭蓝色
        :return:
        '''
        self.pwmB.ChangeDutyCycle(0)

    def turnoff(self):
        '''
        关灯
        :return:
        '''
        self.turn_red()
        self.turn_green()
        self.turn_blue()

    def flicker(self, frequency=0.25):
        '''
        闪烁
        :param frequency: 间隔 默认0.25s
        :return:
        '''
        self.open()
        time.sleep(frequency)
        self.turnoff()
        time.sleep(frequency)

    def breathing(self, seconds=0):
        '''
        呼吸灯
        :param seconds: 持续时间 默认2s
        :return:
        '''

        r_value = random.randint(0, 100)
        r_threshold = random.randint(1, 5)
        r_flag = True
        g_value = random.randint(0, 100)
        g_threshold = random.randint(1, 5)
        g_flag = True
        b_value = random.randint(0, 100)
        b_threshold = random.randint(1, 5)
        b_flag = True
        start_time = time.time()
        while seconds == 0 or time.time() - start_time <= seconds:
            if r_value + r_threshold >= 100:
                r_flag = False
            if r_value - r_threshold <= 3:
                r_flag = True

            if g_value + g_threshold >= 90:
                g_flag = False
            if g_value - g_threshold <= 3:
                g_flag = True

            if b_value + b_threshold >= 100:
                b_flag = False
            if b_value - b_threshold <= 3:
                b_flag = True
            r_value = self._calculation(r_value, r_flag)
            g_value = self._calculation(g_value, g_flag)
            b_value = self._calculation(b_value, b_flag)
            self.pwmR.ChangeDutyCycle(r_value)
            self.pwmG.ChangeDutyCycle(g_value)
            self.pwmB.ChangeDutyCycle(b_value)
            time.sleep(0.05)

        self.turnoff()

    def _calculation(self, value=50, flag=True, threshold=2):
        if flag:
            return value + threshold
        else:
            return value - threshold


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    light = Light()
    # light.open()
    # time.sleep(2)
    # light.turnoff()
    # time.sleep(2)
    # for l in range(10):
    #     light.flicker()
    #     print(l)
    t1 = time.time()
    light.breathing()
    light.breathing(1)
    light.breathing(1)
    light.breathing(1)
    print(time.time() - t1)
