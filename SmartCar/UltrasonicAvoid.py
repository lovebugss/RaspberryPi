# -*- coding:UTF-8 -*-

import time
import logging
from Car import Car
from Servo import Servo
from Ultrasound import Ultrasound

logger = logging.getLogger()


def probe(ultrasound, font_servo):
    font_servo.set_servo('2%')
    d1 = ultrasound.test()
    font_servo.set_servo('25%')
    d2 = ultrasound.test()
    font_servo.set_servo('75%')
    d3 = ultrasound.test()
    font_servo.set_servo('98%')
    d4 = ultrasound.test()
    font_servo.set_servo('50%')

    return d1, d2, d3, d4


def main():
    car = Car()
    ultrasound = Ultrasound()
    font_servo = Servo(0)

    time.sleep(2)
    safe_distance = 70
    while True:

        # 1. 是否符合前进条件
        dis = ultrasound.test()
        if dis < safe_distance:
            # 移动
            d1, d2, d3, d4 = probe(ultrasound, font_servo)
            if max(d1, d2, d3, d4) < 100:
                car.back(0.2)
            if d1 == max(d1, d2, d3, d4):
                car.right(0.5)
            if d2 == max(d1, d2, d3, d4):
                car.right(0.25)
            if d3 == max(d1, d2, d3, d4):
                car.left(0.25)
            if d4 == max(d1, d2, d3, d4):
                car.left(0.5)

        time.sleep(1)
        # 向前移动
        # 重新获取距离
        distance = ultrasound.test()
        while distance > safe_distance:
            car.run()
            time.sleep(0.1)
            distance = ultrasound.test()
        else:
            car.stop()


if __name__ == '__main__':
    main()
