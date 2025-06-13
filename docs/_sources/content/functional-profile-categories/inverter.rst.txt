.. _inverter:

Inverter
--------

General Description
^^^^^^^^^^^^^^^^^^^

The :ref:`functional_profile_category` **Inverter** is used for devices that convert direct current (DC) as
produced by a photovoltaic array (:term:`PVA`) or a :ref:`battery` into a utility frequency alternating current (AC)
that can be fed into a commercial electrical grid or used be a local, off-grid electrical network. It is a critical
system component in a photovoltaic system, allowing the use of ordinary AC-powered equipment.

:term:`PV-Inverter` have special functions adapted for use with photovoltaic arrays, including maximum power
point tracking and anti-islanding protection.

:ref:`battery`  backup inverters are special inverters which are designed to draw energy from a battery, manage
the battery charge via an onboard charger, and export excess energy to the utility grid. These inverters are capable
of supplying AC energy to selected loads during a utility outage.

SmartGridready provides an **Inverter** :term:`Functional Profile` that allows :term:`Modbus` communication with
the :term:`Product` device based on the **SunSpec** specification.

SunSpec
^^^^^^^

The current :term:`Functional Profile` targets :term:`Modbus` devices that are SunSpec compliant. The Modbus SunSpec
Specification defines a standardized way to communicate with and monitor solar and energy systems using the Modbus
protocol. It is published by the SunSpec Alliance, an industry consortium that promotes interoperability among
distributed energy components.

See also `SunSpec home <https://sunspec.org>`_.


Maximum Power Point Tracking (MPPT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function ensures the inverter continuously adjusts the electrical operating point of the panels to extract
the most possible power at any moment, depending on light and temperature conditions.

Anti-Islanding Protection
^^^^^^^^^^^^^^^^^^^^^^^^^

This safety feature prevents the inverter from feeding electricity into the grid when the grid is down (e.g., during a
power outage). This is critical to protect line workers and equipment.


.. raw:: html

    <a href="../functional-profiles.html#functional-profile-category" class="btn btn-neutral float-left">
        <span class="fa fa-arrow-circle-left" aria-hidden="true"></span>
        Back to Functional Profile Categories
    <a>
    <p>

.. toctree::
    :caption: Contents
    :maxdepth: 3