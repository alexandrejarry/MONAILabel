from fastapi import APIRouter
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

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
    gain_issue: str
    deep_zoom_issue: str
    shallow_zoom_issue: str

@router.post("/form")
async def save_form(form: Form):
    return form