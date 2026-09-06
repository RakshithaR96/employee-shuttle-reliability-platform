from enum import StrEnum


class UserRole(StrEnum):
    EMPLOYEE = "employee"
    DRIVER = "driver"
    ADMIN = "admin"


class TripDirection(StrEnum):
    METRO_TO_OFFICE = "metro_to_office"
    OFFICE_TO_METRO = "office_to_metro"


class TripStatus(StrEnum):
    SCHEDULED = "scheduled"
    DRIVER_CHECKED_IN = "driver_checked_in"
    ARRIVED = "arrived"
    DEPARTED = "departed"
    COMPLETED = "completed"
    MISSED = "missed"
    CANCELLED = "cancelled"


class EventType(StrEnum):
    DRIVER_CHECKED_IN = "driver_checked_in"
    ARRIVED = "arrived"
    DEPARTED = "departed"
    COMPLETED = "completed"
    GPS_VERIFIED = "gps_verified"
    ISSUE_REPORTED = "issue_reported"
