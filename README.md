# shutdown_led
Python script to shutdown Raspberry Pi (with led incrementing blinking speed)

Uses the Raspberry Pi GPIO to enable a button to provide shutdown without needing to physically login to the device. If available, an LED will blink to signify the button press and will continue to blink faster until shutdown (6 seconds of continuous button press). The shutdown can be aborted by releasing the button anytime before the 6 seconds.
