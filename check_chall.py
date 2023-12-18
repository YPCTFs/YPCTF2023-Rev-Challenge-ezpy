import unittest

from src import ezpy

FLAG = 'YPCTF{Wec0me_t0_th3_w0rld_0f_pytH0n}'

class ChallengeCheck(unittest.TestCase):
    def test_flag_check(self):
        self.assertTrue(ezpy.check_flag(FLAG))  # add assertion here


if __name__ == '__main__':
    unittest.main()
