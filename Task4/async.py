import asyncio


async def main():
    await asyncio.sleep(2)
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


# Python 3.7+
asyncio.run(main())
