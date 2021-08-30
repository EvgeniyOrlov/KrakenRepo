import time


class TrafficLight:
    # Attribute
    def __init__(self, c):
        self.__color = c

    def running(self, r, y, g):
        while True:     # Работает в непрерывном режиме, до выключения.
            self.__color = r
            print("\033[31m {}" .format(r))
            time.sleep(7)
            self.__color = y
            print("\033[33m {}" .format(y))
            time.sleep(2)
            print("\033[32m {}" .format(g))
            self.__color = g
            time.sleep(5)
            print("\033[32m {}".format(g))
            self.__color = g
            time.sleep(1)
            print("\033[32m {}".format(g))
            self.__color = g
            time.sleep(1)
            print("\033[32m {}".format(g))
            self.__color = g
            time.sleep(1)
            self.__color = y
            print("\033[33m {}".format(y))
            time.sleep(3)


s = TrafficLight('Red')
s.running('Red', 'Yellow', 'Green')
