.. _device-information:

Device Information
------------------

The functional :ref:`functional_profile_category` **DeviceInformation** is associated with the
:ref:`functional_profile_type` of the same name: **DeviceInformation**.

Currently there are two :term:`Functional Profiles` that use the :ref:`functional_profile_category`
**DeviceInformation**.

* :ref:`functional_profile_type` **DeviceInformation** : Provides reading of the 'Device Identifier'
* :ref:`functional_profile_type` **DynamicTariff**     : Provides reading of dynamic tariffs from the
  network system operator (:term:`DSO`).

.. TODO DeviceInformation is used as
   - functional profile category (does this really make sense to have a category for that).
   - functional profile type ...
   - as device category
   - Currently functional profile type is not an enum, it's free text. Is this really intended.
     What about making the functional profile type an enum that includes a well defined
     set of mandatory and optional data points?


.. raw:: html

    <a href="../functional-profiles.html#functional-profile-category" class="btn btn-neutral float-left">
        <span class="fa fa-arrow-circle-left" aria-hidden="true"></span>
        Back to Functional Profile Categories
    <a>
    <p>

.. toctree::
    :caption: Contents
    :maxdepth: 3