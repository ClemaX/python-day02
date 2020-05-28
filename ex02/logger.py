import time
from random import randint

from getpass import getuser


def log(method):
    def logged(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        username = getuser()
        name = method.__name__.replace('_', ' ').title()
        logfile = open(r"machine.log", "a+")
        elapsed = end - start
        if elapsed > 1:
            time_unit = 's'
        else:
            elapsed *= 1000
            time_unit = 'ms'
        logfile.write(f"({username})Running: {name:<18} ")
        logfile.write(f"[ exec-time = {elapsed:.3f} {time_unit:<2}]\n")
        return result
    return logged


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
