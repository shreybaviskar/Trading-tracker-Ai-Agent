from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/")
async def test_route():
    return {"message": "Hello, World!"}
