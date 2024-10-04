import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class TrackedAttributes:
    def __init__(self, attr1, attr2, attr3):
        self._attr1 = attr1
        self._attr2 = attr2
        self._attr3 = attr3

    @property
    def attr1(self):
        return self._attr1

    @attr1.setter
    def attr1(self, value):
        old_value = self._attr1
        self._attr1 = value
        logging.info(f'attr1 изменился: {old_value} -> {value}')

    @property
    def attr2(self):
        return self._attr2

    @attr2.setter
    def attr2(self, value):
        old_value = self._attr2
        self._attr2 = value
        logging.info(f'attr2 изменился: {old_value} -> {value}')

    @property
    def attr3(self):
        return self._attr3

    @attr3.setter
    def attr3(self, value):
        old_value = self._attr3
        self._attr3 = value
        logging.info(f'attr3 изменился: {old_value} -> {value}')


obj = TrackedAttributes(1, 'initial', [1, 2, 3])

obj.attr1 = 2
obj.attr2 = 'updated'
obj.attr3 = [4, 5, 6]
