# Day 1 — Product Requirements

## 1. Problem
Employees report that shuttle cabs sometimes arrive late, leave early, or do not arrive. The current proposed solution—continuous driver live-location sharing—improves visibility but does not provide strong scheduling controls, exception handling, or accountability and raises unnecessary privacy concerns.

## 2. Product objective
Build a privacy-preserving shuttle reliability platform that records the important trip events, detects exceptions automatically, and communicates useful status to employees and HR without continuously tracking drivers.

## 3. Users
### HR / Transport Admin
- Configure routes, stops, cabs, drivers, and schedules
- View active/upcoming trips
- Receive exception alerts
- Review trip history and reliability metrics
- Export reports

### Driver
- View assigned trips
- Check in at pickup location
- Confirm departure when allowed
- Complete trip
- Report operational issues

### Employee
- View today's shuttle schedule
- See confirmed trip status
- Receive arrival/delay notifications
- Report a missed/incorrect shuttle

## 4. Core workflow
1. HR creates a scheduled trip.
2. Driver receives the assigned trip.
3. Driver reaches the pickup zone and taps `Arrived`.
4. Backend performs a one-time GPS/geofence verification.
5. Arrival event is timestamped.
6. Driver can depart only inside the configured departure window.
7. Employees receive the relevant status notification.
8. Driver completes the trip.
9. Backend evaluates punctuality and exceptions.
10. Data becomes available for HR analytics and AI analysis.

## 5. Privacy requirements
- No continuous driver location tracking in MVP.
- GPS is requested only for configured verification events.
- Store the minimum location data necessary for audit/reliability.
- Role-based access to trip and driver data.
- Audit sensitive actions.

## 6. Reliability rules
The system should detect:
- Early departure
- Late arrival
- Missed pickup
- Missing driver check-in
- Trip not started
- Trip not completed
- Repeated driver/trip anomalies

Example configurable rule:
- Scheduled departure: 08:30
- Earliest permitted departure: 08:28
- Grace period: 2 minutes
- If no arrival check-in by 08:25, create a warning.
- If no valid arrival/departure by the escalation threshold, alert HR.

## 7. Notifications
Employee notifications:
- Trip confirmed
- Cab arrived
- Delay detected
- Trip cancelled

HR notifications:
- Driver has not checked in
- Early departure attempt
- Missed pickup
- Significant delay

## 8. AI features — phased
### MVP+ / Phase 2
- Natural-language HR assistant over authorized operational data
- Weekly reliability summaries
- Anomaly explanations

### Later
- Delay probability prediction from historical trip data
- Forecasting by route/day/time

AI must not make safety-critical or disciplinary decisions automatically.

## 9. Success metrics
- On-time departure percentage
- On-time arrival percentage
- Missed-trip percentage
- Average delay
- Early-departure count
- Driver check-in compliance
- Employee-reported incidents
- Notification delivery success

## 10. Non-goals for MVP
- Continuous GPS tracking
- Passenger facial recognition
- Driver surveillance outside trips
- Complex fleet management
- Payment/billing
- Public ride booking
