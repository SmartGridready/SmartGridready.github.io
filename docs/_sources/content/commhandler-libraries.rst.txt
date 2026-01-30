.. _commhandler-libraries:

|dev| SmartGridready Communication Handler Libraries
====================================================

The SmartGridready repositories on GitHub provide programming libraries in Java and Python that facilitate the
implementation of SmartGridready-compliant :term:`Communicator` devices, such as :term:`Energy Manager` devices.

The main functionality of these libraries includes:

* Loading :term:Product Description Files of SmartGridready-compliant devices.
* Using the information provided in the :term:Product Description Files to translate commands
  issued via the generic SmartGridready interface into device-specific commands understood by the :term:Product device.
* Sending commands to the device.
* Receiving device responses and converting them into the standardized representations defined by the generic
  SmartGridready API.

The communication layer currently supports:

* Modbus devices
* REST-API devices
* MQTT devices

The Communication Handlers make use of a device driver library to communicate with the devices.
By default they use the 'Device Driver' libraries, provided by the SmartGridready device driver projects
(see :ref:`device-driver-libraries`). It is also possible to implement custom adapters to integrate 3rd party
device drivers.


Python Implementation
---------------------

You find the Python 'Communication Handler' Library and API docs under the following links:

* `SGrPython Library API Doc <https://smartgridready.github.io/SGrPython/docs/commhandler/>`_
* `SGrPython Library Project <https://github.com/SmartGridready/SGrPython/>`_
* `SGePython Library Integration Code Samples <https://github.com/SmartGridready/SGrPythonSamples>`_


Java Implementation
-------------------

You find the Java 'Communication Handler' Library and API docs under the following links:

* `SGrJava Library API Doc <https://smartgridready.github.io/SGrJava/docs/commhandler/index.html>`_
* `SGrJava Library Project <https://github.com/SmartGridready/SGrJava/>`_
* `SGrJava Library Integration Code Samples <https://github.com/SmartGridready/SGrJavaSamples>`_


.. toctree::
    :caption: Contents
    :maxdepth: 3