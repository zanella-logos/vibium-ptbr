from vibium import browser


def main():
    bro = browser.start(headless=False)

    try:
        principal = bro.page()
        principal.set_content("<title>Principal</title><h1>Principal</h1>")

        secundaria = bro.new_page()
        secundaria.set_content("<h1>Segunda página</h1>")

        for indice, page in enumerate(bro.pages(), start=1):
            print(indice, page.title(), page.url())

        principal.bring_to_front()
        secundaria.close()
    finally:
        bro.stop()


if __name__ == "__main__":
    main()
