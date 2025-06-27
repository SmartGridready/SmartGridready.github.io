.. _sgcp:

SGCP
----

The ***Smart Grid Connection Point** (:term:`SGCP`) :ref:`functional_profile_category` is used within devices
that allow a Distribution System Operator :term:`DSO` gather information and control the power consumption
within their network.

The :term:`SGCP` is a crucial component within a the smart grid (or network) to intelligently
monitor and manage the generation, distribution, and consumption of electricity.

It allows a power grid operators (:term:`DSO`) managing the power consumption dynamically in response to
supply and load conditions, as described in the following example:

 1. The :term:`DSO`/:term:`TSO` (grid operator) detects:

    * High demand
    * Grid instability
    * Supply shortage (e.g., low renewable power generation)

2. The :term:`Flexibility Manager` system of the :term:`DSO` sends signal to:

   * Network Aggregators
   * Directly to Energy Management Systems (:term:`EMS`)

   Communication is done over a smart grid communication network.

3. The aggregator or consumer :term:`EMS`:

   * Evaluates the demand/response request e.g. curtail load, shift usage
   * Decides what actions to take based on:

        * Contracts
        * User preferences
        * Current load and device status

4. The local systems automatically:
    * Turn off or reduce heating, air conditioning, water heaters, EV charging, etc.
    * Shift operation of devices (e.g., delay a washing machine)
    * Possibly export energy from home batteries or solar systems

5. :term:`Smart Meter` or term:`EMS` report to :term:`DSO` and Aggregators:

    * Actual load reduction
    * Timestamped consumption data

6. Based on verified reductions, the participant receives:
    * Financial rewards
    * Bill credits
    * Other incentives


The following chapters describe the SmartGridready :term:`Functional Profiles` assiciated with the **SGCP**
:ref:`functional_profile_category`, which is primarily provided by :term:`EMS` devices:


Unidirectional :term:`Functional Profiles`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unidirectional :term:`Functional Profiles` allow control the device operation mode in just one direction, either
the power consumption of the consumer from the network or the power feed of the 'prosumer' towards the network.

The related :term:`Functional Profiles` are:
* **UniDirFlexLoadMgmt** - allows controlling the power consumption of a power consumer.
* **UniDirFlexFeedInMgmt** - allows controlling the power feed limits towards the power network/grid.


Bidirectional :term:`Functional Profiles`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bidirectional :term:`Functional Profiles` allow controlling the power consumption from and the power feed into the
network.

Functional profiles are:
* **FlexMgmt** - allows controlling the power power consumption AND the power feed in limits.


:ref:`level_of_operation` 2/2m
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :ref:`level_of_operation` 2/2m allow power control by setting the operation mode through 2 digital inputs
(e.g. two relay contacts). The 4 possible operation modes depend on the :term:`Functional Profile`:

* :ref:`level_of_operation` 2: operation mode can only be set.
* :ref:`level_of_operation` 2m: current operation mode can be read back.

.. list-table:: **UniDirFlexLoadMgmt 2/2m Operation Modes**
    :header-rows: 0
    :widths: 20 80

    * - NORMAL
      - In normal operation, the load management optimizes power consumption according to the user's criteria, within
        the permitted power range.
    * - REDUCED
      - In reduced operation, the power consumption is decreased by an agreed percentage (curtailment), if possible.
    * - MAX
      - In maximum operation, the load management allows for maximum power consumption.
    * - LOCKED
      - In the 'locked' operating mode, either no energy or only a defined minimum amount (minLoad) may be drawn from t
        he grid. This can be achieved by reducing power consumption for a maximum duration (maxLockTimeMinutes).

.. list-table:: **UniDirFlexFeedInMgmt 2/2m Operation Modes**
    :header-rows: 0
    :widths: 20 80

    * - NORMAL
      - In normal operation, the load management optimizes the power feed in according the user's criteria.
    * - REDUCED
      - The feed-in power is reduced by an agreed percentage (curtailment), if possible.
    * - MAX
      - The load management allows maximum power feed-in.
    * - LOCKED
      - In this operating mode, either no energy or only a defined minimum amount (minLoad) may be fed into the grid.
        This can be achieved by curtailing generation or disabling battery discharge for a maximum duration
        (maxLockTimeMinutes).

.. list-table:: **FLexMgmt 2/2m Operation Modes**
    :header-rows: 0
    :widths: 20 80

    * - NORMAL
      - No restrictions by the :term:`DSO` power consumption or feed-in according the user's criteria.
    * - MAX_LOAD
      - In maximum operation, the load management allows for maximum power consumption.
    * - MAX_FEEDIN
      - The load management allows maximum power feed-in.
    * - LOCKED
      - In this operation mode power consumption or power feed-in is zero or limited to a minimum amount (minLoad).

:ref:`level_of_operation` 4/4m
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:term:`Functional Profiles` at :ref:`level_of_operation` 4/4m enable fine-grained control of power consumption and/or
feed-in management. They support the configuration of continuous limitation values for both power consumption and/or
feed-in. Additionally, they may allow the definition of time-based limits to be applied during specific periods.

:ref:`level_of_operation` 4m :term:`Functional Profiles` also support reading back current configuration settings
and provide metrics on present operating values.



.. raw:: html

    <a href="../functional-profiles.html#functional-profile-category" class="btn btn-neutral float-left">
        <span class="fa fa-arrow-circle-left" aria-hidden="true"></span>
        Back to Functional Profile Categories
    <a>
    <p>

.. toctree::
    :caption: Contents
    :maxdepth: 3