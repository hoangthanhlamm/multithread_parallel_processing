# Multi-thread Parallel Processing

Library support parallel processing with multi-thread.

## Installation
```shell
$ pip3 install miltithread_parallel_processing
```

## Example

Example job to calculate sum of the squares of the first billion natural numbers.

```python
from multithread_processing.base_job import BaseJob


class SumSquaresJob(BaseJob):
    def __init__(self, batch_size=1000, max_workers=4):
        self.n = 10 ** 9
        work_iterable = range(self.n)
        super().__init__(work_iterable, batch_size, max_workers)

    def _start(self):
        self.sum = 0

    def _execute(self):
        self.batch_executor.execute(
            self.work_iterable,
            self._execute_batch,
            total_items=self.n
        )

    def _execute_batch(self, works):
        _sum = 0
        for i in works:
            _sum += i * i
        self.sum += _sum

    def _end(self):
        print(f"Sum of the squares of the first {self.n} natural numbers: {self.sum}")
        self.batch_executor.shutdown()


if __name__ == "__main__":
    job = SumSquaresJob(
        batch_size=10000,
        max_workers=10
    )
    job.run()
```
