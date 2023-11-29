import unittest
from task import Task
from datetime import date


class MyTestCase(unittest.TestCase):
    # use all optional parameters
    object_one = Task("repair the warp manifolds",
                      is_complete=True, due_date=(2023, 11, 30))

    # give a due date but no completion status
    object_two = Task("bypass the power relay", due_date=(2023, 11, 30))

    # give completion status but no due date
    object_three = Task("stabilize containment field", is_complete=True)

    # use no optional parameters
    object_four = Task("scan for tachyon particles")

    object_five = Task("rewire eps conduits")

    def test_init(self):
        self.assertEqual(self.object_one.name, "repair the warp manifolds")
        self.assertEqual(self.object_one.is_complete, True)
        self.assertEqual(self.object_one.date, date(2023, 11, 30))

        self.assertEqual(self.object_two.name, "bypass the power relay")
        self.assertEqual(self.object_two.is_complete, False)
        self.assertEqual(self.object_two.date, date(2023, 11, 30))

        self.assertEqual(self.object_three.name, "stabilize containment field")
        self.assertEqual(self.object_three.is_complete, True)
        self.assertEqual(self.object_three.date, None)

        self.assertEqual(self.object_four.name, "scan for tachyon particles")
        self.assertEqual(self.object_four.is_complete, False)
        self.assertEqual(self.object_four.date, None)

    def test_get_name(self):
        self.assertEqual(self.object_one.get_name(),
                         "repair the warp manifolds")
        self.assertEqual(self.object_two.get_name(), "bypass the power relay")
        self.assertEqual(self.object_three.get_name(),
                         "stabilize containment field")
        self.assertEqual(self.object_four.get_name(),
                         "scan for tachyon particles")

    def test_get_completion_status(self):
        self.assertEqual(self.object_one.get_completion_status(), True)
        self.assertEqual(self.object_two.get_completion_status(), False)
        self.assertEqual(self.object_three.get_completion_status(), True)
        self.assertEqual(self.object_four.get_completion_status(), False)

    def test_get_date(self):
        self.assertEqual(self.object_one.get_date(), date(2023, 11, 30))
        self.assertEqual(self.object_two.get_date(), date(2023, 11, 30))
        self.assertEqual(self.object_three.get_date(), None)
        self.assertEqual(self.object_four.get_date(), None)

    def test_change_name(self):
        self.object_five.change_name("Re-Wire the EPS Conduits")
        self.assertEqual(self.object_five.get_name(),
                         "Re-Wire the EPS Conduits")

        with self.assertRaises(TypeError):
            self.object_five.change_name(3.14159)

    def test_change_date(self):
        self.object_five.change_date(2023, 12, 20)
        self.assertEqual(self.object_five.get_date(), date(2023, 12, 20))

        self.object_five.change_date("2023", "12", "20")  # wrong data type
        self.assertEqual(self.object_five.get_date(), date(2023, 12, 20))

        self.object_five.change_date(12, 20, 2023)  # wrong order for numbers
        self.assertEqual(self.object_five.get_date(), date(2023, 12, 20))

    def test_change_completion_status(self):
        self.object_five.change_completion_status(True)
        self.assertEqual(self.object_five.get_completion_status(), True)

        self.object_five.change_completion_status(True)
        self.assertEqual(self.object_five.get_completion_status(), True)

        self.object_five.change_completion_status(True)
        self.assertEqual(self.object_five.get_completion_status(), True)


if __name__ == '__main__':
    unittest.main(verbosity=4)
