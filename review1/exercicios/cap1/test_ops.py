import unittest

from cap1 import ops

class TestOperadores(unittest.TestCase):
    def test_menor_igual(self):
        for (a, b) in [
            (3, 3),
            (0, 10),
            (5, 6),
            (-1000, 1000),
        ]:
            with self.subTest(a=a, b=b):
                self.assertTrue(ops.menor_igual(a, b))

    def test_diferente(self):
        for (a, b) in [
            (0, 10),
            (5, 6),
            (-1000, 1000),
        ]:
            with self.subTest(a=a, b=b):
                self.assertTrue(ops.diferente(a, b))

        self.assertFalse(ops.diferente(0, 0))

    def test_and(self):
        for (premissas, esperado) in [
            ((True, True, True), True),
            ((True, True, False), False),
            ((False,), False),
            ((False, True), False),
            ((True, False), False),
        ]:
            with self.subTest(premissas=premissas):
                self.assertEqual(ops.op_and(*premissas), esperado)

    def test_or(self):
        for (premissas, esperado) in [
            ((True, True, True), True),
            ((False, False, False), False),
            ((False,), False),
            ((False, True), True),
            ((True, False), True),
        ]:
            with self.subTest(premissas=premissas):
                self.assertEqual(ops.op_and(*premissas), esperado)

    def test_not(self):
        self.assertFalse(ops.op_not(True))
        self.assertTrue(ops.op_not(False))
