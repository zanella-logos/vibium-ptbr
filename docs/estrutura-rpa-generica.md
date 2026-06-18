# Estrutura genérica de RPA com Vibium

Este modelo é um ponto de partida para robôs pequenos e médios. Ele separa o
ciclo do navegador, as páginas do site, a regra do processo e as evidências.

Não transforme toda função em wrapper. Comece com a API do Vibium diretamente e
extraia componentes quando houver repetição real ou uma política técnica.

## Estrutura sugerida

```text
projeto-vibium/
├── main.py
├── requirements.txt
├── .env.example
├── src/
│   └── automacao/
│       ├── __init__.py
│       ├── config.py
│       ├── exceptions.py
│       ├── logging_config.py
│       ├── browser_session.py
│       ├── pages/
│       │   ├── __init__.py
│       │   └── example_page.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── consulta.py
│       └── evidence/
│           ├── __init__.py
│           └── writer.py
└── tests/
    └── test_example_page.py
```

Para um robô muito pequeno, reduza a estrutura. Não crie dez arquivos para um
script de vinte linhas.

## `main.py`

O ponto de entrada deve coordenar o processo, não concentrar todos os detalhes:

```python
import logging

from automacao.browser_session import BrowserSession
from automacao.config import Settings
from automacao.logging_config import configure_logging
from automacao.services.consulta import executar_consulta


def main():
    configure_logging()
    settings = Settings.from_env()

    with BrowserSession(headless=settings.headless) as session:
        executar_consulta(
            page=session.page,
            url=settings.portal_url,
            output_dir=settings.output_dir,
        )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.exception("Falha não tratada na automação")
        raise
```

## `config.py`

Configurações variáveis devem vir do ambiente:

```python
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    portal_url: str
    output_dir: Path
    headless: bool

    @classmethod
    def from_env(cls):
        return cls(
            portal_url=os.environ.get(
                "PORTAL_URL",
                "https://example.com",
            ),
            output_dir=Path(
                os.environ.get("OUTPUT_DIR", "outputs")
            ),
            headless=(
                os.environ.get("HEADLESS", "false").lower()
                == "true"
            ),
        )
```

## `browser_session.py`

Um context manager garante o encerramento do navegador:

```python
from vibium import browser


class BrowserSession:
    def __init__(self, headless=False):
        self.headless = headless
        self.browser = None
        self.page = None

    def __enter__(self):
        self.browser = browser.start(headless=self.headless)
        self.page = self.browser.page()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.browser is not None:
            self.browser.stop()
```

## `pages/example_page.py`

Page Objects agrupam elementos e comportamentos de uma página:

```python
class ExamplePage:
    def __init__(self, page):
        self.page = page

    def abrir(self, url):
        self.page.go(url)
        self.page.wait_until.loaded(timeout=30_000)

    def titulo(self):
        return self.page.find("h1", timeout=10_000).text()

    def validar(self):
        titulo = self.page.find("h1", timeout=10_000)
        titulo.wait_until("visible", timeout=10_000)
```

## `evidence/writer.py`

Evidências ficam isoladas da regra de negócio:

```python
from pathlib import Path


def salvar_screenshot(page, destino):
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(page.screenshot(full_page=True))
    return destino


def salvar_pdf(page, destino):
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(page.pdf())
    return destino
```

## `services/consulta.py`

O serviço coordena o caso de uso:

```python
from automacao.evidence.writer import salvar_screenshot
from automacao.pages.example_page import ExamplePage


def executar_consulta(page, url, output_dir):
    portal = ExamplePage(page)
    portal.abrir(url)
    portal.validar()

    titulo = portal.titulo()
    salvar_screenshot(page, output_dir / "consulta.png")

    return {"titulo": titulo}
```

## Exceções

Crie exceções quando a automação precisar distinguir tipos de falha:

```python
class AutomationError(Exception):
    pass


class LoginError(AutomationError):
    pass


class ValidationError(AutomationError):
    pass
```

Não capture `Exception` em toda função. Trate uma falha onde seja possível
acrescentar contexto ou tomar uma decisão.

## Logging

```python
import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s %(levelname)s "
            "%(name)s: %(message)s"
        ),
    )
```

Evite registrar senhas, tokens, cookies, certificados e identificadores
completos.

## Wrappers

Um wrapper deve acrescentar uma política ou contrato:

```python
def aguardar_resultado(page, texto, timeout=10_000):
    resultado = page.find(text=texto, timeout=timeout)
    resultado.wait_until("visible", timeout=timeout)
    return resultado
```

Evite abstrações que apenas mudam o nome:

```python
def clicar(page, texto):
    page.find(text=texto).click()
```

Nesse caso, usar a API diretamente é mais claro.

## Checklist

- O navegador sempre é encerrado?
- Há uma condição explícita de sucesso?
- As esperas observam estados reais?
- As evidências ficam fora da regra de negócio?
- Configurações vêm do ambiente?
- Logs evitam dados sensíveis?
- Cada módulo possui uma responsabilidade compreensível?
- A estrutura é proporcional ao tamanho do robô?

