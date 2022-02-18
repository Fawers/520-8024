import unittest

from cap2 import fluxos


class TestFluxos(unittest.TestCase):
    def test_media(self):
        for (notas, esperado) in [
            ((5, 5, 5), 5),
            ((10, 0), 5),
            ((2.5, 4, 9.4), 5.3),
            ((2, 2, 8, 10), 5.5),
            ((7, 8, 9, 10), 8.5),
            ((0, 1, 2, 3), 1.5),
        ]:
            with self.subTest(notas=notas):
                self.assertEqual(fluxos.media(*notas), esperado)

    def test_media_sem_notas(self):
        self.assertEqual(fluxos.media(), 0)

    def test_aprovado(self):
        esperado = 'Aprovado'
        for notas in [(7,),(7, 8, 9)]:
            with self.subTest(notas=notas):
                self.assertEqual(fluxos.status_escola(*notas), esperado)

    def test_recuperacao(self):
        esperado = 'Recuperação'
        for notas in [(5,),(4, 5, 6)]:
            with self.subTest(notas=notas):
                self.assertEqual(fluxos.status_escola(*notas), esperado)

    def test_reprovado(self):
        esperado = 'Reprovado'
        for notas in [(4.5,),(1, 2, 3)]:
            with self.subTest(notas=notas):
                self.assertEqual(fluxos.status_escola(*notas), esperado)
