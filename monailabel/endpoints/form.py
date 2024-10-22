from fastapi import APIRouter
import logging
from pydantic import BaseModel
from monailabel.interfaces.utils.app import app_instance
from monailabel.interfaces.app import MONAILabelApp

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/form",
    tags=["Form"],
    responses={404: {"description": "Not found"}},
)

class Form(BaseModel):
    image_id: str
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
    

def save_form(form):
    instance: MONAILabelApp = app_instance()
    return instance.datastore().save_form(form)

    
@router.post("/")
async def api_save_form(data: Form):
    form = dict(data)
    return save_form(form)