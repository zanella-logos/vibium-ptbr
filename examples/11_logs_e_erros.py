from vibium import browser


HTML = """
<!doctype html>
<html lang="pt-BR">
  <body>
    <h1>Console e erros</h1>
    <script>
      console.log('Mensagem de teste');
      setTimeout(() => {
        throw new Error('Erro de teste');
      }, 100);
    </script>
  </body>
</html>
"""


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.on_console()
        page.on_error()
        page.set_content(HTML)
        page.wait(500)

        print("Console:", page.console_messages())
        print("Erros:", page.errors())
    finally:
        bro.stop()


if __name__ == "__main__":
    main()

