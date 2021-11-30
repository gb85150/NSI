import winsound
import time

def relou(frequency: int, duration: int):
    winsound.Beep(frequency, duration)


if __name__ == '__main__':
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    for i in range(10):
        relou(frequency, duration)
        time.sleep(0.5)