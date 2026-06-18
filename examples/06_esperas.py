from vibium import browser


HTML = """
<!doctype html>
<html lang="pt-BR">
  <body>
    <p id="status">Carregando...</p>
    <script>
      setTimeout(() => {
        document.querySelector('#status').textContent = 'Processo concluído';
      }, 1000);
    </script>
  </body>
</html>
"""


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.set_content(HTML)

        status = page.find("#status", timeout=5_000)

        for _ in range(20):
            if status.text() == "Processo concluído":
                break
            page.wait(250)
        else:
            raise TimeoutError("O status não foi atualizado")

        print(status.text())
    finally:
        bro.stop()


if __name__ == "__main__":
    main()
