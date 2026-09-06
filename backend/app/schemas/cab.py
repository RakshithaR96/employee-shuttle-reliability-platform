from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CabCreate(BaseModel):
    registration_number: str = Field(
        min_length=3,
        max_length=30,
    )
    display_name: str = Field(
        min_length=1,
        max_length=80,
    )
    capacity: int = Field(
        default=4,
        ge=1,
        le=100,
    )


class CabResponse(BaseModel):
    id: int
    registration_number: str
    display_name: str
    capacity: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)