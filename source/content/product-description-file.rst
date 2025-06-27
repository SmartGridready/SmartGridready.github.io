.. _product-description-eid:

Product Description File
========================
* detailed description of :term:`EID` XML's
* data format XML, definition XSD
* howto create an EID
* examples of current EID's
* external link to the EID library


SmartGridready :term:`Product` Library
--------------------------------------

The currently available Product Description Files (:term:`EID`) are listed on the
`SmartGridready Product Library <https://library.smartgridready.ch/Device>`_

You can add a serach filter by modifying the base URL and adding query parameters.
Use the following base URL:

.. code-block:: text

    https://library.smartgridready.ch/Device

and add http query parameters like:

.. code-block:: text

    https://library.smartgridready.ch/Device?manufacturer=Shelly&interface=RESTfulJSON

Each parameter can contain a comma separated list of filter values:

.. code-block::

    ...&interface=RESTfulJSON,Modbus&...

Available parameters are:

* release (aliases: state, releaseState)
* test (aliase: testState)
* manufacturer (aliase: manufacturerName)
* device (aliase: deviceName, product, productName)
* interface (aliase: -)
* category (aliase: deviceCategory)
* fpCategory (aliase: functionalProfileCategory)
* fpType (aliase: functionalProfileType)
* level (aliase: levelOfOperation)



Product EI-XML Documentation on GitHub
--------------------------------------

`Product External Interface XML <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/product.md>`_


.. toctree::
    :caption: Contents
    :maxdepth: 3