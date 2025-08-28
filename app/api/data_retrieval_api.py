from fastapi import APIRouter
from app.services.data_retrival.data_retrieval_service import DataRetrievalService

router = APIRouter(prefix="/tweets", tags=["tweets"])
retrieval_service = DataRetrievalService()


@router.get(
    "/antisemitic",
    response_description="List all tweets in antisemitic collection",
)
async def get_all_antisemitic():
    return await retrieval_service.retrieve_antisemitic()


@router.get(
    "/not-antisemitic",
    response_description="List all tweets in not antisemitic collection",
)
async def get_all_not_antisemitic():
    return await retrieval_service.retrieve_non_antisemitic()
