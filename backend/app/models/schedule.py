from datetime import datetime, timezone, time

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)
    route_id: Mapped[int] = mapped_column(ForeignKey("routes.id"), index=True)
    cab_id: Mapped[int] = mapped_column(ForeignKey("cabs.id"), index=True)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.id"), index=True)
    direction: Mapped[str] = mapped_column(String(40))
    scheduled_departure: Mapped[time] = mapped_column(Time)
    early_departure_tolerance_minutes: Mapped[int] = mapped_column(Integer, default=2)
    late_checkin_threshold_minutes: Mapped[int] = mapped_column(Integer, default=5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
