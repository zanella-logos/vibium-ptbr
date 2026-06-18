from vibium import browser


def main():
    bro = browser.start(headless=False)

    try:
        page = bro.page()
        page.go("https://example.com")
        page.wait_until.loaded(timeout=30_000)

        titulo = page.evaluate("document.title")
        links = page.evaluate(
            "[...document.querySelectorAll('a')].map(a => a.href)"
        )
        arvore = page.a11y_tree()

        print("Título:", titulo)
        print("Links:", links)
        print("Árvore de acessibilidade:", arvore)
    finally:
        bro.stop()


if __name__ == "__main__":
    main()

