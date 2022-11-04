# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from multithread_processing.executors.batch_work_executor import BatchWorkExecutor
from multithread_processing.utils.logging_utils import get_logger

logger = get_logger('BaseJob')


class BaseJob(object):
    def __init__(self, work_iterable, batch_size: int, max_workers: int):
        self.work_iterable = work_iterable
        self.batch_executor = BatchWorkExecutor(batch_size, max_workers)

    def run(self):
        try:
            self._start()
            self._execute()
        except Exception as e:
            logger.error(e)

        finally:
            self._end()

    def _start(self):
        # Declare general variables and preprocess data
        pass

    def _execute(self):
        # Divide the work and assign it to the threads
        self.batch_executor.execute(
            self.work_iterable,
            self._execute_batch,
            total_items=len(self.work_iterable)
        )

    def _execute_batch(self, works):
        # Execute the work by batch
        pass

    def _end(self):
        # End task, export results or close connections
        self.batch_executor.shutdown()
