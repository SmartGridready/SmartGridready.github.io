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

:term:`Functional Profile` Structure
------------------------------------

Figure :ref:`figure_functional_profile_structure` shows the basic structure of a :term:`Functional Profile`

.. _figure_functional_profile_structure:

.. figure:: images/functionalProfile.drawio.png
   :alt: :term:`Functional Profile` Structure

   Functional Profile Structure

A :term:`Functional Profile` is part of a :term:`Product` description and includes the:

* Definition of the :term:`Functional Profile` with identification and description.
* :term:`Datapoints` defining access points to measure and control data on the :term:`Product`.

Example:

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
      - Used with :term:`Functional Profile Category`
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


.. _level_of_operation:

:term:`Level of Operation`
---------------------------

LevelOfOperation defines a complexity level of the :term:`Product` device controls:

.. list-table:: Level of Operation
    :header-rows: 1
    :widths: 10 30 60

    * - Level
      - Description
      - Details
    * - m
      - Monitoring
      - Supports reading of values and settings
    * - 1
      - On-Off
      - The interface allows switching between two discrete operating states
    * - 2
      - Discrete values
      - The interface allows switching between two multiple discrete operating states
    * - 3
      - Set of characteristic curves
      - The interface enables the selection of various pre-configured characteristic
        curves (Discrete, as there is a limited number of characteristic curves).
        Grid-friendly characteristic curves, which can react to grid voltage, are also
        assigned to this level without communication via the SmartGridready interface.
    * - 4
      - Continuous values
      - The interface allows the setting of continuous values. This stage builds upon
        level 2.
    * - 5
      - Dynamically changeable characteristics tables
      - The interface allows the setting of continuous control parameters or characteristic
        curve values. This stage builds upon level 3.
    * - 6
      - Prediction based systems
      - The interface allows the setting of new setpoints and control parameters /
        characteristic curve values based on energy production or load forecasts, up to
        the inclusion of a digital twin.


Levels 1-6 can be combined with a the monitoring (m) level if they offer
read-only data points

(see
`FunctionalProfileDescription.xsd <https://github.com/SmartGridready/SGrSpecifications/blob/master/SchemaDatabase/SGr/Generic/BaseType_LevelOfOperationType.xsd>`__
for details…)


.. _generic_attributes:

Generic Attributes
------------------

Generic attributes incorporate hierarchical inheritance as follows:

- Generic attributes always apply to the data point
- Generic attributes defined on functional profile level apply to all data points of the same
  functional profile.
- Generic attributes defined on device level apply to all functional profiles, and thus to all
  data points of the device If the same attribute is defined on multiple levels the most specific
  definition supersedes any other definition (i.e. data point over functional profile over).

.. _static_datapoint_attributes:

Static Data Point Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These values describe the measurement limits for data points. Depending
on the definition level they apply either to a specific data point,
every data point of a functional profile, or the the entire device.

These attributes are generally used to search for devices that fulfill a
set of minimum requirements to support a specific use case.

+---------------------+---------------+------------------+------------+
| SGr Attribute       | Data Type     | Description      | Example    |
+=====================+===============+==================+============+
| MeasuredValueType   | enum          | Me               | value      |
|                     |               | asuredValueType: |            |
|                     |               | type of          |            |
|                     |               | measurement.     |            |
|                     |               | Possible values  |            |
|                     |               | are “value”,     |            |
|                     |               | “min”, max”,     |            |
|                     |               | “average”,       |            |
|                     |               | “stdDev”         |            |
+---------------------+---------------+------------------+------------+
| Specia              | string        | indicates        | METAS      |
| lQualityRequirement |               | Quality          |            |
|                     |               | requirements     |            |
|                     |               | fulfilled like   |            |
|                     |               | formal           |            |
|                     |               | certifications   |            |
+---------------------+---------------+------------------+------------+
| PrecisionPercent    | float32       | the precision of | 2.0%       |
|                     |               | a measurement,   |            |
|                     |               | calculation      |            |
|                     |               | result or result |            |
|                     |               | of a controls    |            |
|                     |               | process          |            |
+---------------------+---------------+------------------+------------+
| MaximumLatencyTime  | float         | Maximum time in  | 10 ms      |
|                     |               | milliseconds     |            |
|                     |               | from capturing   |            |
|                     |               | of measured      |            |
|                     |               | value until      |            |
|                     |               | ready at the     |            |
|                     |               | product          |            |
|                     |               | interface        |            |
|                     |               | (i.e             |            |
|                     |               | analog-digital   |            |
|                     |               | conversion time) |            |
+---------------------+---------------+------------------+------------+
| SampleRate          | unsignedLong  | SampleRate in    | 200 ms     |
|                     |               | milliseconds     |            |
+---------------------+---------------+------------------+------------+

.. _stability_fallback:

Stability Fallback
^^^^^^^^^^^^^^^^^^

A consumer or a generating system receives the permit for a load change
for a certain period of time. This time is always set to 0 each time a
confirmation message is received (HeartBeat).

The figure below depicts the typical flow 1. the device starts at
initial value. 2. regular communication starts. The communicator
periodically sets new set values. 3. communication breaks. The device
receives its last set value. 4. after reaching the timeout the device
automatically sets the fallback value.

.. figure:: images/genAttributes_sstabilityFallback.drawio.png
   :alt: SGr Stability Fallback

   SGr Stability Fallback

+---------------------+---------------+------------------+------------+
| Stability Fallback  | Data Type     | Description      | Example    |
| Value               |               |                  |            |
+=====================+===============+==================+============+
| maxReceiveTime      | float         | If the device    | 3600.0 s   |
|                     |               | does not receive |            |
|                     |               | any              |            |
|                     |               | communication    |            |
|                     |               | within this time |            |
|                     |               | the device       |            |
|                     |               | applies the      |            |
|                     |               | fallback.        |            |
+---------------------+---------------+------------------+------------+
| initValue           | float         | Initial value    | 6.0 A      |
|                     |               | the device       |            |
|                     |               | before the       |            |
|                     |               | communicator     |            |
|                     |               | sets this value  |            |
|                     |               | (e.g.at          |            |
|                     |               | startup, or      |            |
|                     |               | beginning of     |            |
|                     |               | cycle).          |            |
+---------------------+---------------+------------------+------------+
| fallbackValue       | float         | Value the device | 6.0 A      |
|                     |               | uses in case of  |            |
|                     |               | a fallback       |            |
+---------------------+---------------+------------------+------------+

.. _smooth_transition:

Smooth Transition
^^^^^^^^^^^^^^^^^

The time behavior of a transition from a power adjustment (positive as
well as negative) can be determined by several time values, so that this
starts with a random time delay, changes via a ramp and an expiry time
with return to the initial value. To avoid return to the initial value
the device must either specify the revert time to zero (i.e. no return),
or the communicator must repeat the target value before the revert time
window expires.

The figure below depicts the typical flow 1. the command for the new
target value is received 2. the device randomly starts the ramp, but
latest after winTms 3. the ramp reaches the new target value after
rmpTms 4. if no new target value is received, the device starts
returning to the old target value after rvtTms 5. the ramp reaches the
old target value after rmpTms

.. figure:: images/genAttributes_smoothTransition.drawio.png
   :alt: SGr Smooth Transition

   SGr Smooth Transition

+---------------------+---------------+------------------+------------+
| Smooth Transition   | Data Type     | Description      | Example    |
| Value               |               |                  |            |
+=====================+===============+==================+============+
| winTms              | unsigned long | indicates a time | 300 s      |
|                     |               | window in which  |            |
|                     |               | the new          |            |
|                     |               | operating mode   |            |
|                     |               | is started       |            |
|                     |               | randomly. The    |            |
|                     |               | time window      |            |
|                     |               | begins with the  |            |
|                     |               | start command of |            |
|                     |               | the operating    |            |
|                     |               | mode. The value  |            |
|                     |               | 0 means          |            |
|                     |               | immediate        |            |
+---------------------+---------------+------------------+------------+
| rmpTms              | unsigned long | specifies how    | 450 s      |
|                     |               | quickly the      |            |
|                     |               | changes should   |            |
|                     |               | be made. The     |            |
|                     |               | corresponding    |            |
|                     |               | value is         |            |
|                     |               | gradually        |            |
|                     |               | changed from the |            |
|                     |               | old to the new   |            |
|                     |               | value in the     |            |
|                     |               | specified time.  |            |
+---------------------+---------------+------------------+------------+
| rvrtTms             | unsigned long | determines how   | 7’200 s    |
|                     |               | long the         |            |
|                     |               | operating mode   |            |
|                     |               | should be        |            |
|                     |               | active. When the |            |
|                     |               | time has         |            |
|                     |               | elapsed, the     |            |
|                     |               | operating mode   |            |
|                     |               | is automatically |            |
|                     |               | terminated. If   |            |
|                     |               | rvrtTms = 0      |            |
|                     |               | (standard        |            |
|                     |               | value), the      |            |
|                     |               | operating mode   |            |
|                     |               | remains active   |            |
|                     |               | until a new      |            |
|                     |               | command is       |            |
|                     |               | received.        |            |
+---------------------+---------------+------------------+------------+

.. _datapoint_quality:

Data Point Quality
^^^^^^^^^^^^^^^^^^

SGr has attributes to denote the quality of the measured value. The
presence of any quality attributes either on functional profile or data
point level indicate that the com handler will provide these dynamic
attributes at run time (see documentation of SGr com handler libs)

+---------------------+---------------+------------------+------------+
| SGr Attribute       | Data Type     | Description      | Example    |
+=====================+===============+==================+============+
| MeasuredValueSource | enum          | Value source     | mea        |
|                     |               | kind related to  | suredValue |
|                     |               | SGr level 6      |            |
|                     |               | applications.    |            |
|                     |               | Potential values |            |
|                     |               | are              |            |
|                     |               | measuredValue,   |            |
|                     |               | calculatedValue, |            |
|                     |               | empiricalValue   |            |
+---------------------+---------------+------------------+------------+

.. _curtailment:

Curtailment
^^^^^^^^^^^

Various function profiles require boundaries to set points with respect
to curtailment or home energy management systems.

+---------------------+---------------+------------------+------------+
| SGr Attribute       | Data Type     | Description      | Example    |
+=====================+===============+==================+============+
| Curtailment         | float         | Used in          | 40%        |
|                     |               | state-based      |            |
|                     |               | reduction        |            |
|                     |               | schemes. This    |            |
|                     |               | value specifies  |            |
|                     |               | the reduction in |            |
|                     |               | percent for the  |            |
|                     |               | reduced          |            |
|                     |               | operation mode.  |            |
+---------------------+---------------+------------------+------------+
| MimimumLoad         | float         | Used in          | 2 kW       |
|                     |               | state-based      |            |
|                     |               | reduction        |            |
|                     |               | schemes. In      |            |
|                     |               | locked mode the  |            |
|                     |               | product will not |            |
|                     |               | reduce its load  |            |
|                     |               | below this       |            |
|                     |               | minimum value    |            |
+---------------------+---------------+------------------+------------+
| MaximumLockTime     | float         | used in          | 20 min     |
|                     |               | state-based      |            |
|                     |               | reduction        |            |
|                     |               | schemes. A       |            |
|                     |               | reduction        |            |
|                     |               | command to       |            |
|                     |               | reduced or       |            |
|                     |               | locked mode      |            |
|                     |               | shall not be     |            |
|                     |               | applied longer   |            |
|                     |               | than this        |            |
|                     |               | specified        |            |
|                     |               | duration         |            |
+---------------------+---------------+------------------+------------+
| MinimumRunTime      | float         | Used in          | 15 min     |
|                     |               | state-based      |            |
|                     |               | reduction        |            |
|                     |               | schemes. When    |            |
|                     |               | returning to     |            |
|                     |               | normal mode the  |            |
|                     |               | normal mode must |            |
|                     |               | be guaranteed    |            |
|                     |               | for at least the |            |
|                     |               | specified        |            |
|                     |               | duration         |            |
+---------------------+---------------+------------------+------------+
| ValueByTimeTable    | float         | Used for time    | 1 min      |
|                     |               | tables to        |            |
|                     |               | specify the      |            |
|                     |               | temporal         |            |
|                     |               | separation of    |            |
|                     |               | data curve       |            |
|                     |               | points           |            |
+---------------------+---------------+------------------+------------+
| FlexAssistance      | sgr:F         | Systems with     |            |
|                     | lexAssistance | more than One    |            |
|                     |               | communicator     |            |
|                     |               | need a           |            |
|                     |               | definition of    |            |
|                     |               | the priority of  |            |
|                     |               | the commands /   |            |
|                     |               | demands for a    |            |
|                     |               | flexibility      |            |
|                     |               | requirement.     |            |
|                     |               | This element     |            |
|                     |               | defines the kind |            |
|                     |               | of a such a      |            |
|                     |               | command          |            |
|                     |               | (serviceable for |            |
|                     |               | net (DSO),       |            |
|                     |               | energy or system |            |
|                     |               | (TNO)) and its   |            |
|                     |               | priority (SHALL  |            |
|                     |               | / SHOULD / MAY)  |            |
+---------------------+---------------+------------------+------------+


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
      - * R : :term:`Datapoint` can be read
        * W : :term:`Datapoint` can be written
        * P : :term:`Datapoint` is persisted
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

Defining :term:`Functional Profiles`
------------------------------------

File Naming Scheme
^^^^^^^^^^^^^^^^^^

:term:`Functional Profiles` should have the following file naming convention:

.. code-block:: none

    FP_[specificationOwnerIdentification]_[FunctionalProfileCategory]_[FunctionalProfileType]_[levelOfOperation]_[majorVerion].[minorVerion].xml

**Writing Descriptions**
Functional profile descriptions should be structured as follows:
* Image indicating the typical use of the functional profile, together with an easily understandable title
* Short explanation (i.e. long version of the title)
* Detailed explanation, including very attribute.
* Description on how to apply the functional profile concerning presence level (i.e. how to handle recommended and optional :term:`Datapoints`)

.. _version_number:

:term:`Functional Profile` Version Number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Version of the functional profile.

* changes in primaryVersionNumber indicate breaking changes,
* changes in secondaryVersionNumber indicate complimentary changes,
* changes in subReleaseVersionNumber are without impact on the functionality


:term:`Functional Profile` Release Process
------------------------------------------

Scope
^^^^^

This document structures the process for the life-cycle of functional
profiles.

States
^^^^^^

A :term:`Functional Profile` cycles through the following states:

.. figure:: images/functionalProfile_process.drawio.png
   :alt: SGr Functional Profile Process

   SGr Functional Profile Process

.. list-table::
    :header-rows: 1
    :widths: 25 55 20

    * - Action
      - Description
      - Next Status
    * - Inception
      - A demand for a new :term:`Functional Profile` arises. The new :term:`Functional Profile` is created in state “Draft”
      - Draft
    * - Ready for Review
      - The :term:`Functional Profile` has been developed and is ready for review by its relevant stakeholders.
      - Review
    * - Publish
      - The :term:`Functional Profile` has passed the review and is ready to be used.
      - Published
    * - Revoke
      - A :term:`Functional Profile` has passed its usefulness and is not needed any more. Any state can be directly revoked.
      - Revoked


Creating new :term:`Functional Profiles`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the :term:`Functional Profile` interest groups sees requirements for a new or
improved functionality, it will create a new :term:`Functional Profile` XML with
state “draft”. A new issue will be created for this :term:`Functional Profile`.
The issue has

- a self-evident description covering

  - context in which the need for this :term:`Functional Profile` has arisen
  - purpose of this :term:`Functional Profile`

- a label of the :term:`Functional Profile` interest group concerned
- the project “:term:`Functional Profile` Interest Group” assigned, with status
  “draft”

Any documentation, discussion, and work on the elaboration of this
:term:`Functional Profile` will be tracked in this github issue.

The team then works directly on the XML.

Ready for review
^^^^^^^^^^^^^^^^

When a new :term:`Functional Profile` is considered ready it switches the state
to review. The following criteria must be met for this step

1. Purpose and functionality of the :term:`Functional Profile` is defined
2. level of operation is defined
3. Data points are defined, including mandatory/recommended/optional,
   units, type and read/write
4. Generic attributes for the :term:`Functional Profile` and/or its data points
   are defined

Publish
^^^^^^^

To publish a :term:`Functional Profile` the following criteria must be met:

1. The version is set correctly according to the versioning scheme (see
   below).
2. All stakeholders concerned are happy with the content of the
   :term:`Functional Profile`, and have given their formal consent.
3. “SGr Deklarationsstelle” has been informed about the upcoming
   publication.
4. The :term:`Functional Profile` has been tested by at least one product.

Published :term:`Functional Profiles` will not change anymore. If a change is
requested, a new :term:`Functional Profile` with increased version number will
be created (see versioning scheme below). Therefore, only the release
note structure of the :term:`Functional Profile` can be updated on publishing.

Revoke
^^^^^^

If a :term:`Functional Profile` shall not be used anymore it can be revoked.
Only the note structure of the :term:`Functional Profile` can be updated on
publishing.

Revoked :term:`Functional Profiles` are obsolete and shall not be used for
further declarations of products and communicators. However, they will
remain the data base for legacy reasons.

Versioning Scheme
^^^^^^^^^^^^^^^^^

:term:`Functional Profiles` are numbered as follows: ``Major.Minor.Build``

+--------------------------+-------------------------------------------+
| Number                   | Description                               |
+==========================+===========================================+
| ``Major``                | Describes the major functionality family. |
|                          | Breaking changes implies an increment of  |
|                          | the major number                          |
+--------------------------+-------------------------------------------+
| ``Minor``                | Describes a backward compatible           |
|                          | evolution. Only new functionality is      |
|                          | added, but remaining functionality is     |
|                          | never changed                             |
+--------------------------+-------------------------------------------+
| ``Build``                | The functionality remains identical, but  |
|                          | minor non-functional details change, such |
|                          | as descriptions, translations, remarks    |
+--------------------------+-------------------------------------------+

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



..  TODO's
..  Comments regarding functional profile category and profile types:
    - FP-Category seems to be oriented on the type of the product HeatPump, EVSE, SGCP, Smart Meter etc.
      However: Metering category is more related to many types of products that allow of metering (Zähler) and measuring (messen).

    - FP-type seems to be oriented on concrete functionalities like measure ActivePowerAC, HeatCoolCtrl, LoadCtrl
      There are functional profile types that are used within multiple categories:
      type EnergyMonitor -> categories battery, battery system and heatpump-control

    - LoadReduction_EVSE vs. EMS_Current_Limit: would level of operation be sufficient to distinguish them?

    - BiDirFlexMgmt vs. FlexMgmt: The FP template description for BiDirFlex says nothing about BiDir, however the
      description of FlexMgmt does.

