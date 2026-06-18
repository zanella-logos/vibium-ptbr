from vibium import browser


HTML = """
<!doctype html>
<html lang="pt-BR">
  <body>
    <label for="texto">Texto</label>
    <input id="texto">
    <button id="botao">Passe o mouse</button>
    <p id="resultado"></p>

    <script>
      const botao = document.querySelector('#botao');
      botao.addEventListener('mouseenter', () => {
        document.querySelector('#resultado').textContent = 'Mouse detectado';
      });
    </script>
  </body>
</html>
"""


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.set_content(HTML)

        campo = page.find(label="Texto")
        campo.click()
        page.keyboard.type("Vibium")
        page.keyboard.press("Control+A")
        page.keyboard.type("Vibium PT-BR")

        botao = page.find("#botao")
        botao.hover()

        resultado = page.find("#resultado", timeout=5_000)
        if resultado.text() != "Mouse detectado":
            raise RuntimeError("O evento de mouse não foi detectado")

        print("Campo:", campo.value())
        print("Resultado:", resultado.text())

        caixa = botao.bounding_box()
        if caixa:
            page.mouse.click(
                caixa["x"] + caixa["width"] / 2,
                caixa["y"] + caixa["height"] / 2,
            )
    finally:
        bro.stop()


if __name__ == "__main__":
    main()
