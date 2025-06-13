.. _dynamic-tariff:

Dynamic Tariff
--------------

The dynamic tariff allows an :term:`EMS` to read a list of tariffs that vary over short time intervals (e.g., 15 minutes)
provided by a distribution system operator (:term:`DSO`).

This enables an :term:`EMS` to manage connected electricity consumers by adjusting their power consumption or supply
based on the current short-term tariff. For example, a boiler can be heated when the tariff is low, while a battery
can be discharged during periods of high tariffs.

The :ref:`functional_profile_type` for the **Dynamic Tariff** connection point is **Supplier**. In most cases,
the **Supplier** is a distribution system operator (:term:`DSO`), which publishes the tariffs through a web service API.

The API includes the definition for the requested interval (start and end time) for the list of tariffs. The list of tariffs
is provided to the :term:`EMS` in a JSON format defined by the :term:`Functional Profile`.


.. raw:: html

    <a href="../functional-profiles.html#functional-profile-category" class="btn btn-neutral float-left">
        <span class="fa fa-arrow-circle-left" aria-hidden="true"></span>
        Back to Functional Profile Categories
    <a>
    <p>

.. toctree::
    :caption: Contents
    :maxdepth: 3