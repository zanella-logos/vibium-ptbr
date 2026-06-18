from vibium import browser


HTML = """
<!doctype html>
<html lang="pt-BR">
  <body>
    <h1>Página principal</h1>
    <iframe
      name="conteudo"
      srcdoc="<button id='continuar'>Continuar</button>"
    ></iframe>
  </body>
</html>
"""


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.set_content(HTML)

        frame = page.frame("conteudo")
        if frame is None:
            raise RuntimeError("Frame não encontrado")

        botao = frame.find("#continuar", timeout=5_000)
        print("Botão encontrado no frame:", botao.text())
    finally:
        bro.stop()


if __name__ == "__main__":
    main()

