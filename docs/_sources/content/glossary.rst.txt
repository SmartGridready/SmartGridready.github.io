.. _glossary:

Glossary
========

.. toctree::
    :caption: Contents
    :maxdepth: 3

.. glossary::

    Communicator
        The Communicator is a device designed to interface with :term:`Product` devices. In SmartGridready the Communicator
        leverages a generic API to seamlessly communicate with :term:`Product` devices. A common example for a
        Communicator is an energy manager device.

    Communication Handler
        The Communication Handler is a software component that reads XML-based interface descriptions, which define conversion
        rules between the generic API used by the :term:`Communicator` and :term:`Product`-specific APIs.
        This allows it to adapt to different Products without requiring manual configuration/daption.

    Data Point
        A data point is a read- and/or writeable property of a :term:`Product`. In SmartGridready a :term:`Data Point`
        is a child element of a :term:`Functional Profile`. An example for a readable data point is "ActivePowerACL1"
        of the :term:`Functional Profile` "ActivePowerAC" and is used to measure the AC power consumtion on phase 1.

    Data Points
        Plural form of :term:`Data Point`

    Device Driver Adapter
        Device Driver Adpaters within SmartGridready adapt the API given by the :term:`Communication Handler` libraries to
        a transport layer/technology. SmratGridready provides default adapters for Modbus, Web-Services and MQTT
        as libraries in Python and Java.

    DSO
        A Distribution System Operator is a company or entity responsible for operating, maintaining, and developing
        the electricity distribution network — typically the lower-voltage part of the grid that delivers electricity
        from transmission systems to end consumers (homes, businesses, etc.). See also :term:`TSO` who operates
        the higher-voltage part of the gris.

    EID
        External Interface Description in XML (also known as EI-XML or Product Description File).
        The EID defines the conversion rules needed to adapt a specific :term:`Product` to the SmartGridready
        generic API. It contains a list of :term:`Functional Profile`'s that the :term:`Product` supports, together
        with the conversion rules to adapt the :term:`Product` to the generic API interface.

    External Interface Definition
        See :term:`EID`

    EMS
        Energy Management System. Device or application used for power management within an power-grid or building. Within
        SmartGridready the :term:`EMS` acts usually as a :term:`Communicator`.

    EVSE
        Electric Vehicle Supply Equipment. Provides safe and managed electrical power to charge electric vehicles.

    Energy Manager
        See :term:`EMS`

    Flexibility Manager
        The Flexibility Manager acts within a power grid allowing an intelligent load management. It is usually
        operated by a :term:`DSO`.

    Functional Profile
        The Functional Profile describes a set of common functionalities that are exposed trough the generic
        SmartGridready interface used by the :term:`Communicator`. A SmartGridready compliant :term:`Product` supports one or
        more Functional Profiles. Examples for Functional Profiles are: 'EnergyMonitor` for electric energy measurement,
        'HeatCoolControl' for heat pumps or 'EVSE Load Reduction' for electrical vehicle charging stations.

    Functional Profiles
        Plural form of :term:`Functional Profile`

    Functional Profile Type
        The type of a :term:`Functional Profile` defines a specific combination of related :term:`Data Points`.
        See :ref:`functional_profile_type`.

    Functional Profile Types
        Plural form of :term:`Functional Profile Type`.

    Functional Profile Category
        A :term:`Functional Profile Category` defines the type or usage of the :term:`Product`. Examples are 'Metering'
        (for term:`Smart Meter`) or 'HeatPumpControl`. See :ref:`functional_profile_category`

    Functional Profile Categories
        Plural form of :term:`Functional Profile Category`

    Intermediary
        The :term:`Intermediary` is a microservice that exposes a REST API that allows seamless communication with
        SmartGridready compliant :term:`Product`. It can be deployed as a Docker container and is the ideal
        SmartGridready solution where no :term:`Communication Handler` library is available.

    Level Of Operation
        :term:`Level Of Operation` is an attribute of a :term:`Functional Profile` that defines the complexity of
        the a :term:`Functional Profile` operation. See :ref:`level_of_operation`

    Modbus
        The Modbus interface is a standardized communication interface used in industrial and energy systems to enable
        data exchange between electronic devices. It is based on the Modbus protocol, originally developed by Modicon
        (now Schneider Electric) in 1979, and is widely used due to its simplicity, robustness, and openness.

    PVA
        A system of interconnected solar panels that generate electricity from sunlight.

    PV
        Photo-Voltaic system that produces electric energy from sunlight.

    PV-Inverter
        Converts the DC electricity generated by PV solar panels into AC electricity, which is used by household
        appliances and the electrical grid.

    Product
        A Product is a device that provides power management related services and exposes its functionalities through a
        proprietary interface. The SmartGridready :term:`Communication Handler` allows the :term:`Communicator` to communicate with
        the :term:`Product` through a generic interface, independent of the Product's proprietary implementation. Examples for
        :term:`Products` are smart meters, heat pumps, :term:`PVA`, :term:`EVSE`.

    Product Description File
        See :term:`EID`

    Product Description Files
        Plural of :term:`Product Description File`

    Products
        Plural form of :term:`Product`

    SGCP
        Smart Grid Connection Point. A exposing an :term:`SGCP` allows load management by a power grid operator.

    Smart Meter
        A smart meter is an advanced electric energy meter that automatically records energy consumption and
        communicates the data to the utility provider in real-time or at scheduled intervals.
        Unlike traditional meters, smart meters enable remote readings, dynamic pricing, and better energy management,
        helping both consumers and providers optimize energy use.

    TNO
        A transmission net operator. Synonym of :term:`TSO`

    TSO
        A Transmission System Operator is an entity responsible for the transport of electricity over
        high-voltage transmission networks from power producers to distribution networks or large industrial
        consumers. TSOs operate the backbone of the electrical power grid.

