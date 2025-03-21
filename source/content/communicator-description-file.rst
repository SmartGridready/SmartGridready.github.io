.. _communicator:

:term:`Communicator` Description File
=====================================

A :term:`Communicator` description file contains information about the :term:`Communicator` and the
:term:`Functional Profiles` that the :term:`Communicator` is able to control.

This allows to find matching products that can be used be the communicator.

General Structure
-----------------

The schema of the communicator interface description is structured on
two levels:
* Communicator information concerning manufacturer and product data, and the supported transport layers
* A list of supported functional profiles
* A list of data points with generic data types

The figure below shows the entity relation model of the communicator
interface description

.. figure:: images/communicator.drawio.png
   :alt: Communicator Entity Relation

   Communicator Entity Relation

Communicator Description File Elements
--------------------------------------

Release Notes
^^^^^^^^^^^^^

The release note section contains meta data that describe history and
current state of the communicator

+--------------------------------+--------------------------------------+
| Element                        | Description                          |
+================================+======================================+
| state                          | One of Draft, Review, Released,      |
|                                | Revoked                              |
+--------------------------------+--------------------------------------+
| remarks                        | Optional, arbitrary text. Can be     |
|                                | useful e.g. during draft phase.      |
+--------------------------------+--------------------------------------+
| changeLog                      | Optional, can occurs multiple times. |
|                                | Contains release notes to the        |
|                                | version concerned                    |
+--------------------------------+--------------------------------------+

Communicator Information
^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------+-----------------------------+
| Element                                | Description                 |
+========================================+=============================+
| Name                                   | Communicator Name           |
+----------------------------------------+-----------------------------+
| Manufacturer                           | Manufacturer                |
+----------------------------------------+-----------------------------+
| specOwnerId                            | Owner of the declaration    |
|                                        | (normally identical to      |
|                                        | manufacturer, but different |
|                                        | for 3rd party declarations) |
+----------------------------------------+-----------------------------+
| CommunicatorCategory                   | Communicator Category       |
+----------------------------------------+-----------------------------+
| SoftwareRevision                       | Software revision of        |
|                                        | communicator                |
+----------------------------------------+-----------------------------+

Communicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^

+---------------------------+--------------------------------------------+
| Element                   | Description                                |
+===========================+============================================+
| levelOfOperation          | Level of control defining the complexity   |
|                           | (see                                       |
|                           | LevelOfOperation :ref:`level_of_operation` |
|                           | ), and is defined by the highest level of  |
|                           | the communicator                           |
+---------------------------+--------------------------------------------+

Descriptions
^^^^^^^^^^^^

+-----------------------------------+-----------------------------------+
| Element                           | Description                       |
+===================================+===================================+
| alternativeNames                  | a list of relevant namespaces     |
|                                   | list for to display names used in |
|                                   | different standards like EEBUS,   |
|                                   | IEC6850,, SAREF4ENER etc. (see    |
|                                   | `Alternati                        |
|                                   | veNames <AlternativeNames.md>`__) |
+-----------------------------------+-----------------------------------+
| legibleDescription                | optional, can occur once per      |
|                                   | language. Contains details        |
|                                   | concerning the intended use case  |
|                                   | of the communicator.              |
+-----------------------------------+-----------------------------------+

Transport Services
^^^^^^^^^^^^^^^^^^

+-----------------------------------+-----------------------------------+
| Element                           | Description                       |
+===================================+===================================+
| supportedTransportServices        | Supported transport services (set |
|                                   | of Generic, Contacts, Modbus,     |
|                                   | RESTfulJSON)                      |
+-----------------------------------+-----------------------------------+

Functional Profiles
^^^^^^^^^^^^^^^^^^^

Each communicator contains a list of functional profiles.

.. list-table::
    :widths: 30 70

    * - Element
      - Descriptions
    * - profileName
      - Instance name of the specified functional profile, containing Release Notes, Classification,
        Description.
    * - functionalProfile
      - Copy of the standardized
    * - programmerHints
      - Optional, Optional, can occur multiple times once per language. Contains details
        for the programmer.