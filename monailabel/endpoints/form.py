from fastapi import APIRouter, Depends
from enum import Enum
from monailabel.endpoints.user.auth import RBAC, User
from monailabel.config import RBAC_ADMIN, RBAC_USER, settings
from pydantic import BaseModel

router = APIRouter(
    prefix="/form",
    tags=["Form"],
    responses={404: {"description": "Not found"}},
)

class Form(BaseModel):

    amniotic_fluid: str
    maternal_bladder: str
    fetal_head: str
    fetal_chest: str
    fetal_heart: str
    fetal_limb: str
    placenta: str
    umbilical_cord: str
    shadowing: str
    dropout: str
    gain: str
    deep: str
    shallow: str

@router.post("/")
async def submit_form(form: Form):
    user: User = Depends(RBAC(settings.MONAI_LABEL_AUTH_ROLE_ADMIN))
    return {"Form sent": form}

@router.get("/")
async def get_form(form: Form):
    user: User = Depends(RBAC(settings.MONAI_LABEL_AUTH_ROLE_ADMIN))
    return {"Form sent": form}