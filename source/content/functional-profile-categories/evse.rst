.. _evse:

:term:`EVSE`
------------


Electric Vehicle Supply Equipment (:term:`EVSE`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, there are three types of :term:`Functional Profiles` for the :term:`EVSE`

- :ref:`evse_current_limit` : Enables a controller to set a current limitation for an :term:`EVSE`.
- :ref:`evse_state` : Reads the status of the connector of an :term:`EVSE`
- :ref:`evse_load_reduction` : Sets the operation mode of the :term:`EVSE`.

.. _evse_current_limit:

:term:`EVSE` Current Limit
^^^^^^^^^^^^^^^^^^^^^^^^^^

The functional profile enables a controller to set a current limitation
for an Electric Vehicle Supply Equipment (:term:`EVSE`).

The charging station’s current limit is dynamically regulated by an
external Energy Management System (:term:`EMS`), with the data point
EMSCurrentLimit expressed in amps. This data point enables real-time
monitoring and control of the consumption limit of the charging station.
This specific parameter is designed to be easily adjusted by an Energy
Manager, allowing for efficient and tailored control of the charging
process.

This functional profile can be utilized in conjunction with the :ref:`evse_state` functional profile.



Main Data Points
^^^^^^^^^^^^^^^^

The functional profile covers the following main data points

- **EMSCurrentLimit** (mandatory): The maximum current allowed for the
  charging station at this moment.
- **SafeCurrent** (recommended): In the event of a communication
  interruption with the :term:`EMS`, the :term:`EVSE` automatically adjusts its current
  limit to the Safe Current value.
- **MaxReceiveTimeSec** (recommended): The MaxReceiveTimeSec datapoint
  signifies the timeout for the stability fallback. If the :term:`EVSE` does not
  receive communication within the specified MaxReceiveTimeSec, it will
  automatically limit the current to the SafeCurrent value.
- **HWCurrentLimit** (optional): The maximum current allowed for the
  EVSE is determined by the electrical installation of the charging
  station and cannot be changed during operation.

Feedback Sub Data Points
^^^^^^^^^^^^^^^^^^^^^^^^

If the controller requires different datapoints to write and read the
values EMSCurrentLimit, SafeCurrent, and MaxReceiveTimeSec, the data
direction of can be changed from RW to W and an additional sub data
point Feedback can be used to read the current value

- EMSCurrentLimit.Feedback for EMSCurrentLimit
- SafeCurrent.Feedback for SafeCurrent
- MaxReceiveTimeSec.Feedback for MaxReceiveTimeSec

These sub data points should not be used if the controller sets and
reads the value from the same data point.

SmoothTransition Sub Data Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :ref:`smooth_transition` sub
data points are utilized to specify the transition process following the
reception of a new value for the data points EMSCurrentLimit and
SafeCurrent. The transition process is defined with three sub data
points for both main data points

- SmoothTransition_Window: Indicates a time window in which the new
  operating mode is started randomly. The time window begins with the
  start command of the operating mode. The value 0 means immediate (see
  winTms :ref:`smooth_transition`.
- SmoothTransition_Delay: Specifies how quickly the changes should be
  made. The corresponding value is gradually changed from the old to the
  new value in the specified time. (see rmpTms
  :ref:`smooth_transition`).
- SmoothTransition_Duration: Determines how long the operating mode
  should be active. When the time has elapsed, the operating mode is
  automatically terminated. If set to 0 (standard value), the operating
  mode remains active until a new command is received. (see rvrtTms
  :ref:`smooth_transition`).

Accordingly, the sub data points

- for EMSCurrentLimit are

  - EMSCurrentLimit.SmoothTransition_Window
  - EMSCurrentLimit.SmoothTransition_Delay
  - EMSCurrentLimit.SmoothTransition_Duration

- for SafeCurrent are

  - SafeCurrent.SmoothTransition_Window
  - SafeCurrent.SmoothTransition_Delay
  - SafeCurrent.SmoothTransition_Duration

All six sub data point can be implemented in the device as constant data
points if the value is constant or as regular datapoint if it can be
read from the device.

.. _evse_state:

:term:`EVSE` State
^^^^^^^^^^^^^^^^^^

Functional profile for reading the status of the connector of an
electric vehicle charging station (:term:`EVSE`).

The current state of the wallbox can be read using the data point
ocppState with following values corresponding to the OCPP standard (Open
Charge Point Protocol):

- **AVAILABLE**: The charge point is operational and available for a new
  customer to start a charging session.
- **CHARGING**: A vehicle is currently charging.
- **PREPARING**: The charge point is preparing for a charging session
  after the driver has been authorized.
- **FINISHING**: The charging process is being concluded (e.g., the
  vehicle has reached a full charge and the session is being
  terminated).
- **RESERVED**: The charge point has been reserved for a particular EV
  driver and is not available to other users.
- **UNAVAILABLE**: The charge point is not in operation and cannot be
  used to charge a vehicle.
- **FAULTED**: There is a fault in the charge point, requiring
  maintenance or repair.
- **SUSPENDED_EV_SE**: The charging process has been suspended due to
  some hardware limitations of the Electric Vehicle Supply Equipment
  (:term:`EVSE`).
- **SUSPENDED_EV**: The charging process has been suspended due to some
  conditions on the vehicle side.

The status of the connector indicates, for example, whether a car is
connected to the charging station, if it is currently charging, or if
the connector is not connected to the electric vehicle. The function
profile refers to the states offered by the OCPP 1.6 protocol under
ocppState.

Knowing the status of the charging station allows an external controller
to influence the charging of the car, for example, through the
EMS_Current_Limit functional profile. reserved for a particular EV
driver and is not available to other users.

.. _evse_load_reduction:

:term:`EVSE` LoadReduction
^^^^^^^^^^^^^^^^^^^^^^^^^^

The LoadReduction functional profile sets the operation mode of the
:term:`EVSE`. Depending on the equipment of the controller one of the following
functional profiles apply

- SGr level of operation 1 - controllers with one switch with the
  switching states

  - Switching state **0**: Normal operation, charging according to the
    configured connection power without any restrictions.
  - Switching state **1**: Minimum charging (AC charging at 6 A, DC
    charging at 10 kW).

- SGr level of operation 2 - controllers with two switches with the
  switching states

  - Switching state **0,0**: Normal operation, charging according to the
    configured connection power without any restrictions.
  - Switching state **0,1**: Reduced charging (e.g. 50 % of the maximum
    charging power, but never below 6 A).
  - Switching state **1,0**: Minimum charging (e.g. AC charging at 6 A,
    DC charging at 10 kW).
  - Switching state **1,1**: Charging paused (if bidirectional charging
    is supported maximum feed-in for Vehicle to Infrastructure V2X).

- SGr level of operation 2m - controllers with the operating states
  (states can be set and optionally be read)

  - **EV_NORMAL**: Normal operation, charging without any restrictions
    based on the configured connection power.
  - **EV_REDUCED**: Reduces charging (e.g. to 50 % of the maximum
    charging power, but not below 6 A).
  - **EV_NONE_OR_FEEDIN**: Charging interrupted (if bidirectional
    charging is supported maximum feed-in for vehicle to infrastructure
    V2X).
  - **EV_MINIMAL**: Minimum charging (e.g. AC charging at 6 A, DC
    charging at 10 kW).


.. raw:: html

    <a href="../functional-profiles.html#functional-profile-category" class="btn btn-neutral float-left">
        <span class="fa fa-arrow-circle-left" aria-hidden="true"></span>
        Back to Functional Profile Categories
    <a>
    <p>

.. toctree::
    :caption: Contents
    :maxdepth: 3