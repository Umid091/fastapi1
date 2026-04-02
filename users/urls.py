from fastapi import APIRouter
from fastapi import FastAPI,Request


router =APIRouter(prefix='/users')

@router.get('/')
async def sign_up():
    return {"message": 'signup'}

@router.get('/login')
async def sign_up():
    return {"message": 'login'}


@router.post('/data')
async def data_get(request: Request):
    data = await request.json()
    return data




