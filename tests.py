import unittest
from unittest.mock import MagicMock, Mock, patch

import main


class TestClick(unittest.TestCase):
    @patch('pyautogui.moveTo')
    @patch('pyautogui.click')
    def test_click_calls_pyautogui_functions(self, mock_click, mock_moveTo):
        main.click(100, 200)
        mock_moveTo.assert_called_once_with(100, 200)
        mock_click.assert_called_once()


class TestCheckScreen(unittest.TestCase):
    @patch('pyautogui.locateOnScreen')
    def test_check_screen_returns_true_if_image_found(self, mock_locateOnScreen):
        mock_locateOnScreen.return_value = Mock(left=100, top=200, width=30, height=40)
        self.assertTrue(main.check_screen())

    @patch('pyautogui.locateOnScreen')
    def test_check_screen_returns_false_if_image_not_found(self, mock_locateOnScreen):
        mock_locateOnScreen.return_value = None
        self.assertFalse(main.check_screen())


class TestStopButton(unittest.TestCase):
    @patch('main.Label', autospec=True)
    def test_stop_button_sets_running_job_to_false(self, mock_label):
        main.running_job = True
        main.win.protocol = MagicMock()
        main.win.protocol.return_value = True  # Assume the application is still alive
        main.stop_button()
        self.assertFalse(main.running_job)

    @patch('main.Label', autospec=True)
    @patch('main.Tk.destroy', autospec=True)
    def test_stop_button_does_not_create_label_if_application_destroyed(self, mock_destroy, mock_label):
        main.running_job = True
        main.win.protocol = MagicMock()
        main.win.protocol.return_value = False  # Assume the application is destroyed
        main.stop_button()



class TestRunThreaded(unittest.TestCase):
    def test_run_threaded_starts_thread_and_sets_running_job_to_true(self):
        main.running_job = False
        main.run_threaded(lambda: None)
        self.assertTrue(main.running_job)


if __name__ == '__main__':
    unittest.main()
