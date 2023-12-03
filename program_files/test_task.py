import unittest
from task import Task
from datetime import date


class MyTestCase(unittest.TestCase):
    # use all optional parameters
    object_one = Task("1st task", is_complete=True, due_date="2023-11-03")
    id_one = id(object_one)

    # give a due date but no completion status
    object_two = Task("2nd task", due_date="2023-11-03")
    id_two = id(object_two)

    # give completion status but no due date
    object_three = Task("3rd task", is_complete=True)
    id_three = id(object_three)

    # use no optional parameters
    object_four = Task("4th task")
    id_one = id(object_one)
    
    # object we'll use to change things
    object_five = Task("5th task")
    id_one = id(object_one)

    file_name = "testing.csv"
    test_date = date.fromisoformat("2023-11-03")

    def test_init(self):
        self.assertEqual(self.object_one.name, "1st task")
        self.assertEqual(self.object_one.is_complete, True)
        self.assertEqual(self.object_one.date, self.test_date)

        self.assertEqual(self.object_two.name, "2nd task")
        self.assertEqual(self.object_two.is_complete, False)
        self.assertEqual(self.object_two.date, self.test_date)

        self.assertEqual(self.object_three.name, "3rd task")
        self.assertEqual(self.object_three.is_complete, True)
        self.assertEqual(self.object_three.date, None)

        self.assertEqual(self.object_four.name, "4th task")
        self.assertEqual(self.object_four.is_complete, False)
        self.assertEqual(self.object_four.date, None)

    def test_get_name(self):
        self.assertEqual(self.object_one.get_name(),
                         "1st task")
        self.assertEqual(self.object_two.get_name(), "2nd task")
        self.assertEqual(self.object_three.get_name(),
                         "3rd task")
        self.assertEqual(self.object_four.get_name(),
                         "4th task")

    def test_get_completion_status(self):
        self.assertEqual(self.object_one.get_completion_status(), True)
        self.assertEqual(self.object_two.get_completion_status(), False)
        self.assertEqual(self.object_three.get_completion_status(), True)
        self.assertEqual(self.object_four.get_completion_status(), False)

    def test_get_date(self):
        self.assertEqual(self.object_one.get_date(), self.test_date)
        self.assertEqual(self.object_two.get_date(), self.test_date)
        self.assertEqual(self.object_three.get_date(), None)
        self.assertEqual(self.object_four.get_date(), None)

    def test_change_name(self):
        self.object_five.change_name("Re-Wire the EPS Conduits")
        self.assertEqual(self.object_five.get_name(),
                         "Re-Wire the EPS Conduits")

        with self.assertRaises(TypeError):
            self.object_five.change_name(3.14159)

    def test_change_date(self):
        self.object_five.change_date("2023-12-20")
        self.assertEqual(self.object_five.get_date(),
                         date.fromisoformat("2023-12-20"))

        with self.assertRaises(TypeError):
            self.object_five.change_date(2023-12-20)  # wrong data type

    def test_change_completion_status(self):
        self.object_five.change_completion_status(True)
        self.assertEqual(self.object_five.get_completion_status(), True)

        self.object_five.change_completion_status(True)
        self.assertEqual(self.object_five.get_completion_status(), True)

        self.object_five.change_completion_status(True)
        self.assertEqual(self.object_five.get_completion_status(), True)


if __name__ == '__main__':
    unittest.main(verbosity=4)
