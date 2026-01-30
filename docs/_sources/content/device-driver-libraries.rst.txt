.. _device-driver-libraries:

SmartGridready Device Driver Libraries
======================================

SmartGridready hosts device driver libraries in Java and Python, used by the :ref:`commhandler-libraries` to
communicate with the :term:`Product` devices. By default Communication Handlers use this device drivers out of the
box. However, it is also possible to implement custom adapters to communicate via 3rd party device drivers.

Device Drivers are available for the following `protocols` / technologies:

* Modbus
* Web Services / REST
* MQTT


Python Default Implementations
------------------------------

The Python device drivers are part of the SGrPython library project:
`SGrPython library including device drivers <https://github.com/SmartGridready/SGrPython>`_

Java Default Device Driver Implementations
------------------------------------------

The Java device drivers are hosted in a separate GitHub project:
`SGrJava Drivers <https://github.com/SmartGridready/SGrJavaDrivers>`_
