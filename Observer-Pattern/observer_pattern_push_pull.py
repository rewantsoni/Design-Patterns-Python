# With Push Pull Logic
# Observer Pull the changed data
import abc


class IObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        return 'not implemented'


class IObservable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(IObservable):
    def __init__(self, temperature):
        self.observers = []
        self.temperature = temperature

    def add_observer(self, observer):
        print('Adding the observer {}'.format(observer.__class__.__name__))
        self.observers.append(observer)

    def remove_observer(self, observer):
        print('Removing the observer {}'.format(observer.__class__.__name__))
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def get_temperature(self):
        return self.temperature

    def set_temperature(self):
        print('Setting the temperature')
        self.temperature = self.temperature + 1
        self.notify_observers()


class PhoneDisplay(IObserver):
    def __init__(self, weather_station):
        self.station = weather_station

    def update(self):
        print('In PhoneDisplay temperature is {}'.format(self.station.get_temperature()))


class WindowDisplay(IObserver):
    def __init__(self, weather_station):
        self.station = weather_station

    def update(self):
        print('In WindowDisplay temperature is {}'.format(self.station.get_temperature()))


class SomeRandomDisplay(IObserver):
    def __init__(self, weather_station):
        self.station = weather_station

    def update(self):
        print('In SomeRandomDisplay temperature is {}'.format(self.station.get_temperature()))


if __name__ == '__main__':
    station = WeatherStation(33)

    wc1 = PhoneDisplay(station)
    wc2 = WindowDisplay(station)
    wc3 = SomeRandomDisplay(station)
    station.add_observer(wc1)
    station.add_observer(wc2)
    station.set_temperature()
    station.remove_observer(wc1)
    station.add_observer(wc3)
    station.set_temperature()
