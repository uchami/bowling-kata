import codewars_test as test
from bowling import Bowling

@test.describe('XXX')
def XXX():
    @test.it('test01')
    def test01():
        bowling = Bowling()
        test.assert_equals(0, bowling.score()) 
    
    @test.it('test02')
    def test02():
        bowling = Bowling()
        bowling.roll(5)
        test.assert_equals(bowling.score(), 5) 
    
    @test.it('test03')
    def test03():
        bowling = Bowling()
        bowling.roll(1)
        bowling.roll(7)
        test.assert_equals(bowling.score(), 8) 
    
    @test.it('test04')
    def test04():
        bowling = Bowling()
        invalidQuantityPines = lambda: bowling.roll(11)
        test.expect_error('Cannot throw this many pines', invalidQuantityPines, exception=Exception)
        
    @test.it('test05')
    def test05():
        bowling = Bowling()
        invalidQuantityPines = lambda: bowling.roll(-1)
        test.expect_error('Cannot throw this many pines', invalidQuantityPines, exception=Exception)

    @test.it('test06')
    def test06():
        bowling = Bowling()
        invalidQuantityPines = lambda: bowling.roll(0.5)
        test.expect_error('Cannot throw this many pines', invalidQuantityPines, exception=Exception)