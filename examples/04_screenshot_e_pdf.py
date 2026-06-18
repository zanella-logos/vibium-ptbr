from pathlib import Path

from vibium import browser


OUTPUT = Path("outputs")


def main():
    OUTPUT.mkdir(exist_ok=True)
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.go("https://example.com")
        page.wait_until.loaded(timeout=30_000)

        titulo = page.find("h1", timeout=10_000)

        (OUTPUT / "pagina.png").write_bytes(
            page.screenshot(full_page=True)
        )
        (OUTPUT / "titulo.png").write_bytes(titulo.screenshot())
        (OUTPUT / "pagina.pdf").write_bytes(page.pdf())

        print("Arquivos salvos em:", OUTPUT.resolve())
    finally:
        bro.stop()


if __name__ == "__main__":
    main()

