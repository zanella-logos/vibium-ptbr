# Primeiro script com Python

Crie o arquivo `hello_vibium.py`:

```python
from pathlib import Path

from vibium import browser


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.go("https://example.com")

        titulo = page.find("h1")
        print("Título:", titulo.text())

        imagem = page.screenshot()
        Path("example.png").write_bytes(imagem)
    finally:
        bro.stop()


if __name__ == "__main__":
    main()
```

Execute:

```bash
python hello_vibium.py
```

O script:

1. abre o Chrome;
2. obtém a página padrão;
3. navega para um site público;
4. encontra o primeiro elemento `h1`;
5. lê seu texto;
6. salva uma captura;
7. encerra o navegador mesmo se ocorrer um erro.

## Por que usar `try/finally`?

Sem o `finally`, uma exceção pode deixar o navegador aberto. O encerramento é
uma responsabilidade do script e deve ocorrer também nos caminhos de falha.

## API assíncrona

O Vibium também oferece uma API assíncrona:

```python
import asyncio

from vibium.async_api import browser


async def main():
    bro = await browser.start()

    try:
        page = await bro.page()
        await page.go("https://example.com")
        titulo = await page.find("h1")
        print(await titulo.text())
    finally:
        await bro.stop()


asyncio.run(main())
```

Para scripts lineares, a API síncrona costuma ser mais simples. Use a API
assíncrona quando ela fizer sentido para a arquitetura da aplicação.

