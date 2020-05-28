import ai42.logging.log
import ai42.progressbar
import time


@ai42.logging.log.log
def test_log():
    print("Hello console!")
    return "Hello log!"


listy = range(1000)
ret = 0
for elem in ai42.progressbar.ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)

test_log()
