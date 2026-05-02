# Programação assíncrona em Python

Material da aula da live: https://www.youtube.com/watch?v=hQ-PplE8kFs. O objetivo é entender programação assíncrona com `asyncio`, comparando execução síncrona e concorrente com tarefas.

## Conteúdo do repositório

- [sync_example.py](sync_example.py) - Execução síncrona (bloqueante) das etapas de preparo.
- [async_example.py](async_example.py) - Execução assíncrona concorrente com `asyncio.gather`.
- [async_example2.py](async_example2.py) - Tarefas assíncronas com `create_task` em loop contínuo.
- [db_example.py](db_example.py) - Função assíncrona simulando criação e leitura em um banco (exemplo de estrutura).

## Requisitos

- Python 3.8+ instalado

## Como executar

No terminal, rode um dos exemplos abaixo:

```bash
python sync_example.py
python async_example.py
python async_example2.py
```

## Observações

- [async_example2.py](async_example2.py) roda indefinidamente. Para parar, use `Ctrl+C`.
- [db_example.py](db_example.py) é um trecho didático e não é executável sozinho; você precisaria de um objeto `db` real com `create` e `get`.

## Referência

- Live: https://www.youtube.com/watch?v=hQ-PplE8kFs