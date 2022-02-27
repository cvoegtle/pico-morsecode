import time
from machine import Pin

LONG = 1.0
SHORT = 0.3
PAUSE = 0.3
LONG_PAUSE = 1.0

ON = 1
OFF = 0

class MorseAlphabet:
    def __init__(self, pin=25):
        self.morse_code = MorseCode(pin)

    def one(self):
        self.morse_code.short()
        self.morse_code.long()
        self.morse_code.long()
        self.morse_code.long()
        self.morse_code.long()
        self.morse_code.pause()

    def two(self):
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.long()
        self.morse_code.long()
        self.morse_code.long()
        self.morse_code.pause()

    def three(self):
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.long()
        self.morse_code.long()
        self.morse_code.pause()

    def four(self):
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.long()
        self.morse_code.pause()

    def five(self):
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.short()
        self.morse_code.pause()

    def word_end(self):
        self.morse_code.pause()
        self.morse_code.pause()


class MorseCode:
    def __init__(self, pin=25):
        self.LED = Pin(pin, Pin.OUT)

    def long(self):
        self.LED.value(ON)
        time.sleep(LONG)
        self.LED.value(OFF)
        time.sleep(PAUSE)

    def short(self):
        self.LED.value(ON)
        time.sleep(SHORT)
        self.LED.value(OFF)
        time.sleep(PAUSE)

    def pause(self):
        self.LED.value(OFF)
        time.sleep(LONG_PAUSE)

if __name__ == "__main__":
    alphabet = MorseAlphabet()
    while True:
        alphabet.five()
        alphabet.one()
        alphabet.word_end()

