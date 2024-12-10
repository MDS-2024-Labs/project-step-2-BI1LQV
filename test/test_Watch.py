import unittest
from reactive.observer.Watch import Watch
from reactive.observable import Reactive, Computed

class TestWatch(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('Watch test start')
    
    @classmethod
    def tearDownClass(self):
        print('Watch test end')

    def setUp(self):
        self.R1 = Reactive({"first_name": "John", "last_name": "Doe", "age": 20})
        self._executed_1 = False
        def watchLambda1():
            self.R1.name
            self.R1.age
            self._executed_1 = True
        self.W1 = Watch(watchLambda1)
        self._executed_1 = False

        self.full_name = Computed(lambda: self.R1.first_name + " " + self.R1.last_name)
        self._executed_2 = False
        def watchLambda2():
            self.full_name.value
            self._executed_2 = True
        self.W2 = Watch(watchLambda2)
        self._executed_2 = False

        

    def tearDown(self):
        self.R1 = None
        self.W1.stop()
        self.W1 = None
        self._executed_1 = False

        self.full_name = None
        self.W2.stop()
        self.W2 = None
        self._executed_2 = False
    
    def test_name(self):
        self.R1.first_name = "Mike"
        self.R1.last_name = "Smith"
        # watch effect should be triggered for reactive and computed
        self.assertTrue(self._executed_1)
        self.assertTrue(self._executed_2)

        self._executed_1 = False
        self._executed_2 = False
        self.W1.stop()
        self.W2.stop()
        self.R1.first_name = "Jane"
        self.R1.last_name = "Doe"
        # watch stoped, watch effect should not be triggered
        self.assertFalse(self._executed_1)
        self.assertFalse(self._executed_2)

    def test_age(self):
        self.R1.age = 25
        # age changed, the watch of reactive should be triggered
        self.assertTrue(self._executed_1)
        # age changed, the watch of computed name should not be triggered
        self.assertFalse(self._executed_2)

        self._executed_1 = False
        self._executed_2 = False
        self.W1.stop()
        self.W2.stop()
        self.R1.age = 45
        self.assertFalse(self._executed_1)
        self.assertFalse(self._executed_2)










    

