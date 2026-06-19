.. _openapi-specifications:

OpenAPI Specifications
====================================================

:ref:`Target audience : <table-1>` |dev|

SmartGridready OpenAPI specifications provide standardized, machine readable descriptions of REST interfaces for selected use cases. They are based on established industry standards or defined SmartGridready models and facilitate consistent, interoperable integration across different systems and market participants.

The following sections describe the available OpenAPI specifications per use case.



Dynamic Tariffs
---------------

The :term:`VSE` has published a `handbook <https://www.strom.ch/de/shop/dynamische-netznutzungstarife-im-verteilnetz-hdn-ch-2025>`_ that establishes a common technical and conceptual foundation for dynamic network tariffs in distribution grids.

SmartGridready provides a corresponding OpenAPI specification that translates these requirements into a standardized REST interface definition.
The specification defines how dynamic tariff data must be structured, time referenced and published in a machine-readable format.
The provided specification can be used as template to implement the actual API.

.. note::
    The currently published specification is Version 1 (valid for 2026). The handbook is being revised by the VSE working group *Dynamische Netznutzungstarife im Verteilnetz*. The new version will be published in the course of 2026, coming into effect on 1 January 2027.


**Access the specification**

* View the current OpenAPI specification for dynamic tariffs (Version 1, valid for 2026) in `Swagger UI V1 <../_static/swagger/dynamic-tariff-v1.html>`_
* View the upcoming OpenAPI specification for dynamic tariffs (Version 2, valid for 2027) in `Swagger UI V2 <../_static/swagger/dynamic-tariff-v2.html>`_
* Download the OpenAPI specification and JSON schemas on `Github <https://github.com/SmartGridready/SGrSpecifications/tree/master/DynamicTariff>`_


.. toctree::
    :caption: Contents
    :maxdepth: 3