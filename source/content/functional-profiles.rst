.. _functional-profiles:

Functional Profiles
===================

A functional profile describes a set of related functionalities provided by a :term:`Product`.

The :term:`Functional Profiles` build the foundation of the SmartGridready specification and allow access to any
SmartGridready compliant :term:`Product` through a generic API.

Functional Profile Structure
----------------------------

In general, the :term:`Functional Profile` consists of a set of :term:`Datapoints` that provide read and write
operations related to the functionality.

A SmartGridready :term:`Product` exposes it's functionalities in a well structured way.

.. code-block:: none

   PRODUCT
   ├── COMMON PRODUCT INFO ...
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

The illustration above shows the structure of a :term:`External Interface Definition` XML (:term:`EID`) that exposes
its functionalities by including two :term:`Functional Profiles`. The example shows a simple :term:`Smart Meter`
that exposes AC-energy metering and AC-power measurement functionalities.

A :term:`Communicator` software can read from or write to the device by addressing the :term:`Datapoint` by
:term:`Functional Profile` name and :term:`Datapoint` name. Java code example:

.. code-block:: java

    var acPowerTotal = meteringDevice.getVal("ActiveEnergyAC", "ActiveEnergyACtot");

Available :term:`Functional Profiles`
-------------------------------------


The SmartGridready library lists the currently available :term:`Functional Profiles`:

`Functional Profile Library <https://library.smartgridready.ch/FunctionalProfileTemplate>`_

This list is subject to change and will grow in the future, as new :term:`Functional Profiles` will be added.

As a :term:`Product` supplier check which :term:`Functional Profiles` suit your product's functionalities and add
the matching :term:`Functional Profiles` to your :term:`External Interface Definition` file.



:term:`Functional Profile` Properties
-------------------------------------

The SmartGridready specification defines a set properties for :term:`Functional Profiles`:

* `Functional Profile Category <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/FunctionalProfileCategory.md>`_
* `Functional Profile Types <https://library.smartgridready.ch/FunctionalProfileTemplate>`_
* `Level of Operation <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/LevelOfOperation.md>`_


:term:`Datapoint` Properties
----------------------------

TODO

* reference detail doc.md's in Github (attributes, RW, 2m ...)

* reference functional profiles list in library


:term:`Functional Profile` Release Process
------------------------------------------

See `Functional Profile Release Process <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/functionalProfile_process.md>`_




Additional Documentation on GitHub
----------------------------------

`Functional Profile Documentation <https://github.com/SmartGridready/SGrSpecifications/blob/master/doc/functionalProfile.md>`_
