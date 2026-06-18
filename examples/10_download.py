from pathlib import Path

from vibium import browser


OUTPUT = Path("downloads")
URL = "https://the-internet.herokuapp.com/download"


def main():
    OUTPUT.mkdir(exist_ok=True)
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.go(URL)
        page.wait_until.loaded(timeout=30_000)

        links = page.find_all("#content a")
        if not links:
            raise RuntimeError("Nenhum arquivo disponível para download")

        primeiro_link = links[0]

        with page.capture.download(timeout=30_000) as info:
            primeiro_link.click()

        download = info.value
        if download is None:
            raise RuntimeError("Download não capturado")

        destino = OUTPUT / download.suggested_filename()
        download.save_as(str(destino))

        print("Download salvo em:", destino.resolve())
    finally:
        bro.stop()


if __name__ == "__main__":
    main()

