class ExceptionPrintSendData(Exception):
    """Класс исключения при отправке данных принтеру"""

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception("принтер не отвечает")

    def send_to_print(self, data):
        return True


if __name__ == '__main__':
    p = PrintData()

    try:
        p.print("123")
    except ExceptionPrintSendData:
        print("Ошибка печати")