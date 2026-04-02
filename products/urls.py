from fastapi import APIRouter

router =APIRouter(prefix='/products')


@router.get('/')
async def products_list():
    return {'mevalar': 'olma, anor'}

@router.get('/test')
async def products_list():
    return {'test': 'test'}