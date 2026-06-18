from pathlib import Path

from vibium import browser


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.go("https://example.com")

        titulo = page.find("h1")
        print(titulo.text())

        Path("example.png").write_bytes(page.screenshot())
    finally:
        bro.stop()


if __name__ == "__main__":
    main()

