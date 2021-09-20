# import codewars_test as test
import unittest
from bowling import Bowling

class XXX(unittest.TestCase):
    def test01_when_starting_a_game_must_have_an_score_of_zero(self):
        bowling = Bowling()
        self.assertEqual(0, bowling.score()) 
    
    def test02_when_in_first_roll_score_equals_the_amount_of_pines_rolled(self):
        bowling = Bowling()
        bowling.roll(5)
        self.assertEqual(bowling.score(), 5) 

    def test03_cannot_roll_an_amount_of_pines_grater_than_10(self):
        bowling = Bowling()
        with self.assertRaises(Exception) as cm:
            bowling.roll(11)
        self.assertEqual('Cannot throw this many pines', str(cm.exception))
        
    def test04_cannot_roll_a_negative_amount_of_pines(self):
        bowling = Bowling()
        with self.assertRaises(Exception) as cm:
            bowling.roll(-1)
        self.assertEqual('Cannot throw this many pines', str(cm.exception))

    def test05_cannot_roll_a_non_integer_number_of_pines(self):
        bowling = Bowling()
        with self.assertRaises(Exception) as cm:
            bowling.roll(0.5)
        self.assertEqual('Cannot throw this many pines', str(cm.exception))

    def test06_when_in_second_roll_score_equals_the_sum_of_the_first_two_rolls(self):
        bowling = Bowling()
        bowling.roll(1)
        bowling.roll(7)
        self.assertEqual(bowling.score(), 8) 

    def test07_sum_of_first_two_non_strike_rolls_cannot_add_up_over_10(self):
        bowling = Bowling()
        bowling.roll(5)
        with self.assertRaises(Exception) as cm:
            bowling.roll(7)
        self.assertEqual('Cannot throw this many pines', str(cm.exception))

    def test08_when_rolls_10_pines_Must_end_the_running_frame(self):
        bowling = Bowling()
        bowling.roll(10)
        bowling.roll(5)
        self.assertEqual(bowling.score(), 20)

    def test09(self):
        bowling = Bowling()
        bowling.roll(4)
        bowling.roll(5)
        bowling.roll(5)
        self.assertEqual(bowling.score(), 14)

    def test10_Bonus_for_spare_doubles_next_roll(self):
        bowling = Bowling()
        bowling.roll(5)
        bowling.roll(5)
        bowling.roll(5) 
        self.assertEqual(bowling.score(), 20)
    
    def test11_Bonus_for_strike_doubles_next_two_rolls(self):
        bowling = Bowling()
        bowling.roll(10)
        bowling.roll(5)
        bowling.roll(4) 
        self.assertEqual(bowling.score(), 28)
    
    #Rompe el planteo actual porque cruza 3 frames y el codigo solo mira el frame anterior.
    # @unittest.skip("proximo test")
    def test12(self):
        bowling = Bowling()
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(4) 
        self.assertEqual(bowling.score(), 42)


if __name__ == '__main__':
    unittest.main()