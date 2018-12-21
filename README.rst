Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-tfmini/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/tfmini/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_TFmini.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_TFmini
    :alt: Build Status

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
    python3 -m venv .env
    source .env/bin/activate
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


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TFmini/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-tfmini --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
