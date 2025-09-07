# Binomial Coefficient Threaded Sum

This project was created for a course on Programming Secure, Parallel and Distributed Applications.
It computes binomial coefficients with Python using threads.  

---

## Instructions

### 1. Function Definition

Create a function that, given `n` and `k`, computes and returns:

$$
\binom{n}{k} = \frac{n!}{(n-k)! \, k!}
$$

In Python, this can be done efficiently with:

```python
import math

def choose(n, k):
    return math.comb(n, k)
```

---

### 2. Thread Pool Execution

* Use a `ThreadPoolExecutor` with `max_workers=3`.
* Submit tasks with `map()` for all values of `k` in the range **1 to N**.
* Use `N = 100000` (but start with a smaller test value like `N = 1000`).

---

### 3. Compute & Display Results

* Collect and sum the results from each thread.
* Display the sum of the partial results per thread.
* Finally, check the total against the theoretical value $2^n$.

---

## Hints

* Start with a smaller value of `N` (e.g., `N = 1000`) to confirm correctness and performance.
* Once it works, you can run it with `N = 100000`. Be aware:

  * Results are extremely large integers.
  * Computation can take time and memory.

---

## Example Run

```bash
python main.py -n 1000 -w 3
```