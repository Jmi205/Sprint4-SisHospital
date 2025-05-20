from fastapi import APIRouter, status, Body
import S4SisHospital.historiaClinica.logic.historiasClinicas_logic as historiasClincas_service
from models.models import HistoriaClinica, HistoriaClinicaOut, HistoriaClinicaCollection

router = APIRouter()
ENDPOINT_NAME = "/historiasClinicas"


@router.get(
    "/",
    response_description="List all Historias Clinicas",
    response_model=HistoriaClinicaCollection,
    status_code=status.HTTP_200_OK,
)
async def get_historiasClinicas():
    return await historiasClincas_service.get_historiasClinicas()


@router.get(
    "/{historiaClinica_id}",
    response_description="Get a single HIstoria Clinica by its id",
    response_model=HistoriaClinicaOut,
    status_code=status.HTTP_200_OK,
)
async def get_place(historiaClinica_id: str):
    return await historiasClincas_service.get_historiaClinica(historiaClinica_id)


@router.post(
    "/",
    response_description="Create a new historiaClinica",
    response_model= HistoriaClinicaOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_historiaClinica(historiaClinica: HistoriaClinica = Body(...)):
    return await historiasClincas_service.create_historiaClinica(historiaClinica)


@router.put(
    "/{historiaClinica_id}",
    response_description="Update a historiaClinica",
    response_model=HistoriaClinicaOut,
    status_code=status.HTTP_200_OK,
)
async def update_historiaClinica(historiaClinica_id: str, historiaClinica: HistoriaClinica = Body(...)):
    return await historiasClincas_service.update_historiaClinica(historiaClinica_id, historiaClinica)


@router.delete(
    "/{historiaClinica_id}",
    response_description="Delete a HistoriaClinica",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_historiaClinica(historiaClinica_id: str):
    return await historiasClincas_service.delete_historiaClinica(historiaClinica_id)
