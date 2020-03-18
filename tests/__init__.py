import logging
import unittest
from time import monotonic

logging.basicConfig(level=logging.DEBUG)


class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = logging.getLogger(self.id())
        self.initial_time = monotonic()

    def tearDown(self) -> None:
        self.logger.debug(
            f'Execution time of {self.id()}: {monotonic() - self.initial_time}'
        )
