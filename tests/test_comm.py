import unittest

from ibapi import comm


class CommTestCase(unittest.TestCase):
    def test_make_msg(self):
        text = "ABCD"
        try:
            msg = comm.make_msg(0, False, text)
        except TypeError:
            msg = comm.make_msg(text)
        assert isinstance(msg, (bytes, bytearray))
        assert msg.endswith(text.encode())


if __name__ == "__main__":
    unittest.main()
