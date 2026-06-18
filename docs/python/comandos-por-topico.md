# Comandos Python por tópico

Este guia rápido organiza os comandos mais usados. Ele não substitui a
referência completa e deve ser conferido contra a versão instalada do Vibium.

## Navegador

```python
from vibium import browser

bro = browser.start(headless=False)
page = bro.page()
bro.stop()
```

Principais responsabilidades:

- iniciar o navegador;
- acessar ou criar páginas;
- encerrar a sessão.

## Navegação

```python
page.go("https://example.com")
```

Outras operações de navegação podem incluir voltar, avançar e recarregar.
Confirme os nomes e assinaturas na versão utilizada.

## Localização

Por seletor CSS:

```python
titulo = page.find("h1")
```

Por intenção semântica:

```python
botao = page.find(role="button", text="Entrar")
```

Localizadores semânticos tendem a ser mais legíveis, mas precisam refletir a
estrutura acessível da página.

## Elementos

```python
elemento.click()
elemento.fill("valor")
texto = elemento.text()
```

Antes de interagir, confirme que o localizador identifica o elemento correto.
Depois da interação, valide o resultado esperado.

## Teclado

Operações de teclado são úteis para atalhos, envio de teclas e controles que não
respondem bem a preenchimento direto. Use apenas quando uma interação mais
semântica não resolver o problema.

Consulte a categoria **Keyboard** da referência Python para os métodos
disponíveis na versão atual.

## Mouse

Movimento, clique, duplo clique, rolagem e arraste podem ser necessários em
interfaces complexas. Evite coordenadas fixas quando houver um elemento ou
localizador estável disponível.

Consulte a categoria **Mouse** da referência Python.

## Esperas

Uma espera deve representar uma condição relevante:

- elemento apareceu;
- URL mudou;
- carregamento terminou;
- texto esperado ficou disponível;
- controle mudou de estado.

```python
# Uma pausa fixa pode ser útil para diagnóstico,
# mas não deve ser a estratégia principal.
page.wait(1000)
```

## Capturas

Screenshot:

```python
from pathlib import Path

png = page.screenshot()
Path("pagina.png").write_bytes(png)
```

Capturas ajudam na auditoria e no diagnóstico, mas podem conter dados
confidenciais.

## JavaScript e estado da página

Execução de JavaScript pode resolver casos específicos ou obter estado da
página, mas aumenta o acoplamento com sua implementação interna. Confirme o
método suportado pela versão instalada antes de usar.

## API assíncrona

```python
from vibium.async_api import browser

bro = await browser.start()
page = await bro.page()
await page.go("https://example.com")
await bro.stop()
```

Na API assíncrona, as chamadas correspondentes normalmente precisam de `await`.

## Referência completa

A referência complementar da Daisy Ladybug organiza atualmente a API Python em
categorias como Browser, Navigate, Find, Element, Keyboard, Mouse, Wait, Page,
Capture e Clock:

- [Referência Python](https://www.daisyladybug.com/vibium/python/)
- [Tutorial oficial de Python](https://github.com/VibiumDev/vibium/blob/main/docs/tutorials/getting-started-python.md)

