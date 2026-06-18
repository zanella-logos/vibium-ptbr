from vibium import browser


HTML = """
<!doctype html>
<html lang="pt-BR">
  <body>
    <form id="cadastro">
      <label for="nome">Nome</label>
      <input id="nome" name="nome" placeholder="Digite seu nome">

      <label>
        <input type="checkbox" id="aceite">
        Aceito os termos
      </label>

      <button type="button" data-testid="salvar">Salvar</button>
      <p id="resultado" hidden></p>
    </form>

    <script>
      document.querySelector('[data-testid="salvar"]').addEventListener(
        'click',
        () => {
          const nome = document.querySelector('#nome').value;
          const resultado = document.querySelector('#resultado');
          resultado.textContent = `Salvo: ${nome}`;
          resultado.hidden = false;
        }
      );
    </script>
  </body>
</html>
"""


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.set_content(HTML)

        # Localizador CSS usado para manter o exemplo executável na 26.5.31.
        campo = page.find("#nome")
        campo.fill("Victor")

        aceite = page.find("#aceite")
        aceite.check()

        salvar = page.find('[data-testid="salvar"]')
        salvar.click()

        resultado = page.find(text="Salvo: Victor", timeout=5_000)
        resultado.wait_until("visible", timeout=5_000)

        print(resultado.text())
        print("Checkbox marcado:", aceite.is_checked())
    finally:
        bro.stop()


if __name__ == "__main__":
    main()
