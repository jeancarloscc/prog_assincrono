import asyncio

async def criar_usuario(dados_usuario, db):
    usuario = {
        'nome': dados_usuario.get('nome'),
        'idade': dados_usuario.get('idade')
    }

    db.create(usuario)
    novo_usuario = db.get(usuario)

    return novo_usuario