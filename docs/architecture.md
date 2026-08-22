# Day 1 — System Architecture

## Logical architecture

```text
                         +-----------------------+
                         |     HR Web Dashboard  |
                         +-----------+-----------+
                                     |
                         +-----------v-----------+
                         |       FastAPI         |
                         | Authentication / RBAC |
                         | Trip & Schedule APIs  |
                         | Event Processing      |
                         | Notifications         |
                         +-----+-----------+-----+
                               |           |
                 +-------------+           +----------------+
                 |                                        |
        +--------v---------+                      +---------v--------+
        |    PostgreSQL    |                      |    AI Services   |
        | Users            |                      | HR Assistant     |
        | Trips            |                      | Anomaly Detection|
        | Schedules        |                      | Delay Prediction |
        | Events           |                      +------------------+
        +------------------+
                 ^
                 |
        +--------+---------+
        |                  |
+-------+--------+  +------+---------+
| Driver App     |  | Employee Web  |
| Assigned trips |  | Schedule      |
| Arrived        |  | Trip status   |
| Depart         |  | Notifications |
| Complete       |  | Issue report  |
+----------------+  +----------------+

External services:
- Maps/geocoding/geofence provider for event-time verification
- Email/Teams/push notification provider
```

## Trip state machine

```text
SCHEDULED
   |
   v
DRIVER_ASSIGNED
   |
   v
ARRIVAL_PENDING
   |
   +---- invalid/missing ----> EXCEPTION
   |
   v
ARRIVED
   |
   v
DEPARTED
   |
   v
COMPLETED
```

## Key design decision: event-based GPS

The system does not stream driver coordinates continuously.

A location check happens only when the driver performs an event that requires physical verification, such as `Arrived at pickup`.

The backend validates the distance to the configured geofence and records a verification event. This gives HR an auditable event trail without continuous surveillance.

## Main components

### FastAPI backend
Owns authentication, authorization, schedules, trips, event validation, notifications, and reporting APIs.

### PostgreSQL
System of record for users, schedules, trips, event history, configurations, incidents, and analytics aggregates.

### Driver client
A mobile-friendly web/PWA can be used initially to avoid native-app overhead. Native Android can be introduced later if required for reliable background/device integration.

### Employee client
Responsive web application/PWA for schedules, trip status, notifications, and issue reporting.

### HR dashboard
Operational monitoring, exceptions, historical metrics, reports, and AI-assisted insights.

### AI service
Separated from the transactional API so AI failures cannot block core shuttle operations.

## Security principles
- RBAC: HR, Driver, Employee
- Short-lived authentication tokens/session controls
- Server-side authorization on every protected resource
- Secrets stored outside source code
- Audit trail for administrative changes
- Minimal location retention
- No AI access to data outside the user's authorization scope
