import unittest
from task import Task, TaskCollection
from datetime import date


class MyTaskTester(unittest.TestCase):
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
    id_four = id(object_four)
    
    # object we'll use to change things
    object_five = Task("5th task")
    id_five = id(object_five)

    test_date = date.fromisoformat("2023-11-03")

    def test_init(self):
        self.assertEqual(self.object_one.name, "1st task")
        self.assertEqual(self.object_one.is_complete, True)
        self.assertEqual(self.object_one.date, self.test_date)
        self.assertEqual(self.object_one.unique_id, self.id_one)

        self.assertEqual(self.object_two.name, "2nd task")
        self.assertEqual(self.object_two.is_complete, False)
        self.assertEqual(self.object_two.date, self.test_date)
        self.assertEqual(self.object_two.unique_id, self.id_two)

        self.assertEqual(self.object_three.name, "3rd task")
        self.assertEqual(self.object_three.is_complete, True)
        self.assertEqual(self.object_three.date, None)
        self.assertEqual(self.object_three.unique_id, self.id_three)

        self.assertEqual(self.object_four.name, "4th task")
        self.assertEqual(self.object_four.is_complete, False)
        self.assertEqual(self.object_four.date, None)
        self.assertEqual(self.object_four.unique_id, self.id_four)

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

    def test_get_id(self):
        self.assertEqual(self.object_one.get_id(), self.id_one)
        self.assertEqual(self.object_three.get_id(), self.id_three)

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

    def test_remove_date(self):
        self.object_five.remove_date()
        self.assertEqual(self.object_five.get_date(), None)

    def test_change_completion(self):
        self.object_five.mark_complete()
        self.assertEqual(self.object_five.get_completion_status(), True)
        self.object_five.mark_incomplete()
        self.assertEqual(self.object_five.get_completion_status(), False)
        self.object_five.mark_complete()
        self.assertEqual(self.object_five.get_completion_status(), True)

    def test_to_csv(self):
        string_one = self.object_one.to_csv()
        self.assertEqual(string_one, f"{self.id_one},1st task,True,2023-11-03")


class MyTaskCollectionTester(unittest.TestCase):
    input_file = "test_input_data.csv"
    output_file = "test_output_data.csv"
    task_list = TaskCollection(input_file)

    def test_task_from_csv(self):
        test_csv_line = "id_number,1st task,True,2023-11-03"
        my_task = self.task_list.task_from_csv(test_csv_line)
        self.assertIsInstance(my_task, Task)
        self.assertEqual(my_task.get_name(),"1st task")
        self.assertEqual(my_task.get_completion_status(),True)
        self.assertEqual(my_task.get_date(),date.fromisoformat("2023-11-03"))

        test_csv_line = "id_number,2nd task,False,None"
        my_task = self.task_list.task_from_csv(test_csv_line)
        self.assertIsInstance(my_task, Task)
        self.assertEqual(my_task.get_name(), "2nd task")
        self.assertEqual(my_task.get_completion_status(), False)
        self.assertEqual(my_task.get_date(), None)

    def test_tasks_inside_task_list(self):
        test_one = Task("Temp Task")
        test_one.change_id(1234)
        self.assertEqual(test_one.get_id(), 1234)

        self.task_list.add_task(test_one)
        self.assertEqual(len(self.task_list.task_dictionary), 4)

        test_two = self.task_list.get_task(1234)
        self.assertEqual(test_two, test_one)

        self.task_list.delete_task(1234)
        self.assertEqual(len(self.task_list.task_dictionary), 3)

        test_three = Task("New Task!!")
        test_three.change_id(24601)
        self.task_list.add_task(test_three)
        self.assertEqual(len(self.task_list.task_dictionary), 4)

        self.task_list.update_csv(self.output_file)

if __name__ == '__main__':
    unittest.main(verbosity=4)
