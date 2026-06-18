# Exemplos executáveis

Os exemplos desta pasta usam páginas públicas ou HTML local controlado. Nenhum
deles depende de credenciais, portais internos ou dados reais.

## Preparação

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Exemplos

| Arquivo | Conteúdo |
|---|---|
| [`01_primeiro_script.py`](01_primeiro_script.py) | Abre um site, lê um título e salva screenshot. |
| [`02_async.py`](02_async.py) | Repete o fluxo básico com a API assíncrona. |
| [`03_find_e_interacao.py`](03_find_e_interacao.py) | Demonstra `find`, `fill`, `click` e validação. |
| [`04_screenshot_e_pdf.py`](04_screenshot_e_pdf.py) | Salva screenshot completo, elemento e PDF. |
| [`05_javascript_e_dom.py`](05_javascript_e_dom.py) | Consulta o DOM com `evaluate()` e `a11y_tree()`. |
| [`06_esperas.py`](06_esperas.py) | Usa timeout de localização e espera de elemento. |
| [`07_mouse_e_teclado.py`](07_mouse_e_teclado.py) | Demonstra mouse, teclado e eventos; valide na versão instalada. |
| [`08_frames.py`](08_frames.py) | Interage com um `iframe` local controlado. |
| [`09_multiplas_paginas.py`](09_multiplas_paginas.py) | Cria, lista, alterna e fecha páginas. |
| [`10_download.py`](10_download.py) | Captura e salva um download. |
| [`11_logs_e_erros.py`](11_logs_e_erros.py) | Coleta console e erros JavaScript. |

## Observações

- Execute cada arquivo separadamente.
- Alguns recursos dependem do comportamento do Chrome e do sistema operacional.
- Os exemplos `03` e `06` foram executados com sucesso no Vibium `26.5.31`.
- Teclado global, frames, múltiplas páginas, eventos e download devem ser
  validados no ambiente e na versão utilizados.
- O exemplo de download usa uma página pública externa e pode exigir ajustes se
  ela mudar.
- Use `headless=False` durante estudo e diagnóstico.
- Os arquivos gerados são ignorados pelo Git.
