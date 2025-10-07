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

.. _<configurationList>:

<configurationList>
"""""""""""""""""""

The configuration list element lists the configuration values that must be provided for :term:`EID` when
installing/instantiating a device.

Each configuration value listed in the configuration values has somewhere a placeholder with the same
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


Interface List
^^^^^^^^^^^^^^

The interface list element lists the communication interfaces supported by the :term:`Product`.

**Supported Interfaces**

* **Modbus**

    * RTU, RTU-ASCII, modbus over serial interface RS232 and RS485.
    * TCPIP, TCPIP-ASCII
    * UDPIP, UDPIP-ASCII

* **REST-API** HTTP, HTTPS
* **Messaging** MQTT

For **Modbus** interfaces, the basic ``<interfaceList>`` is structured as follows:

::

    <interfaceList>
        <modbusInterface>
            <modbusInterfaceDescription>
                ...
            </modbusInterfaceDescription>
            <modbusAtttributes>
                ...
            </modbusAttributes>
            <functionalProfileList>
                ...
            </functionalProfileList>
        </modbusInterface>
    </interfaceList>

* ``<modbusInterfaceDescription>`` describes the details needed to setup the communication with the Modbus device.
  See :ref:`<modbusInterfaceDescription>`.
* ``<modbusAttributes>`` contains optional attributes that describe additional modbus properties that
  might be needed to operate. See :ref:`<modbusAttributes>`.
* ``<functionalProfileList>``. Contains a list of functional profiles supported by the Modbus interface.
  See :ref:`<functionalProfileList>`


For **REST-API** interfaces, the basic ``<interfaceList>`` is structured as follows:

::

   <interfaceList>
        <restApiInterface>
            <restApiInterfaceDescription>
            ...
            </restApiInterfaceDescription>
            <functionalProfileList>
            ...
            </functionalProfileList>
        </restApiInterface>
   </interfaceList>

* ``<restApiInterfaceDescription>`` describes the details needed to setup the communication with
  the WEB-/REST- service . See :ref:`<restApiInterfaceDescription>`.
* ``<functionalProfileList>``. Contains a list of supported functional profiles supported by the REST-API interface.
  See :ref:`<functionalProfileList>`.



For **Messaging** interfaces, the basic ``<interfaceList>`` is structured as follows:

::

    <interfaceList>
        <messagingInterface>
            <messagingInterfaceDescription>
            ...
            </messagingInterfaceDescription>
            <functionalProfileList>
            ...
            </functionalProfileList>
        </messagingInterface>
    </interfaceList>

* ``<restApiInterfaceDescription>`` describes the details needed to setup the communication with
  the Messaging service such as an MQTT message broker. See `<messagingInterfaceDescription>`_.
* ``<functionalProfileList>``. Contains a list of supported functional profiles supported by the REST-API interface.
  See :ref:`<functionalProfileList>`


.. note::

    The current :term:`Communication Handler` libraries `SGrJava <https://github.com/SmartGridready/SGrJava>`_ and `SGrPython <https://github.com/SmartGridready/SGrPython>`_ do support only
    one interface listed within the ``<interfaceList>``.


.. _<modbusInterfaceDescription>:

<modbusInterfaceDescription>
""""""""""""""""""""""""""""

The following basic modbus types can be selected:

* RTU - binary data communication via serial interface RS232 or RS485
* RTU-ASCII - communication via serial interface RS232 or RS485 using ASCII characters
* TCPIP - binary data communication via TCP-IP connection
* TCPIP-ASCII - communication via TCP-IP connection using ASCII characters
* UDPIP - binary communication via UDP IP connection
* UDPIP-ASCII - comunication via UDP IP connection using ASCII characters

For **Modbus RTU** and **Modbus RTU-ASCII** the `<modbusInterfaceDescription>` element is structured as follows (sample for
Modbus RTU):

::

    <modbusInterfaceDescripion>
        <modbusInterfaceSelection>RTU</modbusInterfaceSelection>
        <modbusRtu>
              <slaveAddr>{{slave_id}}</slaveAddr>
              <portName>{{serial_port}}</portName>
              <baudRateSelected>{{serial_baudrate}}</baudRateSelected>
              <byteLenSelected>{{serial_databits}}</byteLenSelected>
              <paritySelected>{{serial_parity}}</paritySelected>
              <stopBitLenSelected>{{serial_stopbits}}</stopBitLenSelected>
              <serialInterfaceCapability>
                <baudRatesSupported>1200</baudRatesSupported>
                <baudRatesSupported>2400</baudRatesSupported>
                <baudRatesSupported>4800</baudRatesSupported>
                <baudRatesSupported>9600</baudRatesSupported>
                <baudRatesSupported>19200</baudRatesSupported>
                <baudRatesSupported>38400</baudRatesSupported>
                <baudRatesSupported>57600</baudRatesSupported>
                <baudRatesSupported>115200</baudRatesSupported>
                <byteLenSupported>8</byteLenSupported>
                <paritySupported>EVEN</paritySupported>
                <paritySupported>NONE</paritySupported>
                <paritySupported>ODD</paritySupported>
                <stopBitLenSupported>1</stopBitLenSupported>
              </serialInterfaceCapability>
        </modbusRtu>
    </modbusInterfaceDescription>

*   ``<modbusInterfaceSelection``: one of:

    * RTU
    * RTU-ASCII

*   ``<modbusRtu>``: Container for the serial interface properties.
*   ``<slaveAddr>``: Defines the Modbus slave address used by the device.
*   ``<portName>``: Operating system's ame of the serial port to be used (e.g. COM3, /dev/ttyS0)
*   ``<baudRateSelected>``: The baud rate to be used for the serial communication.
*   ``<paritySelected>``: The parity calculation method to be used for the serial communication.
*   ``<stopBitLenSelected>``: The number of stop-bits used for the serial communicaion.
*   ``<serialInterfaceCapability>``: The baud-rates, byte-length, parity calculation methods and stop-bit numbers that
    are supported by the device. These are read-only values and provide information about the :term:`Product` capabilities.


For **Modbus TCP-IP** and **Modbus UDP-IP** the `<modbusInterfaceDescription>` element is structured as follows (sample
for Modbus TCP-IP):

::

    <modbusInterfaceDescription>
        <modbusInterfaceSelection>TCPIP</modbusInterfaceSelection>
        <modbusTcp>
            <port>{{ip_port}}</port>
            <address>{{ip_address}}</address>
            <slaveId>{{slave_id}}</slaveId>
        </modbusTcp>
        <firstRegisterAddressIsOne>false</firstRegisterAddressIsOne>
        <bitOrder>BigEndian</bitOrder>
    </modbusInterfaceDescription>

* ``<modbusInterfaceSelection>``: one of:

    * TCPIP
    * TCPIP-ASCII
    * UDPIP
    * UDPIP-ASCII

* ``<modbusTcp>``: Container for the TCP-IP and UDP connection properties.
* ``<port>{{ip_port}}</port>``: The TCP/UDP IP port,
* ``<address>{{ip_address}}</address>``: The TCP/UDP IP address (v4, v6).
* ``<slaveId>``: The modbus slave-ID to be adressed.


.. note::

    The values in double brackets like ``{{serial_port}}`` or ``{{ip_address}}`` will be replaced by the configuration
    value with the name in brackets, in our examples ``serial_port`` and ``ip_address``. See also
    :ref:`<configurationList>`.



.. _<modbusAttributes>:

<modbusAttributes>
""""""""""""""""""

The ``<modbusAttributes>`` element is optional, and may contains following optional elements that define additional
properties of the Modbus interface.

The  ``modbusAttributes`` element is as follows (all elements are optional):

::

    <modbusAttributes>
        <pollingLatencyMs>500</pollingLatencyMs>
        <accessProtection>
            <modbusExceptionCode>IllegalFunction</modbusExceptionCode>
            <modbusExceptionCode>IllegalAddress</modbusExceptionCode>
            <isEnabled>true</isEnabled>
        </accessProtection>
        <layer6Deviation>
            <2RegBase1000_L2H/>
        </layer6Deviation>
    </modbusAttributes>

* ``<pollingLatencyMs``: Defines the latency (delay between sending a request and receiving a response) of the data read
  from the :term:`Product` device.
* ``<accessProtection>``: Modbus datapoints may be protected by execptions. If this is the case, a
  datapoint may be selected as true with a range of supported exceptions. A NOT listed
  exception means no XY exception.
* ``<modbusExceptionCode``: One of:

    * IllegalFunction
    * IllegalAddress
    * IllegalDataValue
    * SlaveFailure
    * ACK
    * SlaveBusy
    * NACK
    * MemoryParityErr
    * GtwyPathErr
    * GtwyTargetErr

* ``<isEnabled>``:

    * if ``true``: the listed exceptions are enabled
    * if ``false``: the listed exceptions are disabled

* ``<layer6Deviation>``: Is used to correct non standard data representation on the application layer (layer6).
  Following settings are supported:

    * ``2RegBase1000_L2H`` : 2 registers represent a combined value. As an example a metering value shows kWh at the lower
      address and MWh at the higher address, where ``higherUnit = 1000 * lowerUnit``.
    * ``2RegBase1000_H2L`` : 2 registers represent a combined value. As an example a metering value shows MWh at the lower
      address and kWh at the higher address, where ``higherUnit = 1000 * lowerUnit``.


.. _<restApiInterfaceDescription>:

<restApiInterfaceDescription>
"""""""""""""""""""""""""""""

The ``<restApiInterfaceDescription>`` element is structured as follows:

::

      <restApiInterfaceDescription>
        <restApiInterfaceSelection>URI</restApiInterfaceSelection>
        <restApiUri>{{baseUri}}</restApiUri>
        <restApiAuthenticationMethod>BearerSecurityScheme</restApiAuthenticationMethod>
        <restApiBearer>
            <restApiServiceCall>
                ...
            </restApiServiceCall>
        </restApiBearer>
      </restApiInterfaceDescription>

* ``<restApiInterfaceSelection>``: Selects the type of the addressing used for the communication. The address type
    is expected suit the address given within the element ``<restApiUri>`` One of:

    * TCPV4
    * TCPV6
    * URI

* ``<restApiUri>``: the base URI use to connect to the web service. This value must be common for all :term:"Data Points"
  listed within the element :ref:`<functionalProfileList>`. Specific endpoint addresses can be configured as path relative
  to the URI given in ``restApiUri``
* ``restApiAuthenticationMethod`` the authentication method used to connect to the server. One of

   * NoSecurityScheme : no security is applied
   * BearerSecurityScheme : a bearer token is needed to authenticate. See :ref:`<restApiBearer>`.
   * ApiKeySecurityScheme : an API key is used to access the webservice: Add the API key to the http header for each
     datapoint definition.
   * BasicSecurityScheme : use username and password. See :ref:`<restApiBasic>`
   * DigestSecurityScheme : use a digest securty scheme: RFU.
   * PskSecurityScheme : use a PSK security scheme: RFU.
   * OAuth2SecurityScheme : use OAuth2 : RFU.
   * HawkSecurityScheme : use Hawk security scheme : RFU.
   * AwsSignatureSecurityScheme : use AWS security scheme. Add the API key to the http header for each datapoint definition.
     See the 'Note'in :ref:`<restApiServiceCall>` on how to add an authentication header to the web service call.

* ``<restApiBearer>``: container for the web service call to authenticate and get the bearer token. The received bearer token
  is then added to the http header for each subsequent WEB service call to read :term:`Data Points`.
  See :ref:`<restApiServiceCall>` for details.
* ``<restApiServiceCall>``: defines the web service call to get the bearer token. See :ref:`<restApiServiceCall>`.


.. _<restApiBearer>:

<restApiBearer>
"""""""""""""""

The ``<restApiBearer>`` element specifies the web service call needed to get a bearer token when the authentication
scheme ``AuhtenticationSchemeBearer`` is required.

The SGr libraries SGrJava <https://github.com/SmartGridready/SGrJava>`_
and `SGrPython <https://github.com/SmartGridready/SGrPython>`_ extract the bearer token according the rules defined
in the ``<restApiServiceCall`` and store it in memory. The token is then automatically added to the https heaser
as ``Authorization: Bearer <token>`` for all subsequent web service calls that communicate with the :term:`Product`
device.

For a detailed description of the ``<restApiServiceCall>`` see :ref:`<restApiServiceCall>`.

The following example shows a ``<restApiServiceCall>`` definition that provides login data in the request body and
extracts the bearer token named 'accessToken' from the response body using a JMESPath expression:

::

    <restApiAuthenticationMethod>BearerSecurityScheme</restApiAuthenticationMethod>
    <restApiBearer>
      <restApiServiceCall>
        <requestHeader>
          <header>
            <headerName>Accept</headerName>
            <value>application/json</value>
          </header>
          <header>
            <headerName>Content-Type</headerName>
            <value>application/json</value>
          </header>
        </requestHeader>
        <requestMethod>POST</requestMethod>
        <requestPath>/authentication</requestPath>
        <requestBody>{"strategy": "local", "email": "{{username}}", "password": "{{password}}"}</requestBody>
        <responseQuery>
          <queryType>JMESPathExpression</queryType>
          <query>accessToken</query>
        </responseQuery>
      </restApiServiceCall>
    </restApiBearer>

.. note::

    For a complete description of all elements used above see :ref:`<restApiServiceCall>`.

.. note::

    Here is a description of the most important elements regarding the :ref:`<restApiServiceCall>` within the
    :ref:`<restApiBearer>` definition:

    * ``<requestBody>`` defines the request body to be sent in the web service request. Note {{username}} and {{password}}
      parameters within the double brackets. Username and password are provided as configuration parameters.
      See also :ref:`<configurationList>`.

    * ``<responseQuery>`` defines the JMESPath query to extract the bearer token from the http response body, named ``accessToken``.
      The response body could be something like:

      ::

        {
            "userID" : "JohnDoe",
            "tokenExpiry" : "2025-04-24T02:35:00Z",
            "accessToken" : "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgeWVsbG93IGJveC4="
        }



.. _<restApiBasic>:

<restApiBasic>
""""""""""""""

Within the :ref:`<restApiBasic>` element you can define basic authentication used for each service call used to read or
write data for a :term:`Data Point`.

The SGr libraries SGrJava <https://github.com/SmartGridready/SGrJava>`_
and `SGrPython <https://github.com/SmartGridready/SGrPython>`_ build automatically a base 64 encoded authorization header
``Authorization: Basic base64( "user:password")`` the is used in all service calls the access a :term:`Data Point`.

Example for a :ref:`<restApiBasic>` element:

::

    <restApiAuthenticationMethod>BasicSecurityScheme</restApiAuthenticationMethod>
    <restApiBasic>
      <restBasicUsername>{{username}}</restBasicUsername>
      <restBasicPassword>{{password}}</restBasicPassword>
    </restApiBasic>


.. note::

    ``{{username}}`` and ``{{password}}`` are placeholder values and are intednded to be replaced by the correct value
    when loading and initializing the :term:`Communication Handler` libraries. See :ref:`<configurationList>`



.. _<restApiServiceCall>:

<restApiServiceCall>
""""""""""""""""""""

The ``<restApiServiceCall`` is used to define the web service call needed to read from a :term:`Data Point` or write
to a :term:`Data Point`. It is further used to communicate with authentication web services for example to get a
a bearer token for further authentication (see :ref:`<restApiBearer>`).

An example for a ``restApiService`` call looks as follows:

::

    <restApiServiceCall>
      <requestHeader>
        <header>
          <headerName>Accept</headerName>
          <value>application/json</value>
        </header>
      </requestHeader>
      <requestMethod>GET</requestMethod>
      <requestPath>/digitaltwins?sensor_id={{sensor_id}}</requestPath>
      <responseQuery>
        <queryType>JMESPathExpression</queryType>
        <query>sum([[0].ten_sec.p_l1,[0].ten_sec.p_l2,[0].ten_sec.p_l3])</query>
      </responseQuery>
    </restApiServiceCall>

* ``<requestHeader>`` : contains a list of ``<header>`` elements that define the http-header added to the
  http request.
* ``<header>`` : represents one http-header entry consisting of a ``<headerName>`` / ``<headerValue`` pair.
* ``<requestMethod>`` the request http-method to be used. One of:

  * GET
  * POST
  * PUT
  * DELETE
  * PATCH
* ``<requestPath>`` : determines the path used to access the web service endpoint. The path is concatenated
  with the base path given by the ``restApiUri`` within the ``<restApiInterfaceDescription>`` (see
  :ref:`<restApiInterfaceDescription>`.
* ``<responseQuery>`` : is the container for the query parameters that extract the result value from the
  webservice response body.
* ``<queryType>`` : determines the type of the query language. It is one of the following:

  * JMESPathExpression : uses JMESPath to extract a value from a JSON response. See also `JMESPath <https://jmespath.org/>`_.
  * XPathExpression : uses XPAth to extract the a value from a XML response. See also `XPath <https://en.wikipedia.org/wiki/XPath>`_.
  * RegularExpression : uses a regular expression to extract the value from a textual response: See also `Regular Expression <https://en.wikipedia.org/wiki/Regular_expression>`_.
  * JMESPathMapping : used to map and restructure JSON response to another JSON representation: Details see
    :ref:`JMESPathMapping` for details.
  * ``<query>`` : contains the query expression in the query language given by ``<queryType>``. The example above shows a
    JMESPath expression that calulates the sum of three values given by the response.

.. note::

    If you need an API key for web service authentication you can add the API key directly to the ``<requestHeader>``
    element as a configuration value. For example with the authentication method ``<restApiAuthenticationMethod>``
    ``ApiKeySecurityScheme`` you can add:

    ::

       <header>
          <headerName>x-api-key</headerName>
          <value>AbCdEfGhIjKlMnOpQrStUvWxYz123456</value>
       </header>




.. _<messagingInterfaceDescription>:

<messagingInterfaceDescription>
"""""""""""""""""""""""""""""""

TODO






.. _<functionalProfileList>:

<functionalProfileList>
"""""""""""""""""""""""

TODO


.. _JMESPathMapping:

JMESPathMapping
"""""""""""""""

TODO


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