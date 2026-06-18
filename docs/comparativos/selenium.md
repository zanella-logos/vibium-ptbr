# Migração de Selenium para Vibium

Vibium e Selenium não são intercambiáveis linha por linha. Migre pelo
comportamento esperado, não apenas pelo nome dos métodos.

## Mapeamento inicial

| Intenção | Selenium | Vibium Python |
|---|---|---|
| Abrir sessão | `webdriver.Chrome()` | `browser.start()` |
| Obter página | objeto `driver` | `bro.page()` |
| Navegar | `driver.get(url)` | `page.go(url)` |
| Localizar por CSS | `driver.find_element(By.CSS_SELECTOR, "h1")` | `page.find("h1")` |
| Clicar | `element.click()` | `element.click()` |
| Preencher | `element.send_keys(valor)` | `element.fill(valor)` |
| Ler texto | `element.text` | `element.text()` |
| Screenshot | `driver.save_screenshot(...)` | `page.screenshot()` retorna bytes |
| Encerrar | `driver.quit()` | `bro.stop()` |

## Estratégia de migração

1. escolha um fluxo pequeno;
2. registre entradas, resultados e evidências atuais;
3. implemente o mesmo comportamento em Vibium;
4. compare os resultados;
5. trate esperas e navegação explicitamente;
6. só então remova o fluxo antigo.

## Esperas

Não converta automaticamente:

```python
time.sleep(5)
```

em outra espera fixa. Identifique a condição que realmente importa, como uma
URL, mensagem ou elemento.

## Localizadores

Revise os localizadores durante a migração. Um seletor CSS herdado pode
funcionar, mas um localizador semântico pode descrever melhor a intenção:

```python
page.find(role="button", text="Entrar")
```

Confirme a assinatura na versão instalada.

## Recursos externos ao navegador

Popups nativos, certificados digitais, janelas do sistema operacional e
captchas podem exigir ferramentas complementares. Não atribua automaticamente
essas responsabilidades ao Vibium.

