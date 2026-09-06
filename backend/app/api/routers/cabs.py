from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.cab import Cab
from app.schemas.cab import CabCreate, CabResponse


router = APIRouter(
    prefix="/cabs",
    tags=["Cabs"],
)


@router.post(
    "",
    response_model=CabResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_cab(
    payload: CabCreate,
    db: Session = Depends(get_db),
) -> Cab:
    cab = Cab(
        registration_number=payload.registration_number,
        display_name=payload.display_name,
        capacity=payload.capacity,
    )

    db.add(cab)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A cab with this registration number already exists.",
        )

    db.refresh(cab)
    return cab


@router.get(
    "",
    response_model=list[CabResponse],
)
def list_cabs(
    db: Session = Depends(get_db),
) -> list[Cab]:
    statement = select(Cab).order_by(Cab.id)
    return list(db.scalars(statement).all())


@router.get(
    "/{cab_id}",
    response_model=CabResponse,
)
def get_cab(
    cab_id: int,
    db: Session = Depends(get_db),
) -> Cab:
    cab = db.get(Cab, cab_id)

    if cab is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cab not found.",
        )

    return cab