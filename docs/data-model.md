# Day 3 — Data Model

## Core entities

- **Employee** — employee identity and active status.
- **Driver** — driver/vendor identity and active status.
- **Cab** — vehicle identity, capacity, and active status.
- **Route** — pickup/destination coordinates and geofence configuration.
- **Schedule** — operational plan connecting route, cab, driver, direction, and timing rules.
- **Trip** — one concrete execution of a schedule on a service date.
- **TripEvent** — operational events such as check-in, arrival, departure, completion, GPS verification, and issue reporting.

## Privacy decision

There is deliberately no driver-location stream. A `TripEvent` may contain coordinates only when a location-sensitive event is explicitly recorded.

This allows the platform to verify events such as “cab arrived at the metro pickup point” without retaining a continuous trail of the driver's movements.

## AI readiness

Structured trip and event history can later support:

- delay prediction
- anomaly detection
- route reliability scoring
- recurring issue detection
- operational recommendations

The AI layer will consume historical operational events rather than requiring continuous surveillance.
