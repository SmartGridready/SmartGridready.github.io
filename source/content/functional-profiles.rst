.. _functional-profiles:

Functional Profiles
===================

A :term:`Functional Profile` describes a set of related functionalities provided by a :term:`Product`.
It thereby focuses entirely on the functionality. Any transport-specific details are not part of the functional profile
(e.g. on how to get or set a :term:`Datapoint` on a specific product).

The main intent is to allow communicator manufacturers to easily implement their use cases based on logically grouped
:term:`Datapoints`, while device-specific communication details are handled SmartGridread CommHandler library.

Any :term:`Product` that supports the :term:`Functional Profiles` required for a specific use case is therefore automatically
compatible and can be used without changing the :term:`Communicator` implementation.

The :term:`Functional Profiles` build the foundation of the SmartGridready specification and allow access to any
SmartGridready compliant :term:`Product` through a generic API.

The SmartGridready library lists the currently available :term:`Functional Profiles`:
See `Functional Profile Library <https://library.smartgridready.ch/FunctionalProfileTemplate>`_

This list of :term:`Functional Profile` definitions is subject to change and will grow in the future, as new
:term:`Functional Profiles` will be added.

As a :term:`Product` supplier you need check which :term:`Functional Profiles` suit your :term:`Product`'s functionalities
and add the matching :term:`Functional Profiles` to the :term:`External Interface Definition` file.

Functional Profile Structure
----------------------------

A :term:`Functional Profile` is part of a :term:`Product` description and includes the:

* Definition of the :term:`Functional Profile` with identification and description.
* :term:`Datapoints` defining access points to measure and control data on the :term:`Product`.

.. code-block:: none

   PRODUCT
   ├── DEFINITION (Generic product info ...)
   │
   ├── FUNCTIONAL-PROFILE (ActiveEnergyAC)
   │   ├── DATAPOINT (ActiveEnergyACTot)
   │   ├── DATAPOINT (ActiveEnergyACTot)
   │   ├── DATAPOINT (ActiveEnergyACL1)
   │   ├── DATAPOINT (ActiveEnergyACL3)
   │   └── DATAPOINT (ActiveEnergyACL3)
   │
   └──FUNCTIONAL-PROFILE (ActivePowerAC)
       ├── DATAPOINT (ActivePowerACTot)
       ├── DATAPOINT (ActivePowerACL1)
       ├── DATAPOINT (ActivePowerACL3)
       └── DATAPOINT (ActivePowerACL3)

The illustration above shows a sample for the structure of a :term:`Product` description file in XML (:term:`EID`).
The :term:`Product` description exposes its functionalities by including two :term:`Functional Profiles`.
The example shows a simple :term:`Smart Meter` that exposes AC-energy metering and AC-power measurement functionalities.

A :term:`Communicator` software can read from or write to the device by addressing the :term:`Datapoint` by
:term:`Functional Profile` name and :term:`Datapoint` name. Java code example:

.. code-block:: java

    var acPowerTotal = meteringDevice.getVal("ActiveEnergyAC", "ActiveEnergyACTot");

A functional profile is defined/identified by:

* **Functional Profile Category:** see :ref:`functional_profile_category`
* **Functional Profile Type:** see: :ref:`functional_profile_types`
* **Level Of Operation:** see :ref:`level_of_operation`
* **Version Number:** see :ref:`version_number`

.. _functional_profile_category:

:term:`Functional Profile Categories`
-------------------------------------

The :term:`Functional Profile Category` is related the type of a :term:`Product` and its functionalities.

The list below shows the currently published :term:`Functional Profile Categories` (follow the links for a detailed
description):

.. list-table::
    :widths: 23 54 23
    :header-rows: 1

    * - Category
      - Assigned to :term:`Functional Profiles` used with :term:`Products` of type:
      - Details page

    * - **Actuator**
      - Used with actuator :term:`Products`. Examples for actuator devices are electrical relays, servo motors etc.
      - :ref:`actuator`

    * - **Battery**
      - Used with battery :term:`Products`, e.g. batteries that store electrical energy produced by a :term:`PVA`.
      - :ref:`battery`

    * - **BatterSystem**
      - Used with combined systems that consist of a battery and an :ref:`Inverter`
      - :ref:`battery-system`


    * - **DeviceInformation**
      - Has no predefined :term:`Datapoints`. Used to provide device information and add manufacturer proprietary
        :term:`Datapoints`.
      - :ref:`device-information`

    * - **DynamicTariff**
      - Used to query dynamic tariff information from a power grid operator system.
      - :ref:`device-information`

    * - **EVSE**
      - Used for Electrical Vehicle Supply Equipment (:term:`EVSE`) :term:`Products` like charging stations.
      - :ref:`device-information`

    * - **HeatingCircuit**
      - Used with :term:`Products` that allow reading information from a heating circuit, such as temperature.
      - :ref:`heating-circuit`

    * - **HeatPumpControl**
      - Used with :term:`Products` that allow controlling heat pumps and reading information from heat pumps.
      - :ref:`heating-circuit`


    * - **Inverter**
      - Used with :term:`Products` that allow controlling and reading status from :term:`PV-Inverter` devices.
      - :ref:`inverter`

    * - **Metering**
      - Used with :term:`Products` that provide metering an measurement functionalities like electrical power or energy
        consumption, for example smart meter devices.
      - :ref:`metering`

    * - **SGCP**
      - Used for Smart Grid Connection Point (:term:`SGCP`) :term:`Products`.
      - :ref:`metering`

    * - **Sensor**
      - Used with :term:`Products` that allow reading data from sensor devices, for example a humidity sensor.
      - :ref:`sensor`

    * - **TemperatureSensor**
      - Used with :term:`Products` that measure temperatures.
      - :ref:`temperature-sensor`


.. toctree::
    :maxdepth: 1
    :hidden:

    functional-profile-categories/actuator
    functional-profile-categories/battery
    functional-profile-categories/battery-system
    functional-profile-categories/device-information
    functional-profile-categories/dynamic-tariff
    functional-profile-categories/evse
    functional-profile-categories/heating-circuit
    functional-profile-categories/heatpump-control
    functional-profile-categories/inverter
    functional-profile-categories/metering
    functional-profile-categories/sgcp
    functional-profile-categories/sensor
    functional-profile-categories/temperature-sensor


.. _functional_profile_types:

:term:`Functional Profile Types`
--------------------------------

The :term:`Functional Profile Types` are assigned to a :term:`Functional Profile Category` and define a set of related
functionalities and associated :term:`Datapoints`.

.. list-table:: :term:`Functional Profile Types`
    :header-rows: 1
    :widths: 25 50 25

    * - :term:`Functional Profile Type`
      - Description
      - Associated :term:`Functional Profile Category`
    * - ActiveEnergyAC
      - Provides AC energy metering :term:`Datapoints` for single phase, multi phase and total energy consumption.
      - :ref:`metering`
    * - ActiveEnergyBalanceAC
      - Provides energy balance metering :term:`Datapoints` providing data for imported, exported and net energy towards
        the power grid.
      - :ref:`metering`
    * - ActivePowerAC
      - Provides AC power measurement for single phase, multi phase and total power consumption.
      - :ref:`metering`
    * - ApparentEnergyAC
      - Provides :term:`Datapoints` for AC apparent energy metering. Supports single phase, multi phase and total
        apparent energy metering.
      - :ref:`metering`
    * - ApparentPowerAC
      - Provides :term:`Datapoints` for AC apparent power measurement. Supports single phase, multi phase and total
        apparent power measurements.
      - :ref:`metering`
    * - BiDirFlexMgmt
      - Functional profile for Energy Management Systems (EMS) that feature a bidirectional communication interface with
        a flexibility manager (e.g., utility company / grid operator). The interface allows both the retrieval of
        current data and the targeted control of power at the grid connection point via defined data points.
      - :ref:`sgcp`
    * - BufferStorageCtrl
      - This :term:`Functional Profile` type extends the **HeatPumpBase** :term:`Functional Profile` type. It provides
        :term:`Datapoints` to read temperature from and control heat pump buffer storage devices.
      - :ref:`heatpump-control`
    * - CurrentAC
      - Provides :term:`Datapoints` for AC current measurements. Supports single phase, multi phase and current
        against the neutral conductor measurements.
      - :ref:`metering`
    * - CurrentDC
      - Defines a single :term:`Datapoint` to measure DC current.
      - :ref:`metering`
    * - DeviceInformation
      - Empty functional profile without data points that can be used for vendor specific information and data points.
        It allows the handling of data points, which are valid for the whole device.
      - :ref:`device-information`
    * - DomHotWaterCtrl
      - This :term:`Functional Profile` type extends the **HeatPumpBase** :term:`Functional Profile`. It provides
        :term:`Datapoints` that are available for controlling a domestic hot water circuit.
      - :ref:`heatpump-control`
    * - EMS_Current_Limit
      - This :term:`Functional Profile` type enables a controller to set a current limitation for a charging station
        (Electric Vehicle Supply Equipment, :term:`EVSE`).
      - :ref:`evse`
    * - ESVEState
      - :term:`Functional Profile` for reading the status of the connector of an electric vehicle charging station
        (:term:`EVSE`).
      - :ref:`evse`
    * - EnergyMonitor
      - :term:`Functional Profile` that supports :term:`Datapoints` to read operating data such as energy consumption
        from a :term:`Product`.
      - :ref:`heatpump-control`, :ref:`battery`, :ref:`battery-system`
    * - FlexMgmt
      - :term:`Functional Profile` for Energy Management Systems (EMS) that feature a bidirectional communication
        interface with a flexibility manager (e.g., utility company / grid operator). The interface allows both the
        retrieval of current data and the targeted control of power at the grid connection point via defined data points.
      - :ref:`SGCP`
    * - Frequency
      - Defines a single :term:`Datapoint` to measure AC frequency.
      - :ref:`metering`
    * - HeatCoolCtrl
      - This :term:`Functional Profile` type extends the **HeatPumpBase** :term:`Functional Profile`. It provides
        :term:`Datapoints` that are available for controlling a heat pump heating and cooling circuit.
      - :ref:`heatpump-control`
    * - HeatPumpBase
      - This is the basic :term:`Functional Profile` for heat pumps. It allows operation mode control and reading operation
        status and measure temperature etc.
      - :ref:`heatpump-control`
    * - Humidity
      - Defines a single :term:`Datapoint` to measure humidity.
      - :ref:`Sensor`
    * - LoadManagement
      - :term:`Functional Profile` type for Energy Management Systems (EMS) with a communication interface to the the
        flexibility manager (to power suppliers, pooling providers or similar) that is controllable via two relay contacts.
      - :ref:`SGCP`
    * - LoadReduction_EVSE
      - :term:`Functional Profile` type to control load reduction of Electrical Vehicle Supply Equipement :term:`EVSE`.
      - :ref:`EVSE`
    * - PowerCtrl
      - :term:`Functional Profile` type to control the power consumption of heat pumps by controlling parameters
        like compressor power consumption or compressor rotations per minute.
      - :ref:`heatpump-control`
    * - PowerFactor
      - Provides :term:`Datapoints` to read the power factor defined as:

        .. math::

            PowerFactor = \frac{ActivePower}{ApparentPower}

        It supports single phase, multi phase and overall measurement.
      - :ref:`metering`


..  Comments regarding functional profile category and profile types:
    - FP-Category seems to be oriented on the type of the product HeatPump, EVSE, SGCP, Smart Meter etc.
      However: Metering category is more related to many types of products that allow of metering (Zähler) and measuring (messen).

    - FP-type seems to be oriented on concrete functionalities like measure ActivePowerAC, HeatCoolCtrl, LoadCtrl
      There are functional profile types that are used within multiple categories:
      type EnergyMonitor -> categories battery, battery system and heatpump-control

    - LoadReduction_EVSE vs. EMS_Current_Limit: would level of operation be sufficient to distinguish them?

    - BiDirFlexMgmt vs. FlexMgmt: The FP template description for BiDirFlex says nothing about BiDir, however the
      description of FlexMgmt does.



.. _level_of_operation:

:term:`Level of Operation`
---------------------------

Level of control defining the complexity

.. _version_number:

:term:`Functional Profile` Version Number
-----------------------------------------
Version of the functional profile.

* changes in primaryVersionNumber indicate breaking changes,
* changes in secondaryVersionNumber indicate complimentary changes,
* changes in subReleaseVersionNumber are without impact on the functionality

:term:`Datapoints`
-------------------
A :term:`Functional Profile` mainly defines a set of :term:`Datapoints`. The :term:`Datapoints` define access points to values
that can be read from or written to the product.

The :term:`Datapoints` are defined by the following attributes:

.. list-table:: :term:`Datapoint` Attributes
    :header-rows: 1
    :widths: 30 70

    * - Element
      - Description
    * - :term:`Datapoint` Name
      - Name of the :term:`Datapoint`. Should be unique within the functional profile.
    * - Data Direction
      - * 'R' if :term:`Datapoint` can be read
        * 'W` if :term:`Datapoint` can be written
        * 'P` if :term:`Datapoint` is persisted
    * - Presence Level
      - Datapoint availability within an :term:`Product` that implements the :term:`Functional Profile`:
        * Mandatory
        * Recommended
        * Optional
    * - Data Type
      - Data type of the :term:`Datapoint` value. (e.g. float32, int, string...)
    * - Alternative Names
      - A list of relevant name spaces list for to display names used in different standards like
        EEBUS, IEC6850, SAREF4ENER etc.
    * - Legible Description
      - Optional, can occur once per language. Contains details concerning the intended use case of the functional profile.

If a :term:`Datapoint` is defined as mandatory in the functional profile, it must also be present in the product implementing
this functional profile.

If no :term:`Datapoint` is mandatory in the functional profile, then at least one :term:`Datapoint` must be recommended and at least
one of the recommended :term:`Datapoints` must be presentin the product implementing this :term:`Functional Profile`.


Sub Datapoints
--------------

Datapoints that are connected to other :term:`Datapoints` can be modeled as sub :term:`Datapoints`.
The connection between :term:`Datapoint` and sub :term:`Datapoint` are defined with naming conventions. If e.g. a :term:`Datapoint` has the
name "MainDatapoint" and is connected with a sub :term:`Datapoint` "SubDatapoint" the sub :term:`Datapoint` name has the name
"MainDatapoint.SubDatapoint" - this means, the sub :term:`Datapoint` name is appended to the main :term:`Datapoint` name separated
with a dot.

An example for a sub :term:`Datapoint` is "Voltage.Precision" as the precision of the :term:`Datapoint` "Voltage".

Defining Functional Profiles
----------------------------

File Naming Scheme
^^^^^^^^^^^^^^^^^^
Functional profiles should have the following file naming conventions:

.. code-block:: none

    FP_[specificationOwnerIdentification]_[FunctionalProfileCategory]_[FunctionalProfileType]_[levelOfOperation]_[majorVerion].[minorVerion].xml

**Writing Descriptions**
Functional profile descriptions should be structured as follows:
* Image indicating the typical use of the functional profile, together with an easily understandable title
* Short explanation (i.e. long version of the title)
* Detailed explanation, including very attribute.
* Description on how to apply the functional profile concerning presence level (i.e. how to handle recommended and optional :term:`Datapoints`)


Release Notes
^^^^^^^^^^^^^^
The release notes section contains meta data that describe history and current state of the functional profile.

.. list-table:: Releas Notes
    :header-rows: 1
    :widths: 30 70

    * - Element
      - Description
    * - Status
      - One of 'Draft', 'Review', 'Released', 'Revoked'
    * - Remarks
      - Optional, text with remarks e.g. can be useful during the draft phase for todo's etc.
    * - Change Log
      - Optional, can occur multiple times. Contains release notes to the version concerned



:term:`Functional Profile` Release Process
------------------------------------------

See `Functional Profile Release Process <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/functionalProfile_process.md>`_




Additional Documentation on GitHub
----------------------------------

See `Functional Profile Documentation <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/functionalProfile.md>`_

