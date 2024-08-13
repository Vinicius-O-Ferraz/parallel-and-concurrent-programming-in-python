import time
import asyncio

async def brew_coffee()->str:
    print("Start brew_coffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "Coffee ready"

async def toast_bagel():
    print("Start toast_bagel()")
    await asyncio.sleep(2)
    print("End toast_bagel()")
    return "Bagel toasted"

async def main():
    start_time = time.time()

    batch = asyncio.gather(brew_coffee(),toast_bagel())
    result_coffee, result_bagel = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(result_coffee)
    print(result_bagel)
    print(f" Your breakfast is ready in {elapsed_time:.2f}")

if __name__ == '__main__':
    asyncio.run(main())