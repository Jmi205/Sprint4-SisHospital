from fastapi import APIRouter

from S4SisHospital.historiaClinica.views import historiasClinicas_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(historiasClinicas_view.router, prefix=historiasClinicas_view.ENDPOINT_NAME)