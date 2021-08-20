class Base:
    """Class that provides global game functionality like update(). make sure to run super().__init__() to add it to the global list"""
    _instances = []
    _game      = None

    def __init__(self):
        self.__class__._instances.append(self)
    
    def _kill(self):
        """Call this instead of __del__ to make sure it's not referenced anymore"""
        self.__class__._instances.remove(self)
        del self

    def _update(self, delta):
        pass

    def _physics_update(self, delta):
        pass

    def _load_content(self):
        pass

    def _input(self):
        pass

    def _render(self):
        pass

    @classmethod
    def update_all(cls, delta):
        for instance in cls._instances:
            instance._update(delta)

    @classmethod
    def physics_update_all(cls, delta):
        for instance in cls._instances:
            instance._physics_update(delta)

    @classmethod
    def load_content_all(cls):
        for instance in cls._instances:
            instance._load_content()

    @classmethod
    def input_all(cls):
        for instance in cls._instances:
            instance._input()

    @classmethod
    def render_all(cls):
        for instance in cls._instances:
            instance._render()

    def get_by_type(cls, type):
        list = []
        for instance in cls._instances:
            if isinstance(instance, type):
                list.append(instance)
        return list