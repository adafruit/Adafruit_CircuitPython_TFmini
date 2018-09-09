import time
import board
import adafruit_tfmini

# Use hardware uart
import busio
uart = busio.UART(board.TX, board.RX)

# Simplest use, connect with the uart bus object
tfmini = adafruit_tfmini.TFmini(uart)

# You can put in 'long distance' mode
#tfmini.mode = adafruit_tfmini.MODE_LONG
#print("Now in mode", tfmini.mode)

while True:
    print("Distance: %d cm (strength %d, mode %x)" %
          (tfmini.distance, tfmini.strength, tfmini.mode))
    time.sleep(0.1)
