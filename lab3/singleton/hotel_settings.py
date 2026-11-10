
class HotelSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.name = "Grand Hotel"
            self.check_in = "14:00"
            self.check_out = "12:00"
            self._initialized = True

    def show_info(self):
        print("Отель:", self.name)
        print("Заселение:", self.check_in)
        print("Выселение:", self.check_out)
