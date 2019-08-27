# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import subprocess
import time

subprocess.call("echo 2=100 > /dev/servoblaster", shell=True)
# 设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)
# 忽略警告信息
GPIO.setwarnings(False)


class Servo(object):
    '''
    由于GPIO 设置舵机是会导致舵机抖动,所以使用Servoblaster来控制舵机.
    详见:https://github.com/richardghirst/PiBits/tree/master/ServoBlaster
    '''

    def __init__(self, id):
        self.id = id
        # 居中
        print('init servo')
        subprocess.call("sudo echo {}=50% > /dev/servoblaster".format(id), shell=True)

    def set_servo(self, ratio):
        '''
        设置舵机角度
        :param ratio:百分百 1-100%
        :return:
        '''
        if ratio < 0 or ratio > 100:
            raise ValueError('')
        command = "sudo echo {}={} > /dev/servoblaster".format(self.id, ratio)
        print('set servo : %s' % command)
        subprocess.call(command, shell=True)


if __name__ == '__main__':
    servo = Servo(5)
    time.sleep(2)
    servo.set_servo('100%')
    time.sleep(2)
    servo.set_servo('0%')
    time.sleep(2)
    servo.set_servo('50%')
