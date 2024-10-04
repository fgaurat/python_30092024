from Rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_get_surface(self):
        r = Rectangle(2,5)
        assert r.get_surface()==10
        
    def test_longueur(lf):
        r = Rectangle(3,5)
        assert r.longueur==2

    def test_get_largeur(self):
        r = Rectangle(2,5)
        assert r.largeur==5

    def test_set_longueur(self):
        r = Rectangle(2,5)
        r.longueur=(12)
        assert r.longueur==12

    def test_set_largeur(self):
        r = Rectangle(2,5)
        r.largeur=(12)
        assert r.largeur==12

    def test_set_longueur_largeur(self):
        r = Rectangle(2,5)
        r.longueur=(12)
        r.largeur=(12)
        assert r.longueur==12
        assert r.largeur==12

if __name__=='__main__':
    unittest.main()
