# Programacao assincrona em Python

Material da aula da live https://www.youtube.com/watch?v=hQ-PplE8kFs. O objetivo e entender programacao assincrona com `asyncio`, comparando execucao sincrona e concorrente com tarefas.

## Conteudo do repositorio

- [sync_example.py](sync_example.py) - Execucao sincrona (bloqueante) das etapas de preparo.
- [async_example.py](async_example.py) - Execucao assincrona concorrente com `asyncio.gather`.
- [async_example2.py](async_example2.py) - Tarefas assincronas com `create_task` em loop continuo.
- [db_example.py](db_example.py) - Funcao assincrona simulando criacao e leitura em um banco (exemplo de estrutura).

## Requisitos

- Python 3.8+ instalado

## Como executar

No terminal, rode um dos exemplos abaixo:

```bash
python sync_example.py
```

```bash
python async_example.py
```

```bash
python async_example2.py
```

## Observacoes

- [async_example2.py](async_example2.py) roda indefinidamente. Para parar, use `Ctrl+C`.
- [db_example.py](db_example.py) e um trecho didatico e nao e executavel sozinho; voce precisaria de um objeto `db` real com `create` e `get`.

## Referencia

- Live: https://www.youtube.com/watch?v=hQ-PplE8kFs
