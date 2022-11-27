from pygame import mixer


class Composition:
    """
    Класс музыкальная композиция
    """
    def __init__(self, path: str):
        """
        Конструктор класса
        :param path: Путь до файла
        """
        self.path: str = path
        self.duration: int = int(mixer.Sound(path).get_length())
        self.name: str = path.split('/')[-1][0:-4]

    def __str__(self) -> str:
        """
        Информация об объекте класса
        :return: Строка с информацией
        """
        return f"Название: {self.name}; Путь: {self.path}; Длительность: {self.duration}"

    def __repr__(self) -> str:
        """
        Информация об объекте класса
        :return: Строка с информацией
        """
        return f"Название: {self.name}; Путь: {self.path}; Длительность: {self.duration}"
