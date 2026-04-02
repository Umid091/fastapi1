from fastapi import APIRouter

router =APIRouter(prefix='/auth')

@router.get('/')
async def sign_up():
    return {"message": 'signup'}

@router.get('/login')
async def sign_up():
    return {"message": 'login'}