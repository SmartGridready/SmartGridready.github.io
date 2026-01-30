.. _home:

Documentation Overview
======================

.. list-table:: Target audience icon explanation

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


The following table gives you a documentation overview and the targeted audience for each section.

.. list-table:: Documentation Overview
    :header-rows: 1
    :widths: 30 40 30

    *   - Chapter
        - Description
        - Target Audience

    *   - :ref:`introduction`
        - Describes the basic idea and concepts of SmartGridready.
        - * |planner| |supplier| |grid| |dev| Everybody

    *   - :ref:`getting-involved`
        - There are many ways to get involved and contribute to the SmartGridready project.
          This chapter describes how you can participate in SmartGridready projects based on your interests and expertise.
        - * Everybody

    *   - :ref:`functional-profiles`
        - Explains the central role of :term:`Functional Profiles` in SmartGridready.
          Describes the :term:`Functional Profiles` in detail.

          .. raw:: html

             <br>

          Provides a link to the official SmartGridready library where all available :term:`Functional Profiles`
          are listed.

        -
          * :term:`Product` Suppliers
          * :term:`Communicator` Suppliers
          * Architects and Planners
          * Network Operators
          * All Developers

    *   - :ref:`product-description-eid`
        - Describes the structure of :term:`External Interface Definition` files.
          Gives instructions on how to create an :term:`EID` file.

          .. raw:: html

             <br>

          Provides a link to the official SmartGridready libary where all available :term:`Functional Profiles`
          are listed.

        - * Architects and Planners
          * Network Operators
          * :term:`Product` Suppliers
          * :term:`Communication Handler` Library Developers

    *   - :ref:`sgr-declaration`
        - Guides you through the steps needed to get your :term:`Product` SmartGridready declared.
        - * :term:`Product` Suppliers
          * :term:`Communicator` Suppliers
          * Architects and Planners

    *   - :ref:`commhandler-libraries`
        - Describes the :term:`Communication Handler` libraries and API's in detail. Provides installation and getting started instructions. There are currently libraries in Python and Java.
        - * :term:`Communication Handler` Developers
          * :term:`Communicator` Developers

    *   - :ref:`device-driver-libraries`
        - Describes the :term:`Device Driver Adapter` and the device driver adapter API in detail.
        - * :term:`Product` Suppliers
          * :term:`Communication Handler` Developers

    *   - :ref:`intermediary`
        - Describes the SmartGridready :term:`Intermediary`. The intermediary provides a REST service to communicate
          with SmartGridready declared :term:`Products` through a REST API. It can be deployed within a Docker container
          and is a good solution where no native library (Python, Java) is available.
        - * :term:`Communicator` Suppliers
          * :term:`Communicator` Developers

