.. _battery:

Battery
-------

The :ref:`functional_profile_category` **Battery** refers to energy storage systems (ESS), such as home
batteries or industrial battery banks, that are designed to interact intelligently with the electrical
grid. These products are capable not only of storing and supplying power, but also of participating
in energy management services controlled by an :term:`EMS`. The :term:`EMS` manages efficient energy
consumption and coordinates energy supply to the distribution network (:term:`DSO`).

Devices of the **Battery** :ref:`functional_profile_category` support the **EnergyMonitor**
:ref:`functional_profile_type` that allow the :term:`EMS` to read characteristic values from the **Battery**:

* maximum capacity
* available energy
* active DC power consumption
* consumption of energy during the night
* SoC, state of charge in percent
* SoH, state of health

and control the **Battery** status:

* maximum discharge limit within a period of time
* maximum charge limit within a given period of time
* operation mode for charging

.. raw:: html

    <a href="../functional-profiles.html#functional-profile-category" class="btn btn-neutral float-left">
        <span class="fa fa-arrow-circle-left" aria-hidden="true"></span>
        Back to Functional Profile Categories
    <a>
    <p>

.. toctree::
    :caption: Contents
    :maxdepth: 3