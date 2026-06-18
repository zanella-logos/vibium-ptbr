# Referência completa — Vibium Python

Referência em português baseada nas categorias da
[Daisy Ladybug](https://www.daisyladybug.com/vibium/python/), na distribuição
oficial do PyPI e na API instalada do Vibium `26.5.31`.

## Antes de usar

`bro`, `page`, `el`, `elemento` e `botao` são nomes de variáveis escolhidos pelo
programador. Eles não fazem parte do nome do comando:

```python
el = page.find("button")
el.click()
```

Isto também é válido:

```python
botao = page.find("button")
botao.click()
```

Nos dois casos, o método do Vibium é `click()`. Este guia usa:

- `bro` para o navegador;
- `page` para uma página;
- `el` para um elemento;
- `ctx` para um contexto isolado;
- `download` para um arquivo baixado.

## Fluxo mínimo

```python
from vibium import browser

bro = browser.start(headless=False)

try:
    page = bro.page()
    page.go("https://example.com")
    el = page.find("h1")
    print(el.text())
finally:
    bro.stop()
```

## 1. Browser

| Comando | Descrição |
|---|---|
| `browser.start()` | Inicia o Chrome e retorna um navegador controlável. |
| `bro.page()` | Retorna a página padrão do navegador. |
| `bro.new_page()` | Abre e retorna uma nova página/aba. |
| `bro.pages()` | Retorna todas as páginas abertas. |
| `bro.new_context()` | Cria um contexto isolado, semelhante a uma sessão anônima. |
| `bro.on_page(callback)` | Registra uma função para novas páginas. |
| `bro.on_popup(callback)` | Registra uma função para novos popups. |
| `bro.remove_all_listeners()` | Remove listeners de página, popup ou todos. |
| `bro.stop()` | Encerra o navegador e libera os recursos. |

```python
bro = browser.start(
    headless=False,
    headers={"X-Test": "valor"},
    executable_path=None,
)
```

## 2. Navigate

| Comando | Descrição |
|---|---|
| `page.go(url)` | Navega para uma URL. |
| `page.reload()` | Recarrega a página atual. |
| `page.back()` | Volta no histórico de navegação. |
| `page.forward()` | Avança no histórico de navegação. |
| `page.url()` | Retorna a URL atual. |
| `page.title()` | Retorna o título da página. |

```python
page.go("https://example.com")
print(page.url())
print(page.title())
```

## 3. Find

| Comando | Descrição |
|---|---|
| `page.find("css")` | Retorna o primeiro elemento encontrado por seletor CSS. |
| `page.find(role=...)` | Localiza um elemento pelo papel ARIA. |
| `page.find(text=...)` | Localiza um elemento pelo texto. |
| `page.find(label=...)` | Localiza um campo pelo rótulo associado. |
| `page.find(placeholder=...)` | Localiza um campo pelo placeholder. |
| `page.find(alt=...)` | Localiza um elemento pelo texto alternativo. |
| `page.find(title=...)` | Localiza um elemento pelo atributo `title`. |
| `page.find(testid=...)` | Localiza um elemento por identificador de teste. |
| `page.find(xpath=...)` | Localiza um elemento por XPath. |
| `page.find(near=...)` | Restringe a busca pela proximidade de outro conteúdo. |
| `page.find_all(...)` | Retorna todos os elementos correspondentes. |
| `el.find(...)` | Procura um elemento dentro de outro elemento. |
| `el.find_all(...)` | Procura vários elementos dentro de outro elemento. |

Todos os localizadores aceitam `timeout`:

```python
entrar = page.find(
    role="button",
    text="Entrar",
    timeout=10_000,
)
```

Exemplos:

```python
page.find("#login")
page.find("input[name='email']")
page.find(role="button", text="Salvar")
page.find(label="Usuário")
page.find(placeholder="Pesquisar")
page.find(alt="Logotipo")
page.find(title="Fechar")
page.find(testid="menu-principal")
page.find(xpath="//button[contains(., 'Continuar')]")

linhas = page.find_all("table tbody tr")
```

## 4. Mapeamento da página web

A API Python `26.5.31` não possui um método `page.map()`. O comando `map`
pertence principalmente à CLI e ao MCP.

Alternativas em Python:

| Comando | Descrição |
|---|---|
| `page.a11y_tree()` | Retorna a árvore de acessibilidade da página. |
| `page.find_all(...)` | Lista elementos que correspondem a um localizador. |
| `page.content()` | Retorna o HTML completo da página. |
| `page.evaluate(...)` | Executa JavaScript para consultar o DOM. |

```python
arvore = page.a11y_tree()
print(arvore)

botoes = page.find_all(role="button")
for botao in botoes:
    print(botao.text())
```

Com toda a árvore de acessibilidade:

```python
arvore = page.a11y_tree(everything=True)
```

## 5. Element

### Interação

| Comando | Descrição |
|---|---|
| `el.click()` | Clica no elemento. |
| `el.dblclick()` | Executa clique duplo. |
| `el.hover()` | Move o ponteiro sobre o elemento. |
| `el.focus()` | Coloca foco no elemento. |
| `el.tap()` | Executa toque no elemento. |
| `el.drag_to(destino)` | Arrasta o elemento até outro elemento. |
| `el.scroll_into_view()` | Rola a página até o elemento ficar visível. |
| `el.dispatch_event(tipo)` | Dispara um evento DOM no elemento. |

```python
el.click(timeout=10_000)
el.dblclick()
el.hover()
origem.drag_to(destino)
```

### Campos e formulários

| Comando | Descrição |
|---|---|
| `el.fill(valor)` | Substitui o conteúdo de um campo. |
| `el.type(texto)` | Digita texto simulando entrada pelo teclado. |
| `el.clear()` | Limpa o campo. |
| `el.press(tecla)` | Pressiona uma tecla com foco no elemento. |
| `el.check()` | Marca checkbox ou controle compatível. |
| `el.uncheck()` | Desmarca checkbox ou controle compatível. |
| `el.select_option(valor)` | Seleciona uma opção de um `<select>`. |
| `el.set_files(arquivos)` | Define arquivos em um campo de upload. |

```python
page.find(label="E-mail").fill("usuario@example.com")
page.find(label="Senha").fill("senha-ficticia")
page.find(role="checkbox").check()
page.find("select").select_option("BR")
page.find("input[type=file]").set_files(["documento.pdf"])
```

### Leitura

| Comando | Descrição |
|---|---|
| `el.text()` | Retorna o texto do elemento. |
| `el.inner_text()` | Retorna o texto interno renderizado. |
| `el.html()` | Retorna o HTML do elemento. |
| `el.value()` | Retorna o valor atual de um campo. |
| `el.attr(nome)` | Retorna um atributo. |
| `el.get_attribute(nome)` | Retorna um atributo; forma equivalente explícita. |
| `el.label()` | Retorna o rótulo acessível. |
| `el.role()` | Retorna o papel ARIA. |
| `el.bounding_box()` | Retorna a posição e o tamanho do elemento. |
| `el.bounds()` | Retorna os limites do elemento. |

### Estado

| Comando | Descrição |
|---|---|
| `el.is_visible()` | Informa se o elemento está visível. |
| `el.is_hidden()` | Informa se o elemento está oculto. |
| `el.is_enabled()` | Informa se está habilitado. |
| `el.is_editable()` | Informa se pode ser editado. |
| `el.is_checked()` | Informa se está marcado. |
| `el.wait_until(estado)` | Espera `visible`, `hidden`, `attached` ou `detached`. |

```python
el.wait_until("visible", timeout=10_000)

if el.is_enabled():
    el.click()
```

## 6. Keyboard

| Comando | Descrição |
|---|---|
| `page.keyboard.press(tecla)` | Pressiona e solta uma tecla. |
| `page.keyboard.type(texto)` | Digita texto na página. |
| `page.keyboard.down(tecla)` | Mantém uma tecla pressionada. |
| `page.keyboard.up(tecla)` | Solta uma tecla pressionada. |

```python
page.keyboard.press("Enter")
page.keyboard.press("Control+A")
page.keyboard.type("texto")

page.keyboard.down("Shift")
page.keyboard.press("Tab")
page.keyboard.up("Shift")
```

## 7. Mouse e toque

| Comando | Descrição |
|---|---|
| `page.mouse.move(x, y)` | Move o mouse para uma coordenada. |
| `page.mouse.click(x, y)` | Clica em uma coordenada. |
| `page.mouse.down()` | Pressiona o botão do mouse. |
| `page.mouse.up()` | Solta o botão do mouse. |
| `page.mouse.wheel(dx, dy)` | Movimenta a roda do mouse. |
| `page.touch.tap(x, y)` | Executa toque em uma coordenada. |

```python
page.mouse.move(400, 300)
page.mouse.click(400, 300)
page.mouse.wheel(0, 600)

page.mouse.down()
page.mouse.move(700, 300)
page.mouse.up()
```

Prefira `el.click()`, `el.hover()` e `el.drag_to()` quando existir um elemento
estável. Coordenadas dependem de janela, zoom e layout.

## 8. Wait

| Comando | Descrição |
|---|---|
| `page.wait(ms)` | Aguarda uma quantidade fixa de milissegundos. |
| `page.wait_until.loaded()` | Aguarda o estado de carregamento da página. |
| `page.wait_until.url(padrao)` | Aguarda a URL corresponder ao padrão. |
| `el.wait_until(estado)` | Aguarda o estado de um elemento. |

```python
page.wait_until.loaded(timeout=30_000)
page.wait_until.url("**/dashboard", timeout=30_000)
page.find(text="Sucesso").wait_until("visible", timeout=10_000)
```

Use `page.wait(ms)` apenas quando não houver uma condição melhor para observar.

## 9. Page

| Comando | Descrição |
|---|---|
| `page.content()` | Retorna o HTML completo. |
| `page.set_content(html)` | Substitui o conteúdo por um HTML informado. |
| `page.evaluate(js)` | Executa JavaScript e retorna o resultado. |
| `page.eval(js)` | Alias de `page.evaluate()`. |
| `page.add_script(js)` | Injeta JavaScript na página. |
| `page.add_style(css)` | Injeta CSS na página. |
| `page.expose(nome, fn)` | Expõe uma função para uso no contexto da página. |
| `page.scroll(...)` | Rola a página ou um contêiner. |
| `page.set_viewport(tamanho)` | Define o viewport. |
| `page.viewport()` | Retorna o viewport atual. |
| `page.set_window(...)` | Define tamanho e posição da janela. |
| `page.window()` | Retorna informações da janela. |
| `page.bring_to_front()` | Traz a página para frente. |
| `page.close()` | Fecha a página. |
| `page.set_headers(headers)` | Define cabeçalhos HTTP extras. |
| `page.set_geolocation(coords)` | Define uma localização simulada. |
| `page.emulate_media(...)` | Emula mídia, cores, contraste ou movimento reduzido. |

```python
links = page.evaluate(
    "[...document.querySelectorAll('a')].map(a => a.href)"
)

page.set_viewport({"width": 1366, "height": 768})
page.set_window(width=1366, height=900, x=0, y=0)
page.scroll("down", amount=3)
```

## 10. Frames

| Comando | Descrição |
|---|---|
| `page.frames()` | Retorna todos os frames da página. |
| `page.frame(nome_ou_url)` | Procura um frame por nome ou URL. |
| `page.main_frame()` | Retorna o frame principal. |

```python
frame = page.frame("checkout")

if frame is None:
    raise RuntimeError("Frame não encontrado")

frame.find(role="button", text="Continuar").click()
```

## 11. Capture

### Screenshot e PDF

| Comando | Descrição |
|---|---|
| `page.screenshot()` | Retorna screenshot da página em bytes. |
| `el.screenshot()` | Retorna screenshot do elemento em bytes. |
| `page.pdf()` | Retorna a página em PDF como bytes. |

```python
from pathlib import Path

Path("pagina.png").write_bytes(page.screenshot(full_page=True))
Path("elemento.png").write_bytes(el.screenshot())
Path("pagina.pdf").write_bytes(page.pdf())
```

### Captura de eventos

| Comando | Descrição |
|---|---|
| `page.capture.navigation(...)` | Captura uma navegação disparada por uma ação. |
| `page.capture.download(...)` | Captura um download. |
| `page.capture.dialog(...)` | Captura um diálogo JavaScript. |
| `page.capture.request(...)` | Captura uma requisição correspondente. |
| `page.capture.response(...)` | Captura uma resposta correspondente. |
| `page.capture.event(...)` | Captura um evento pelo nome. |

```python
with page.capture.download(timeout=30_000) as info:
    page.find(text="Baixar").click()

download = info.value
download.save_as("downloads/arquivo.pdf")
```

### Download

| Comando | Descrição |
|---|---|
| `download.url()` | Retorna a URL do download. |
| `download.path()` | Retorna o caminho temporário, quando disponível. |
| `download.suggested_filename()` | Retorna o nome sugerido. |
| `download.save_as(destino)` | Copia o arquivo para o destino informado. |

## 12. Eventos, console e rede

| Comando | Descrição |
|---|---|
| `page.on_dialog(acao)` | Aceita, rejeita ou trata diálogos. |
| `page.on_download(callback)` | Registra callback para downloads. |
| `page.on_console()` | Inicia coleta de mensagens do console. |
| `page.console_messages()` | Retorna mensagens coletadas. |
| `page.on_error()` | Inicia coleta de erros da página. |
| `page.errors()` | Retorna erros coletados. |
| `page.on_request(callback)` | Observa requisições. |
| `page.on_response(callback)` | Observa respostas. |
| `page.on_web_socket(callback)` | Observa conexões WebSocket. |
| `page.route(padrao, acao)` | Intercepta requisições correspondentes. |
| `page.unroute(padrao)` | Remove uma interceptação. |
| `page.remove_all_listeners()` | Remove listeners registrados. |

```python
page.on_console()
page.on_error()

page.go("https://example.com")

print(page.console_messages())
print(page.errors())
```

## 13. BrowserContext

Contextos mantêm cookies e armazenamento isolados.

| Comando | Descrição |
|---|---|
| `ctx.new_page()` | Cria uma página no contexto. |
| `ctx.cookies()` | Retorna cookies, opcionalmente filtrados por URL. |
| `ctx.set_cookies(cookies)` | Define cookies. |
| `ctx.clear_cookies()` | Limpa cookies. |
| `ctx.storage()` | Retorna o estado de armazenamento. |
| `ctx.set_storage(state)` | Restaura um estado de armazenamento. |
| `ctx.clear_storage()` | Limpa o armazenamento. |
| `ctx.add_init_script(js)` | Adiciona script executado na inicialização. |
| `ctx.close()` | Fecha o contexto. |

```python
ctx = bro.new_context()
page = ctx.new_page()

try:
    page.go("https://example.com")
finally:
    ctx.close()
```

## 14. Clock

O relógio controla `Date`, timers e fuso horário da página.

| Comando | Descrição |
|---|---|
| `page.clock.install()` | Instala o relógio controlável. |
| `page.clock.fast_forward(ticks)` | Avança o relógio. |
| `page.clock.run_for(ticks)` | Executa timers pelo período informado. |
| `page.clock.pause_at(tempo)` | Pausa em uma data ou instante. |
| `page.clock.resume()` | Retoma o relógio. |
| `page.clock.set_fixed_time(tempo)` | Fixa o horário observado pela página. |
| `page.clock.set_system_time(tempo)` | Altera o horário simulado do sistema. |
| `page.clock.set_timezone(fuso)` | Define o fuso horário simulado. |

```python
page.clock.install("2026-06-18T09:00:00")
page.clock.set_timezone("America/Sao_Paulo")
page.clock.fast_forward(5_000)
```

## API assíncrona

Na API assíncrona, importe:

```python
from vibium.async_api import browser
```

As operações correspondentes usam `await`:

```python
bro = await browser.start()

try:
    page = await bro.page()
    await page.go("https://example.com")
    el = await page.find("h1")
    print(await el.text())
finally:
    await bro.stop()
```

## Fontes

- [Vibium no PyPI](https://pypi.org/project/vibium/)
- [Repositório oficial](https://github.com/VibiumDev/vibium)
- [Tutorial oficial de Python](https://github.com/VibiumDev/vibium/blob/main/docs/tutorials/getting-started-python.md)
- [Daisy Ladybug — Python API](https://www.daisyladybug.com/vibium/python/)

