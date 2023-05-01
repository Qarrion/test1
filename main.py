import asyncio

async def coro(lock, name):
    print(f"{name} is waiting to acquire the lock")
    async with lock:
        print(f"{name} has acquired the lock")
        # Do something with the shared resource
        await asyncio.sleep(1)
    print(f"{name} has released the lock")

async def main():
    # Create a lock
    lock = asyncio.Lock()

    # Create multiple coroutines that access the shared resource
    tasks = [asyncio.create_task(coro(lock, f"Coroutine {i+1}")) for i in range(3)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

asyncio.run(main())

"test 추가"