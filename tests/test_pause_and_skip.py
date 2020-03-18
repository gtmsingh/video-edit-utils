import cv2

from src.const import TEST_FILES_DIR
from src.pause_and_skip import pause_and_skip
from tests import BaseTest


class TestPauseAndSkip(BaseTest):
    def test_with_optimization(self):
        cv2.setUseOptimized(True)

        filename = "pause_and_skip"
        in_file = TEST_FILES_DIR / f"{filename}.mp4"
        out_file = TEST_FILES_DIR / f"{filename}_processed"
        pause_and_skip(in_file, out_file, 10)

    def test_without_optimization(self):
        cv2.setUseOptimized(False)

        filename = "pause_and_skip"
        in_file = TEST_FILES_DIR / f"{filename}.mp4"
        out_file = TEST_FILES_DIR / f"{filename}_processed"
        pause_and_skip(in_file, out_file, 10)
