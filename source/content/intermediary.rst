.. _intermediary:

SmartGridready Intermediary
---------------------------

The SmartGridready Intermediary provides access to SmartGridready compliant devices through a WebService via REST-API.

The Intermediary is the ideal solution whenever you want to communicate with SmartGridready :term:`Product` devices,
but using one of the native Communication Handler libraries (:ref:`commhandler-libraries`) in not option.
As an example if your client application is not written in a programming language where SmartGridready
provides a native library (currently Python and Java only) you can resort to the Intermediary.

You can run the SmartGridready Webservice as a standalone application or in a Docker container.

The Intermediary allows you to:

* Register multiple :term:`Products` with their product description files (see :ref:`product-description-eid`)
* Add multiple :term:`Product` device instances together with instance specific configuration (e.g device address etc.).
* Adress a :term:`Product` device by name to communicate wit the device.
* Administer :term:`Product` descriptions and :term:`Product` instances


The Intermediary is available as an open source project and hosted on GitHub:

`SGrIntermediary <https://github.com/SmartGridready/SGrJavaIntermediary>`_


.. toctree::
    :caption: Contents
    :maxdepth: 3