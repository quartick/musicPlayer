"""Модуль связного кольцевого списка"""


class LinkedListItem:
    """
    Узел связного списка
    """

    def __init__(self, data: object = None):
        """
        Метод для инициализации связного списка
        @param data: данные узла
        """
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """
        Метод для строкового представления
        @return: строковое представление
        """
        return str(self.data)

    @property
    def next_item(self) -> object:
        """
        Свойство для получения следующего узла
        @return: узел
        """
        return self.next

    @next_item.setter
    def next_item(self, value: object):
        """
        Сеттер для следующего узла
        @param value: узел
        """
        self.next = value
        if value:
            value.prev = self

    @property
    def previous_item(self):
        """
        Свойство для получения предыдущего узла
        @return: узел
        """
        return self.prev

    @previous_item.setter
    def previous_item(self, value):
        """
        Сеттер для предыдущего узла
        @param value: узел
        """
        self.prev = value
        if value:
            value.next = self


class LinkedList:
    """
    Класс связного кольцевого списка
    """

    def __init__(self, first_item: None | LinkedListItem = None):
        """
        Метод для инициализации связного списка
        @param first_item: первый элемент
        """
        self._last = None
        self.iter_num = 0
        if first_item:
            self.first_item = first_item
            self.head = first_item
            self.length = 1
            item = first_item
            while item.next_item != self.head:
                self.length += 1
                item = item.next_item
            self.head.previous_item = item
        else:
            self.first_item = None
            self.head = None
            self.length = 0

    @property
    def last(self) -> LinkedListItem | None:
        """
        Свойство для возвращения последнего узла списка
        :return: узел
        """
        if self.head is None:
            return None
        return self.head.previous_item

    @staticmethod
    def checking_node_type(item: object):
        """
        Метод для проверки объекта на принадлежность к типу LinkedListItem
        :param item: объект
        :return: узел
        """
        if isinstance(item, LinkedListItem):
            return item
        return LinkedListItem(item)

    def append_in_empty(self, node: LinkedListItem) -> None:
        """
        Метод для добавления узла в пустой список
        :param node: узел
        """
        self.first_item = node
        self.head = self.first_item
        self.head.next_item = self.first_item
        self.head.previous_item = self.first_item

    def append_left(self, item: object) -> None:
        """
        Метод для добавления узла в начало списка
        :param item: объект
        """
        node: LinkedListItem = self.checking_node_type(item)
        if not self.head:
            self.append_in_empty(node)
        else:
            node.previous_item = self.last
            node.next_item = self.head
            self.head = self.first_item = node
        self.length += 1

    def append_right(self, item: LinkedListItem) -> None:
        """
        Метод для добавления узла в конец списка
        :param item: объект
        """
        node = self.checking_node_type(item)
        if not self.head:
            self.append_in_empty(node)
        else:
            self.last.next_item = node
            node.next_item = self.head
        self.length += 1

    def append(self, item):
        """
        Алиас для добавления справа
        :param item: объект
        """
        self.append_right(item)

    def remove(self, item: LinkedListItem | object) -> int:
        """
        Метод для удаления узла
        :param item: узел или объект
        :return: индекс удаленного элемента
        """
        temp_item = self.head
        for _ in range(self.length):
            if temp_item.data == item or temp_item == item:
                if self.length == 1:
                    self.head = None
                    self.length = 0
                    return _
                if temp_item == self.head:
                    last = self.last
                    self.head = temp_item.next_item
                    self.head.previous_item = last
                    self.length -= 1
                    return _
                temp_item.previous_item.next_item = temp_item.next_item
                self.length -= 1
                return _
            temp_item = temp_item.next_item
        raise ValueError

    def insert(self, previous: int, item: object):
        """
        Метод для вставки элеента по индексу
        :param previous: элемент после которого надо вставить
        :param item: элемент для вствки
        """
        item = self.checking_node_type(item)
        temp_item = self.head
        for _ in range(previous):
            temp_item = temp_item.next_item
        item.previous_item = temp_item.previous_item
        item.next_item = temp_item
        if previous == 0:
            self.head = item
            self.first_item = item
        self.length += 1

    def __len__(self) -> int:
        """
        Метод для получения длины списка
        :return: длина списка
        """
        return self.length

    def __iter__(self):
        """
        Метод для поддержки итерации
        :return: список
        """
        temp_item = self.head
        for _ in range(self.length):
            yield temp_item
            temp_item = temp_item.next_item

    def __getitem__(self, index: int) -> object:
        """
        Метод для получения элемента по индексу
        :param index: индекс
        :return: элемент
        """
        temp_item = self.head
        if index >= self.length or index < -self.length:
            raise IndexError
        if index < 0:
            index = self.length - abs(index)
        for i in range(self.length):
            if i == index:
                return temp_item
            temp_item = temp_item.next_item

    def __contains__(self, item: object):
        """
        Поддержка оператора in
        :param item: Элемент связного списка
        :return: True/False
        """
        for i in range(self.__len__()):
            if self.__getitem__(i) == item:
                return True
        return False

    def __reversed__(self):
        """
        Метод для переворота списка
        :return: перевернутый список
        """
        return reversed([item.data for item in self])

    def __repr__(self):
        """
        Метод для отображения списка
        :return: строковое представление списка
        """
        return f"[{', '.join(str(i.data) for i in self)}]"

    @last.setter
    def last(self, value: object):
        """
        сеттер для последнего элемента
        :param value: объект
        """
        self._last = value
