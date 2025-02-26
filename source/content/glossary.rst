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

    CommHandler
        The CommHandler is a software component that reads XML-based interface descriptions, which define conversion
        rules between the generic API used by the :term:`Communicator` and :term:`Product`-specific APIs.
        This allows it to adapt to different Products without requiring manual configuration/daption.

    EID
        External Interface Description in XML (also known as EI-XML). The EID defines the conversion rules needed to
        adapt a specific :term:`Product` to the SmartGridready generic API. It contains a list of :term:`Functional
        Profile`'s that the :term:`Product` supports, together with the conversion rules to adapt the :term:`Product`
        to the generic API interface.

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
        The Flexibility Manager acts within a power grid allowing an intelligent load management.

    Functional Profile
        The Functional Profile describes a set of common functionalities that are exposed trough the generic
        SmartGridready interface used by the :term:`Communicator`. A SmartGridready compliant :term:`Product` supports one or
        more Functional Profiles. Examples for Functional Profiles are: 'EnergyMonitor` for electric energy measurement,
        'HeatCoolControl' for heat pumps or 'EVSE Load Reduction' for electrical vehicle charging stations.

    Functional Profiles
        Plural form of :term:`Functional Profile`

    PVA
         A system of interconnected solar panels that generate electricity from sunlight.

    Product
        A Product is a device serves the :term:`Communicator`. It exposes its functionalities through a
        proprietary interface. The SmartGridready :term:`CommHandler` allows the :term:`Communicator` to communicate
        with the Product through a generic interface, independent of the Product's proprietary implementation.

    SGCP
        Smart Grid Connection Point. A exposing an :term:`SGCP` allows load management by a power grid operator.


