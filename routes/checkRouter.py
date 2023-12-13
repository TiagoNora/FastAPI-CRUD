from fastapi import APIRouter

router = APIRouter(prefix='/check', tags=['CHECK'])

@router.get("/")
async def check():
    return {"status": "Está a funcionar!"}
