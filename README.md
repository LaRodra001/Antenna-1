# Antenna Trilateration System

A distributed positioning system designed to estimate the location of a device using **trilateration and multiple independent antennas**, each hosted on its own server.

## Mathematical Foundation

Trilateration estimates a position using distances from known reference points.

For an antenna at position \((x_i,y_i)\), with measured distance \(r_i\) to a device at \((x,y)\), the ideal distance equation is:

\[
(x-x_i)^2+(y-y_i)^2=r_i^2
\]

With at least three suitably positioned antennas, the system can estimate a two-dimensional position. Additional antennas can improve robustness when their measurements are combined using an appropriate estimation method.

## Architecture

The system follows a distributed architecture:

- **Antenna servers:** Independent endpoints that expose antenna status and positioning data.
- **Positioning client:** Communicates with the antennas and collects their measurements.
- **Trilateration engine:** Processes the measurements and estimates the device's coordinates.
- **Visualization layer:** Displays the antennas, distance circles, and estimated device position.

Each antenna is independently deployable, making the architecture modular and easier to expand.

---

*Developed by LaRodra001_*