from unittest import TestCase
import Misc_function

class UnitTest(TestCase):

# if r[0] > r[1]
    def test_perc1(self):
        self.assertEqual(Misc_function.calc_percentage([18, 9]), 97.5)
    
# if r[1] > r[0]
    def test_perc2(self):
        self.assertEqual(Misc_function.calc_percentage([9, 18]), 2.5)

    def test_midpoint(self):
        self.assertEqual(Misc_function.midpoint(0, 4, 0, 8), (0, 6))

    def test_dist_for(self):
        self.assertEqual(Misc_function.distance_formula(4, 0, 0, 3), 5)

    def test_in_circle(self):
        self.assertEqual(Misc_function.in_circle(2, 3, 5, 0, 0), True)

# if x1 = x2, and y1 > y_circle
    def test_angle_formula1(self):
        self.assertEqual(Misc_function.angle_formula(2, 3, 2, 7, 4, 0), 270)

#if x1 = x2, and y1 !> y_circle
    def test_angle_formula2(self):
        self.assertEqual(Misc_function.angle_formula(2, 3, 2, 7, 4, 4), 90)

#if x1 != x2, and x1 < x_circle
    def test_angle_formula3(self):
        self.assertEqual(Misc_function.angle_formula(4, 3, 2, 7, 6, 4), 243.43494882292202)

#if x1 != x2 and x1 > x_circle ang < 0
    def test_angle_formula4(self):
        self.assertEqual(Misc_function.angle_formula(8, 6, 5, 3, 2, 9), 315.0)

#if x1 != x2 and x1 = x_circle
    def test_angle_formula5(self):
        self.assertEqual(Misc_function.angle_formula(2, 6, 5, 3, 2, 9), 45.0)

#if x1 != x2 and x1 > x_circle ang !< 0
    def test_angle_formula6(self):
        self.assertEqual(Misc_function.angle_formula(3, 6, 5, 3, 2, 9), 56.309932474020215)

#for proximity
    def test_prox_1(self):
        self.assertEqual(Misc_function.proximity(5, 8, 12, 22), True)

    def test_prox_2(self):
        self.assertEqual(Misc_function.proximity(2, 5, 12, 4), True)

    def test_prox_3(self):
        self.assertEqual(Misc_function.proximity(6, 3, 13, 5), True)
    
    def test_prox_4(self):
        self.assertEqual(Misc_function.proximity(13, 25, 18, 5), True)

    def test_prox_5(self):
        self.assertEqual(Misc_function.proximity(3, 8, 13, 6), True)
    
    def test_prox_6(self):
        self.assertEqual(Misc_function.proximity(21, 24, 18, 4), True)

    def test_prox_7(self):
        self.assertEqual(Misc_function.proximity(42, 20, 31, 16), True)

    def test_prox_8(self):
        self.assertEqual(Misc_function.proximity(23, 13, 34, 7), False)

    def test_prox_9(self):
        self.assertEqual(Misc_function.proximity(21, 24, 15, 3), True)

    def test_prox_10(self):
        self.assertEqual(Misc_function.proximity(42, 15, 31, 11), True)

    def test_prox_11(self):
        self.assertEqual(Misc_function.proximity(9, 23, 34, 11), True)

# for angle_inside
    def test_ang_in1(self):
        self.assertEqual(Misc_function.angle_inside(220, 135, 220), False)

    def test_ang_in2(self):
        self.assertEqual(Misc_function.angle_inside(220, 135, 135), False)

    def test_ang_in3(self):
        self.assertEqual(Misc_function.angle_inside(220, 135, 240), True)

    def test_ang_in4(self):
        self.assertEqual(Misc_function.angle_inside(220, 135, 360), True)

    def test_ang_in5(self):
        self.assertEqual(Misc_function.angle_inside(220, 135, 180), False)

    def test_ang_in6(self):
        self.assertEqual(Misc_function.angle_inside(220, 135, 90), True)

    def test_ang_in7(self):
        self.assertEqual(Misc_function.angle_inside(220, 135, 0), True)

    def test_ang_in8(self):
        self.assertEqual(Misc_function.angle_inside(75, 180, 130), True)
    
    def test_ang_in9(self):
        self.assertEqual(Misc_function.angle_inside(75, 180, 20), False)

    def test_ang_in10(self):
        self.assertEqual(Misc_function.angle_inside(75, 180, 240), False)

    def test_ang_in11(self):
        self.assertEqual(Misc_function.angle_inside(220, 220, 240), False)

    def test_ang_in13(self):
        self.assertEqual(Misc_function.angle_inside(220, 240, 240), False)

    def test_ang_in14(self):
        self.assertEqual(Misc_function.angle_inside(220, 240, 220), False) 

#for angle_avg
    def test_ang_av1(self):
        self.assertEqual(Misc_function.angle_avg(230, 240), 235)

    def test_ang_av2(self):
        self.assertEqual(Misc_function.angle_avg(230, 230), 230)

    def test_ang_av3(self):
        self.assertEqual(Misc_function.angle_avg(270, 90), 0)

    def test_ang_av4(self):
        self.assertEqual(Misc_function.angle_avg(220, 150), 5.0)

    def test_ang_av5(self):
        self.assertEqual(Misc_function.angle_avg(170, 45), 287.5)       

 



