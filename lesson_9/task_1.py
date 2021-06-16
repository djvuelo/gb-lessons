from time import sleep


class TrafficLight:
    __color = 'red'
    __sec = 7

    def running(self):
        while True:
            print(f'{self.__color} light')
            for i in range(0, self.__sec):
                sleep(1)
            self.set_state()

    def set_state(self):
        if self.__color == 'red':
            self.__color = 'yellow'
            self.__sec = 2
        elif self.__color == 'yellow':
            self.__color = 'green'
            self.__sec = 2
        elif self.__color == 'green':
            print('-' * 10 + 'цикл' + '-' * 10)
            self.__color = 'red'
            self.__sec = 7


traffic_light1 = TrafficLight()
traffic_light1.running()
