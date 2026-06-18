# Conceitos da API Python

## Browser

Representa a sessão do navegador:

```python
from vibium import browser

bro = browser.start(headless=False)
```

Encerre a sessão ao final:

```python
bro.stop()
```

## Página

O método `bro.page()` obtém a página padrão:

```python
page = bro.page()
```

Na referência da API também podem existir métodos para criar e gerenciar outras
páginas. Confirme a assinatura na versão instalada antes de incorporá-los a um
projeto.

## Navegação

```python
page.go("https://example.com")
```

Depois de navegar, valide um sinal observável da página esperada.

## Localização

O exemplo mais simples usa um seletor CSS:

```python
titulo = page.find("h1")
```

A referência atual também apresenta localização semântica por propriedades
como papel e texto. Consulte a assinatura correspondente à sua versão:

```python
botao = page.find(role="button", text="Entrar")
```

Localizadores semânticos costumam expressar melhor a intenção do teste ou robô.

## Interação

O objeto retornado por `page.find()` representa um elemento:

```python
elemento.click()
elemento.fill("valor")
texto = elemento.text()
```

Nem todos os métodos servem para todos os elementos. Um campo pode ser
preenchido; um botão normalmente deve ser clicado.

## Captura

`page.screenshot()` retorna bytes:

```python
from pathlib import Path

Path("pagina.png").write_bytes(page.screenshot())
```

## Esperas

Evite transformar atrasos fixos na estratégia principal:

```python
# Frágil quando usado sem uma condição posterior
page.wait(3000)
```

Prefira aguardar ou verificar uma condição relacionada ao resultado:

- URL esperada;
- texto visível;
- elemento presente;
- desaparecimento de um carregamento;
- estado atualizado de um controle.

Os métodos exatos de espera podem mudar entre versões; consulte a
[referência atual](https://www.daisyladybug.com/vibium/python/).

