### Docker Compose
Docker Compose is a tool that helps you define and run multi-container Docker applications. Think of it as a blueprint for your entire application stack.

### I/O-Bound Tasks ⏳

These tasks mostly **wait for data transfer**, rather than active processing.

**Examples:**

* **Saving a large file** to disk.
* **Streaming video** over the internet.
* **Sending data** to a printer.
* **Reading user input** from a keyboard.

***

### CPU-Bound Tasks 🧠

These tasks constantly **perform calculations** and are limited by processor speed.

**Examples:**

* **Running complex analytics** on a large dataset.
* **Cracking a password** through brute force.
* **Training a machine learning model**.
* **Compiling source code** into an executable.ystems where different agents might be reasoning, planning, or executing distinct sub-tasks concurrently.


---

## Multithreading 🧵

* **What it is:** One program, many tasks running **concurrently** (CPU rapidly switches). Shares memory.
* **Best for:** **I/O-bound tasks** (waiting for data), e.g., downloading files, web Browse.

---

## Multiprocessing 👯

* **What it is:** Many independent programs running **in parallel** (true simultaneous execution). Separate memory.
* **Best for:** **CPU-bound tasks** (heavy calculations), e.g., video rendering, machine learning training.

1)  
docker compose up
docker compose stop