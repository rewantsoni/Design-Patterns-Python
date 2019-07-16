# With Push Push Logic
# We notify the observer of the data that has changed
import abc


class IObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, temperature):
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
            observer.update(self.temperature)

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        print('Setting the temperature')
        self.temperature = temperature
        self.notify_observers()


class PhoneDisplay(IObserver):

    def update(self, temperature):
        print('In PhoneDisplay temperature is {}'.format(temperature))


class WindowDisplay(IObserver):

    def update(self, temperature):
        print('In WindowDisplay temperature is {}'.format(temperature))


class SomeRandomDisplay(IObserver):

    def update(self, temperature):
        print('In SomeRandomDisplay temperature is {}'.format(temperature))


if __name__ == '__main__':
    station = WeatherStation(33)

    wc1 = PhoneDisplay()
    wc2 = WindowDisplay()
    wc3 = SomeRandomDisplay()
    station.add_observer(wc1)
    station.add_observer(wc2)
    station.set_temperature(35)
    station.remove_observer(wc1)
    station.add_observer(wc3)
    station.set_temperature(37)
