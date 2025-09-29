TODO
* detailed description of :term:`EID` XML's
* data format XML, definition XSD
* howto create an EID
* examples of current EID's
* external link to the EID library
* Link and desc to SGrLibrary


.. _product-description-eid:

:term:`Product Description File`
================================

Introduction
------------

The :term:`Product Description File` contains the information needed to describe the :term:`Product` and use it
through the generic SmartGridready API.

This allows potential :term:`Communicator` devices such as :term:`EMS` to easily integrate, implement, or access
any SmartGridready certified product through a standardized set of functionalities.

The :term:`Product Description File` contains:

* General information about the :term:`Product` such as product name, description or the product supplier.
* The configuration parameters needed to operate the product.
* The communication interface/protocol that is used to read values from and control the :term:`Product`. Supported
  interfaces/protocols are:

  * Modbus
  * Http/REST
  * MQTT

* The :term:`Functional Profiles` that are supported by the :term:`Product`
* The :term:`Data Points` that are provided by the :term:`Product`

:numref:`figure_product_description_file_structure` shows the structure of a :term:`Product Description File`:

.. _figure_product_description_file_structure:

.. figure:: images/product.drawio.png
    :alt: :term:`Product Description File` Structure

    :term:`Product Description File` Structure


The :term:`Product Description File` is an XML file, defined by the SmartGridready XML Schema (XSD) which builds
the core of the SmartGridready Specification. You find the according resources on Github within SmartGridready
project `SGrSpecifications <https://github.com/SmartGridready/SGrSpecifications/>`_:

* SGr XML Schema (XSD): `Schema Database <https://github.com/SmartGridready/SGrSpecifications/tree/master/SchemaDatabase>`_.
* :term:`Product Description Files` : `External Interfaces <https://github.com/SmartGridready/SGrSpecifications/tree/master/XMLInstances/ExtInterfaces>`_

:term:`Product Description File` content
----------------------------------------

The following chapters describe the term:`Product Description File` (:term:`EID`) content und and are intended provide
a guide for :term:`EID` creators.

General Information
^^^^^^^^^^^^^^^^^^^

This chapter describes the XML elements that provide general information


<deviceName>
""""""""""""

The name and optionally the model of the device.

Example:

::

  <deviceName>
    CLEMAP Energy Monitor
  </deviceName>


<manufacturer>
""""""""""""""

The name of the manufacturer

Example:

::

  <manufacturer>
    CLEMAP
  </manufacturer>

<releaseNotes>
""""""""""""""

The publication status and release version of the :term:`EID`, together with the publisher.

Example:

::

  <releaseNotes>
    <state>Published</state>
    <changeLog>
        <version>1.0.0</version>
        <date>2024-01-24</date>
        <author>Jane Doe, Acme</author>
        <comment>Published</comment>
    </changeLog>
  </releaseNotes>

<deviceInformation>
"""""""""""""""""""

Common device information, together with a legible description.

Explanations of specific child elements:

* **<legibleDescription>**: The CDATA[[]] container allows formatting text with HTML syntax. This is used for the
  :term:`Product` description text in the `SGr library <https://library.smartgridready.ch/>`_.
* **<deviceCategory>**: The device category consists of an enumerated list of device categories inherited from the
  EEBUS specification.
* **<levelOfOperation>** see :ref:`level_of_operation`

Example:

::

  <deviceInformation>
    <legibleDescription>
      <textElement>CDATA[[Some device description ... <p> ... ]]</textElement>
      <language>de</language>
      <uri>https://www.clemap.com/...</uri>
    </legibleDescription>
    <deviceCategory>
        SubMeterElectricity
    </deviceCategory>
    <isLocalControl>false</isLocalControl>
    <softwareRevision>1.0.0</softwareRevision>
    <hardwareRevision>1.0.0</hardwareRevision>
    <manufacturerSpecificationIdentification>
        CLEMAP
    </manufacturerSpecificationIdentification>
    <levelOfOperation>m</levelOfOperation>
    <versionNumber>
      <primaryVersionNumber>1</primaryVersionNumber>
      <secondaryVersionNumber>0</secondaryVersionNumber>
      <subReleaseVersionNumber>0</subReleaseVersionNumber>
    </versionNumber>
    <testState>Verified</testState>
  </deviceInformation>



Configuration List
^^^^^^^^^^^^^^^^^^

<configurationList>
"""""""""""""""""""

The configuration list element lists the configuration values that must be provided for :term:`EID` when
installing/instantiating a device.

Each configuration value listed in the configuration values has somewhere placeholder sibling with the same
name in the :term:`EID` which is replaced with the configuration value when installing/instantiating a device
using the :term:`EID`.

As an example, the configuration entry:

::

    <configurationListElement>
      <name>ipaddress</name>
      <dataType>
        <string/>
      </dataType>
    </configurationListElement>

corresponds to a placeholder ``{{ipaddress}}`` used elsewhere in the :term:`EID`. This placeholder will be replaced
with the actual configuration value during installation or instantiation.

This convention enables the use of the same :term:`EID` for multiple device instances by parameterizing instance-specific
values.

Example:

::

 <configurationList>
    <configurationListElement>
      <name>ipaddress</name>
      <dataType>
        <string/>
      </dataType>
      <configurationDescription>
        <textElement>Device IP address</textElement>
        <language>en</language>
        <label>IP Address</label>
      </configurationDescription>
      <configurationDescription>
        <textElement>IP Adresse des Gerätes</textElement>
        <language>de</language>
        <label>IP Adresse</label>
      </configurationDescription>
    </configurationListElement>
    <configurationListElement>
 </configurationList>






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
* test (aliases: testState)
* manufacturer (aliases: manufacturerName)
* device (aliases: deviceName, product, productName)
* interface (aliases: -)
* category (aliases: deviceCategory)
* fpCategory (aliases: functionalProfileCategory)
* fpType (aliases: functionalProfileType)
* level (aliases: levelOfOperation)






Product EI-XML Documentation on GitHub
--------------------------------------

`Product External Interface XML <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/product.md>`_


.. toctree::
    :caption: Contents
    :maxdepth: 3