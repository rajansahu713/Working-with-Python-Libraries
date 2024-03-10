



import time

def callRajan():
    time.sleep(4)
    print("Hi Rajan")

def callSharma():
    time.sleep(2)
    print("Hi Sharma")


def main():
    start = time.time()
    task1 = callRajan()
    task2 = callSharma()
    end = time.time()   
    print(f"Time taken without asyncio is {end - start}")

if __name__ == "__main__":
    main()




