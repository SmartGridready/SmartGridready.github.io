.. _home:

Documentation Overview
======================

Welcome to the SmartGridready documentation! This guide provides a comprehensive overview of the SmartGridready ecosystem, its concepts, and available resources. The documentation is organized into chapters, each tailored to specific audiences such as planners, suppliers, grid operators, and developers.

.. note::
   Each chapter in the documentation is labeled with icons representing the intended target audience. Refer to **Table 1** below for an explanation of these icons. This will help you quickly identify the sections most relevant to your interests and needs.

.. |planner| replace:: 🧑‍💼
.. |supplier| replace:: 🏭
.. |grid| replace:: ⚡
.. |dev| replace:: 🧑‍💻


.. list-table:: Target audience icon explanation
    :name: table-1

    * - Symbol
      - Description
    * - |planner|
      - Planners & Architects
    * - |supplier|
      - :term:`Product` and :term:`Communicator` suppliers
    * - |grid|
      - Power Grid Operators
    * - |dev|
      - Developers (Communicator devices, SGr libraries)


To help you navigate the documentation, the following overview **Table 2** lists all main chapters, describes their content, and shows which target audiences each chapter is intended for using the icons explained above. Use this table to quickly find the sections most relevant to your needs.

.. list-table:: Documentation Overview
    :header-rows: 1
    :widths: 30 40 30

    *   - Chapter
        - Description
        - Target Audience

    *   - :ref:`introduction`
        - Describes the basic idea and concepts of SmartGridready.
        - |planner| |supplier| |grid| |dev|

    *   - :ref:`getting-involved`
        - There are many ways to get involved and contribute to the SmartGridready project.
          This chapter describes how you can participate in SmartGridready projects based on your interests and expertise.
        - |planner| |supplier| |grid| |dev|

    *   - :ref:`functional-profiles`
        - Explains the central role of :term:`Functional Profiles` in SmartGridready.
          Describes the :term:`Functional Profiles` in detail.

          .. raw:: html

             <br>

          Provides a link to the official SmartGridready library where all available :term:`Functional Profiles`
          are listed.

        - |planner| |supplier| |grid| |dev|

    *   - :ref:`product-description-eid`
        - Describes the structure of :term:`External Interface Definition` files.
          Gives instructions on how to create an :term:`EID` file.

          .. raw:: html

             <br>

          Provides a link to the official SmartGridready libary where all available :term:`Functional Profiles`
          are listed.

        - |planner| |supplier| |grid| |dev|

    *   - :ref:`sgr-declaration`
        - Guides you through the steps needed to get your :term:`Product` SmartGridready declared.
        - |supplier| |grid| |dev|

    *   - :ref:`commhandler-libraries`
        - Describes the :term:`Communication Handler` libraries and API's in detail. Provides installation and getting started instructions. There are currently libraries in Python and Java.
        - |dev|

    *   - :ref:`device-driver-libraries`
        - Describes the :term:`Device Driver Adapter` and the device driver adapter API in detail.
        - |dev|

    *   - :ref:`intermediary`
        - Describes the SmartGridready :term:`Intermediary`. The intermediary provides a REST service to communicate
          with SmartGridready declared :term:`Products` through a REST API. It can be deployed within a Docker container
          and is a good solution where no native library (Python, Java) is available.
        - |dev|

    *   - :ref:`openapi-specifications`
        - Provides OpenAPI specification templates for selected SmartGridready use cases.
          These specifications define standardized REST interfaces and machine-readable data models that support interoperable integration of services such as dynamic tariff APIs.
        - |dev|
