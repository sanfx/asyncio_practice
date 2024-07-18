## Example of asyncio/await and threading
An example of asynchronous programming using async and await in Python 3.
Asynchronous Programming ExampleHere's a simple example using asyncio:

```
import asyncio

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)  # Simulate a network request
    print("Data fetched!")
    return {"data": "sample data"}

async def main():
    print("Starting main function...")
    data = await fetch_data()
    print(f"Received data: {data}")

# Run the main function
asyncio.run(main())
```

In this example:
- `fetch_data` is an asynchronous function that simulates a network request by sleeping for 2 seconds.
- `main` is another asynchronous function that waits for `fetch_data` to complete using the await keyword.
- `asyncio.run(main())` runs the main function.

Difference Between async/await and threading
----
 `async/await`
- **Concurrency Model**: Uses an event loop to manage and schedule tasks. Tasks are non-blocking and can yield control back to the event loop using await.
- **Use Case**: Ideal for I/O-bound tasks like network requests, file I/O, or any operation that involves waiting.
- **Performance**: Efficient for handling many I/O-bound tasks concurrently without creating multiple threads.

`threading`
- **Concurrency Model**: Uses multiple threads, each with its own execution context. The operating system's scheduler manages these threads.
- **Use Case**: Suitable for CPU-bound tasks that require parallel execution, such as computations or tasks that can benefit from multiple CPU cores.
- **Performance**: Can be less efficient for I/O-bound tasks due to the overhead of context switching and potential issues with thread safety.
Example Using threading

Here's a similar example using the threading module:
```
import threading
import time

def fetch_data():
    print("Start fetching data...")
    time.sleep(2)  # Simulate a network request
    print("Data fetched!")
    return {"data": "sample data"}

def main():
    print("Starting main function...")
    thread = threading.Thread(target=fetch_data)
    thread.start()
    thread.join()
    print("Main function complete.")

# Run the main function
main()
```
In this example:
- `fetch_data` is a regular function that simulates a network request by sleeping for 2 seconds.
- `main` creates a new thread to run fetch_data and waits for it to complete using join.

**Key Differences**
- **Control**: With async/await, you have explicit control over when the task yields control back to the event loop. With threading, the operating system's scheduler decides when to switch between threads.
- **Resource Usage**: async/await is generally more efficient for I/O-bound tasks as it avoids the overhead of creating and managing multiple threads.
- **Complexity**: threading can be simpler for *CPU-bound* tasks but introduces complexity with thread safety and synchronization.