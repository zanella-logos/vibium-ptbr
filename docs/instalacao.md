# Instalação

## Requisitos

- Python 3.9 ou superior;
- Windows x64, Linux x64 ou macOS;
- acesso à internet na primeira execução para baixar dependências e o Chrome.

## Ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalar o Vibium

```bash
pip install vibium
```

O Chrome é baixado automaticamente na primeira chamada a `browser.start()`.
Também é possível preparar o navegador antecipadamente:

```bash
vibium install
```

## Verificar a instalação

```bash
pip show vibium
```

Crie `verificar_vibium.py`:

```python
from vibium import browser

bro = browser.start()

try:
    page = bro.page()
    page.go("https://example.com")
    print(page.find("h1").text())
finally:
    bro.stop()
```

Execute:

```bash
python verificar_vibium.py
```

## Modo headless

Para executar sem uma janela visível:

```python
bro = browser.start(headless=True)
```

Durante desenvolvimento e diagnóstico, prefira `headless=False`.

## Cache no Windows

Segundo o tutorial oficial, os arquivos gerenciados pelo Vibium ficam em:

```text
%LOCALAPPDATA%\vibium\
```

## Próximo passo

Continue em [Primeiro script com Python](python/primeiro-script.md).

