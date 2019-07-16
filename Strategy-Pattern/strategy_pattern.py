import abc


# New Strategy Fly
class IFlyBehaviour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        return 'not implemented'


class SimpleFly(IFlyBehaviour):
    def fly(self):
        return 'I know how to fly simply'


class JetFly(IFlyBehaviour):
    def fly(self):
        return 'I can fly at jet speed'


class NoFly(IFlyBehaviour):
    def fly(self):
        return 'I cant Fly'


# New Strategy Quack
class IQuackBehaviour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        return 'not implemented'


class SimpleQuack(IQuackBehaviour):
    def quack(self):
        return 'I know how to quack'


class LoudQuack(IQuackBehaviour):
    def quack(self):
        return 'I can quack loudly'


class NoQuack(IQuackBehaviour):
    def quack(self):
        return 'I cant Quack'


# New Strategy Display
class IDisplayBehaviour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        return 'not implemented'


class SimpleDisplay(IDisplayBehaviour):
    def display(self):
        return 'I know how to display simply'


class JsonDisplay(IDisplayBehaviour):
    def display(self):
        return 'I know how to display in Json format'


class RawDisplay(IDisplayBehaviour):
    def display(self):
        return 'I can display in raw format'


class Duck:
    def __init__(self, i_display_strategy, i_fly_strategy, i_quack_strategy):
        self.i_display_strategy = i_display_strategy
        self.i_fly_strategy = i_fly_strategy
        self.i_quack_strategy = i_quack_strategy

    def set_display(self, i_display_strategy):
        self.i_display_strategy = i_display_strategy

    def set_fly(self, i_fly_strategy):
        self.i_fly_strategy = i_fly_strategy

    def set_quack(self, i_quack_strategy):
        self.i_quack_strategy = i_quack_strategy

    def __str__(self):
        return 'I am a Duck. {}. {}. {}.'.format(self.i_display_strategy.display(),
                                                 self.i_fly_strategy.fly(),
                                                 self.i_quack_strategy.quack())

    def get_duck(self):
        return 'I am a Duck. {}. {}. {}.'.format(self.i_display_strategy.display(),
                                                 self.i_fly_strategy.fly(),
                                                 self.i_quack_strategy.quack())


if __name__ == '__main__':
    strategy_display = JsonDisplay()
    strategy_fly = JetFly()
    strategy_quack = SimpleQuack()
    duck = Duck(strategy_display, strategy_fly, strategy_quack)
    print(duck)
    print(duck.get_duck())