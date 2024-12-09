import unittest
from reactive import Reactive
class TestReactive(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("reactive test start")
    
    @classmethod
    def tearDownClass(self):
        print("reactive test end")

    def setUp(self):
        self.reactiveImpl1 = Reactive({"name": "John", "age": 20})

    def tearDown(self):
        self.reactiveImpl1 = None

    def test_getter_name(self):
        self.assertEqual(self.reactiveImpl1.name, "John")
    
    def test_setter_name(self):
        self.reactiveImpl1.name = "Yolo"
        self.assertEqual(self.reactiveImpl1.name, "Yolo")
    
    def test_getter_age(self):
        self.assertEqual(self.reactiveImpl1.age, 20)
    
    def test_setter_age(self):
        self.reactiveImpl1.age = 21
        self.assertEqual(self.reactiveImpl1.age, 21)
