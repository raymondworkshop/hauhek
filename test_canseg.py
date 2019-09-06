#import pytest
import unittest
import time

#TODO: how to call argparse

from ..canseg import segmentation

class CansegTestCase(unittest.TestCase):
    def setUp(self):
        self.query = '呢幾日天氣成日變，你要小心保重身體'

    def tearDown(self):
        time.sleep()

    def test_canseq(sent):
        output = segmentation()
        print(output)
        assert true

if __name__ == "__main__":
    unittest.main()