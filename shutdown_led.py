#!/usr/bin/python3

from gpiozero import LED, Button
from signal import pause
import sys, os

ledGPIO = int(sys.argv[1]) if len(sys.argv) >= 2 else 27  # Raspberry Pi 1
btnGPIO = int(sys.argv[2]) if len(sys.argv) >= 3 else 7   # Raspberry Pi 1
time_to_shutdown = 5


led = LED(ledGPIO)
button = Button(btnGPIO, hold_time = 1, hold_repeat=True)


def when_pressed():

  # led.blink()
  print(f"Button is pressed. Shutdown threshold is {time_to_shutdown}-seconds.")


def when_released():

  led.off()
  print("Button released. Shutdown counter is reset.")


def when_held(button):

  elapsed_time = round(button.pressed_time)
  print(f"Button pressed for (seconds): {elapsed_time}")

  led.blink(on_time=1/(2**elapsed_time), off_time=1/(2**elapsed_time))

  if elapsed_time > time_to_shutdown:
    led.off()
    print (f"Button exceeded {time_to_shutdown}-seconds threshold. Shutting down now...")
    os.system("sudo halt")


if __name__ == '__main__':

  button.when_pressed = when_pressed
  button.when_released = when_released
  button.when_held = when_held


  pause()
