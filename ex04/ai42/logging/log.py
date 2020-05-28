from getpass import getuser
import time


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
        logfile.write(f"[ exec-time = {elapsed:.3f} {time_unit:<2} ]\n")
        logfile.close()
        return result
    return logged
