import unittest
from swords import SwordsSecond

class TestSwordsSecond(unittest.TestCase):
    def setUp(self):
        # Ініціалізуємо дані для тестів
        self.sword1 = SwordsSecond("Excalibur", "Epic", 20, 50)
        self.sword2 = SwordsSecond("Sting", "Blue", 15, 40)

    def test_attack_successful(self):
        # Перевіряємо, чи атака пройшла успішно
        damage = 10
        expected_vitality = self.sword2.vitality - damage
        self.sword1.attack(self.sword2)
        self.assertEqual(self.sword2.vitality, expected_vitality)

    def test_attack_unsuccessful(self):
        # Перевіряємо, що атака пропущена, якщо передано не підходящий об'єкт
        result = self.sword1.attack("Enemy")
        self.assertIn("промахнулись", result)

if __name__ == '__main__':
    unittest.main()
