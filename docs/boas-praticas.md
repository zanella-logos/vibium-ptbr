# Boas práticas

## Encerre o navegador

```python
bro = browser.start()

try:
    page = bro.page()
    # automação
finally:
    bro.stop()
```

## Verifique resultados

Depois de uma ação, confirme uma mudança relacionada ao objetivo:

- página correta;
- mensagem esperada;
- arquivo criado;
- elemento com novo estado;
- registro salvo.

## Evite segredos no código

```python
import os

usuario = os.environ["AUTOMATION_USER"]
senha = os.environ["AUTOMATION_PASSWORD"]
```

Nunca publique senhas, tokens, certificados, dados pessoais, strings de conexão
ou evidências de produção.

## Não esconda a API cedo demais

Um wrapper que apenas renomeia um método acrescenta pouco:

```python
def clicar(page, alvo):
    return page.find(alvo).click()
```

Extraia um componente quando ele oferecer um contrato útil, por exemplo:

- validação posterior;
- timeout configurável;
- tratamento de erro com contexto;
- política de evidência;
- comportamento de domínio reutilizável.

## Registre a versão

Automação de navegador depende do comportamento da biblioteca e do navegador.
Registre a versão validada no projeto:

```bash
pip freeze > requirements.txt
```

Para bibliotecas, considere limites de versão conscientes em vez de atualizar
produção automaticamente.

## Produza exemplos mínimos

Um bom exemplo:

- ensina um conceito principal;
- usa site público ou controlado;
- encerra os recursos;
- informa o resultado esperado;
- não contém dados reais;
- pode ser executado isoladamente.

