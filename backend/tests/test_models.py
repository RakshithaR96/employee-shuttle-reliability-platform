from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session

from app.db.base import Base
from app.models import Cab, Driver, Employee, Route, TripEvent


def test_expected_tables_exist() -> None:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    table_names = set(inspect(engine).get_table_names())

    assert {
        "employees",
        "drivers",
        "cabs",
        "routes",
        "schedules",
        "trips",
        "trip_events",
    }.issubset(table_names)


def test_core_records_can_be_persisted() -> None:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        employee = Employee(
            employee_code="E001",
            name="Test Employee",
            email="test@example.com",
        )
        driver = Driver(name="Test Driver", phone="9999999999")
        cab = Cab(registration_number="KA01TEST", display_name="Cab 1")
        route = Route(
            name="Metro to Office",
            pickup_name="Metro Station",
            pickup_latitude=12.0,
            pickup_longitude=77.0,
            destination_name="Office",
            destination_latitude=12.1,
            destination_longitude=77.1,
        )

        session.add_all([employee, driver, cab, route])
        session.commit()

        assert employee.id is not None
        assert driver.id is not None
        assert cab.id is not None
        assert route.id is not None
