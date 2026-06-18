import asyncio

from vibium.async_api import browser


async def main():
    bro = await browser.start()

    try:
        page = await bro.page()
        await page.go("https://example.com")

        titulo = await page.find("h1")
        print(await titulo.text())
    finally:
        await bro.stop()


if __name__ == "__main__":
    asyncio.run(main())

