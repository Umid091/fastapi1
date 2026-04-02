from email.policy import default

from fastapi import APIRouter,Request

router =APIRouter(prefix='/products')


@router.get('/')
async def products_list():
    return {'mevalar': 'olma, anor'}

@router.get('/test')
async def products_list():
    return {'test': 'test'}

@router.post('age')
async def get_age(request: Request ):
    data = await request.json()
    return data


