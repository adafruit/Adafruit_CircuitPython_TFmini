Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-tfmini/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/tfmini/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_TFmini/workflows/Build%CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_TFmini/actions/
    :alt: Build Status

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Code Style: Ruff

A CircuitPython/Python library for Benewake's TF mini distance sensor

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-tfmini/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-tfmini

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-tfmini

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install adafruit-circuitpython-tfmini

Usage Example
=============

.. code-block:: python

	import time
	import board  # comment this out if using pyserial
	import busio  # comment this out if using pyserial
	import adafruit_tfmini

	# Use hardware uart
	uart = busio.UART(board.TX, board.RX)

	# Or, you can use pyserial on any computer
	#import serial
	#uart = serial.Serial("/dev/ttyS2", timeout=1)

	# Simplest use, connect with the uart bus object
	tfmini = adafruit_tfmini.TFmini(uart)

	# You can put in 'short' or 'long' distance mode
	tfmini.mode = adafruit_tfmini.MODE_SHORT
	print("Now in mode", tfmini.mode)

	while True:
	    print("Distance: %d cm (strength %d, mode %x)" %
		  (tfmini.distance, tfmini.strength, tfmini.mode))
	    time.sleep(0.1)


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/tfmini/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TFmini/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
