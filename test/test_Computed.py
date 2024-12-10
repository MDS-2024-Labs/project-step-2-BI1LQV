import unittest
from reactive import Computed, Reactive
class TestComputed(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("computed test start")
    
    @classmethod
    def tearDownClass(self):
        print("computed test end")

    def setUp(self):
        self.reactiveImpl1 = Reactive({"name": "John", "age": 20})
        self.reactiveImpl2 = Reactive({"name": "Bell", "age": 40})
        self.computedImpl1 = Computed(lambda: self.reactiveImpl1.name + " " + self.reactiveImpl2.name)
        self.computedImpl2 = Computed(lambda: self.reactiveImpl1.age + self.reactiveImpl2.age)

    def tearDown(self):
        self.reactiveImpl1 = None
        self.reactiveImpl2 = None
        self.computedImpl1 = None
        self.computedImpl2 = None

    def test_getter(self):
        self.assertIsNone(self.computedImpl1.parent)
        self.assertIsNone(self.computedImpl2.address)
        self.assertEqual(self.computedImpl1.value, "John Bell")
        self.assertEqual(self.computedImpl2.value, 60)
    
    def test_setter(self):
        self.reactiveImpl1.name = "Yolo"
        self.assertEqual(self.reactiveImpl1.name, "Yolo")
        self.assertEqual(self.computedImpl1.value, "Yolo Bell")
        self.reactiveImpl2.age = 21
        self.assertEqual(self.reactiveImpl2.age, 21)
        self.assertEqual(self.computedImpl2.value, 41)
