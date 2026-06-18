# Comandos Python por tópico

Este guia organiza os comandos mais usados da API síncrona. As assinaturas
abaixo foram verificadas localmente com o Vibium `26.5.31`.

Ele não substitui a referência completa. Como o projeto evolui rapidamente,
confira a versão instalada antes de reutilizar um exemplo:

```bash
pip show vibium
```

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
- listar páginas abertas;
- reagir à abertura de páginas e popups;
- encerrar a sessão.

```python
page = bro.page()          # página padrão
nova = bro.new_page()      # cria outra página
paginas = bro.pages()      # lista páginas abertas
bro.stop()
```

## Navegação

```python
page.go("https://example.com")
page.reload()
page.back()
page.forward()
```

Informações da página:

```python
print(page.url())
print(page.title())
print(page.content())
```

Esperar o carregamento ou uma URL:

```python
page.wait_until.loaded(timeout=30_000)
page.wait_until.url("**/dashboard", timeout=30_000)
```

## Localização

Por seletor CSS:

```python
titulo = page.find("h1")
campo = page.find("input[name='email']")
```

Por propriedades semânticas:

```python
botao = page.find(role="button", text="Entrar")
usuario = page.find(label="Usuário")
busca = page.find(placeholder="Pesquisar")
logo = page.find(alt="Logotipo")
salvar = page.find(title="Salvar")
menu = page.find(testid="menu-principal")
```

Por XPath:

```python
item = page.find(xpath="//button[contains(., 'Continuar')]")
```

Com timeout:

```python
mensagem = page.find(text="Operação concluída", timeout=10_000)
```

Encontrar vários elementos:

```python
linhas = page.find_all("table tbody tr")

for linha in linhas:
    print(linha.text())
```

Buscar dentro de um elemento:

```python
tabela = page.find("table")
botao = tabela.find(role="button", text="Detalhes")
```

Prefira, nesta ordem prática:

1. `testid`, quando a aplicação fornece um identificador estável;
2. propriedades semânticas como `role`, `label` e `text`;
3. seletores CSS estáveis;
4. XPath quando as alternativas não forem suficientes.

## Elementos

```python
elemento.click()
elemento.dblclick()
elemento.fill("valor")
texto = elemento.text()
```

### Clique e foco

```python
botao.click(timeout=10_000)
botao.dblclick()
botao.hover()
botao.focus()
botao.scroll_into_view()
```

### Campos de texto

```python
campo.fill("novo valor")  # substitui o conteúdo
campo.type("texto")       # simula digitação
campo.clear()
campo.press("Enter")
```

### Checkbox e seleção

```python
checkbox.check()
print(checkbox.is_checked())
checkbox.uncheck()

selecao.select_option("valor-da-opcao")
```

### Upload

```python
arquivo = page.find("input[type='file']")
arquivo.set_files([r"C:\caminho\documento.pdf"])
```

### Drag-and-drop

```python
origem = page.find(testid="item")
destino = page.find(testid="destino")
origem.drag_to(destino)
```

### Texto, HTML, valor e atributos

```python
print(elemento.text())
print(elemento.inner_text())
print(elemento.html())
print(elemento.value())
print(elemento.attr("href"))
print(elemento.get_attribute("data-id"))
```

### Consultar estado

```python
elemento.is_visible()
elemento.is_hidden()
elemento.is_enabled()
elemento.is_editable()
elemento.is_checked()
```

### Esperar estado

```python
elemento.wait_until("visible", timeout=10_000)
```

Antes de interagir, confirme que o localizador identifica o alvo correto.
Depois, valide o resultado esperado.

## Teclado

Em um elemento:

```python
campo.press("Enter")
```

Na página:

```python
page.keyboard.press("Control+A")
page.keyboard.type("texto")
page.keyboard.down("Shift")
page.keyboard.up("Shift")
```

Prefira `fill()` para preencher campos de forma direta. Use teclado quando o
comportamento real da tecla for relevante.

## Mouse

Interação com elementos:

```python
elemento.click()
elemento.dblclick()
elemento.hover()
origem.drag_to(destino)
```

Controle direto por coordenadas:

```python
page.mouse.move(400, 300)
page.mouse.click(400, 300)
page.mouse.down()
page.mouse.move(700, 300)
page.mouse.up()
page.mouse.wheel(0, 600)
```

Para descobrir a posição de um elemento:

```python
caixa = elemento.bounding_box()
print(caixa)
```

Coordenadas são mais frágeis porque dependem de janela, zoom e layout. Use
`elemento.click()`, `hover()` e `drag_to()` sempre que houver um alvo confiável.

## Scroll

```python
page.scroll("down", amount=3)
page.scroll("up", amount=2)
page.scroll("down", amount=1, selector="#conteudo")
elemento.scroll_into_view()
```

## Esperas

Uma espera deve representar uma condição relevante:

- elemento apareceu;
- URL mudou;
- carregamento terminou;
- texto esperado ficou disponível;
- controle mudou de estado.

```python
page.wait(1000)
```

Esperas mais específicas:

```python
page.wait_until.loaded(timeout=30_000)
page.wait_until.url("**/dashboard", timeout=30_000)
elemento.wait_until("visible", timeout=10_000)
```

`page.wait(ms)` é uma pausa fixa. Pode ser útil durante diagnóstico ou para uma
transição conhecida, mas não deve substituir a verificação do resultado.

## Páginas, popups e frames

```python
nova_pagina = bro.new_page()
paginas = bro.pages()
nova_pagina.bring_to_front()
nova_pagina.close()
```

Frames:

```python
frames = page.frames()
frame = page.frame("nome-ou-parte-da-url")

if frame:
    frame.find(role="button", text="Continuar").click()
```

O retorno de `page.frame()` pode ser `None`. Trate esse caso.

## Downloads e diálogos

Capturar um download disparado por uma ação:

```python
with page.capture.download(timeout=30_000) as download:
    page.find(text="Baixar").click()

arquivo = download.value
print(arquivo.suggested_filename())
arquivo.save_as("downloads/arquivo.pdf")
```

Diálogos JavaScript:

```python
page.on_dialog("accept")
```

Valide o comportamento exato de captura na versão instalada e no site usado.

## Capturas

Screenshot:

```python
from pathlib import Path

png = page.screenshot(full_page=True)
Path("pagina.png").write_bytes(png)
```

Screenshot de um elemento:

```python
Path("elemento.png").write_bytes(elemento.screenshot())
```

PDF:

```python
Path("pagina.pdf").write_bytes(page.pdf())
```

Capturas ajudam na auditoria e no diagnóstico, mas podem conter dados
confidenciais.

## Web, HTML e JavaScript

Ler o HTML completo:

```python
html = page.content()
```

Executar JavaScript:

```python
titulo = page.evaluate("document.title")
quantidade = page.eval("document.querySelectorAll('a').length")
```

Inserir script ou CSS:

```python
page.add_script("window.exemplo = true")
page.add_style("body { outline: 3px solid red; }")
```

Alterar o HTML da página:

```python
page.set_content("<h1>Página de teste</h1>")
```

JavaScript pode resolver casos específicos, mas aumenta o acoplamento com a
implementação interna do site. Prefira a API de elementos quando ela atender ao
caso.

## Janela e viewport

```python
page.set_viewport({"width": 1366, "height": 768})
print(page.viewport())

page.set_window(width=1366, height=900, x=0, y=0)
print(page.window())
```

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
