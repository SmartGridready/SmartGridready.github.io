.. _introduction:

Introduction
============

Basic Concepts
--------------

The goal of SmartGridready is to ensure seamless interoperability between energy management devices, energy consuming,
energy producing and energy measuring devices, allowing an intelligent power management.

SmartGridready distinguishes between:

*   Controlled devices referred to as :term:`Product`

    Examples for :term:`Product` devices are smart-meters, heat pumps, :term:`EVSE` charging stations, term:`PVA` inverters.

*   Controlling devices referred to as :term:`Communicator`

    Examples for :term:`Communicator` devices are Energy Management Systems (:term:`EMS`) and :term:`Flexibility Manager`
    devices operated by power grid operators.

SmartGridready establishes a standardized framework to enable interoperability between system components, allowing
:term:`Communicator` devices to communicate with :term:`Product` devices in a unified, standardized manner,
independent of the :term:`Product` suppliers and their proprietary communication interfaces.

Interoperability is achieved by :term:`Functional Profile` definitions and :term:`External Interface Definition` (:term:`EID`)
files in XML that build the core of the SmartGridready specification.
The :term:`External Interface Definition` files define a set of :term:`Functional Profiles` exposed by a specific
:term:`Product` and the rules to adapt the communication from the generic SmartGridready interface to the proprietary
:term:`Product` interface.

Architecture
------------

:numref:`basic-architecture` illustrates the basic architecture of a SmartGridready environment.

.. _basic-architecture:
.. figure:: images/architecture.png
    :align: center
    :width: 56%

    Basic architecture

.. list-table:: Component descriptions
    :widths: 10 40
    :header-rows: 1

    *   - Component
        - Description

    *   - :term:`Flexibility Manager`
        - Acts as a load manager in a power grid. Allows flexible power management by communicating with Energy Managers :term:`EMS` within sub-networks, residential areas and buildings.

    *   - :term:`Communicator`
        - Part of the :term:`Flexibility Manager` or :term:`EMS` that communicates with :term:`Product` devices within the system. SmartGridready allows a communicator communicate with any :term:`Product` device through standardized interface.

    *   - :term:`Functional Profile`
        - The :term:`Functional Profile` defines a set of standardized functionalities exposed by a :term:`Product` device. The :term:`Functional Profile` forms the core of the SmartGridready standard, enabling flawless communication with any :term:`Product` device that conforms to the SmartGridready specification.

    *   - :term:`Energy Manager`
        - Acts as a power manager within a building. Provides a Smart Grid Connection Point :term:`SGCP` receiving commands from :term:`Flexibility Manager` devices.

    *   - Heat pump,

          :term:`PVA` inverter,

          :term:`EVSE` charging station

        - Samples for :term:`Product` devices

Further documentation
---------------------
`SmartGridready home page <https://smartgridready.ch/>`_

`SmartGridready GitHub projects home <https://github.com/SmartGridready>`_

.. toctree::
    :caption: Contents
    :maxdepth: 3