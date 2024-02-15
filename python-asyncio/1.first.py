# This is simple example of asyncio where we have demosted 
# if you run this program without asycio it will take 6 seconds to excecute but with asyncio only 4 seconds

import asyncio


async def callRajan():
    await asyncio.sleep(4)
    print("How are you Rajan")


async def callSharma():
    await asyncio.sleep(2)
    print("How are you Sharma")


async def main():
    task1 = asyncio.create_task(callRajan())
    task2 = asyncio.create_task(callSharma())
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())




