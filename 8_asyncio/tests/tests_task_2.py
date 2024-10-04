import unittest
import os
import asyncio
import aiofiles
from scr.task_2 import main

class TestFileCreation(unittest.TestCase):

    def setUp(self):
        """Создаем временную директорию для тестов."""
        self.directory = 'templates_test'
        os.makedirs(self.directory, exist_ok=True)

    def tearDown(self):
        """Удаляем временную директорию после тестов."""
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        os.rmdir(self.directory)

    async def check_file_content(self):
        """Проверка содержимого файла."""

        for index in range(1, 11):
            filename = os.path.join(self.directory, f"file_{index}.txt")
            async with aiofiles.open(filename, 'r', encoding='UTF-8') as f:
                content = await f.read()
            expected_content = f'Это файл под номером - {index}'
            self.assertEqual(content, expected_content)

    def test_files_creation(self):
        """Тест создания файлов"""

        async def test_main():
            await main()

        asyncio.run(test_main())


if __name__ == '__main__':
    unittest.main()
