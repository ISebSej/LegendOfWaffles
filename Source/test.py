
class Master():
    _instances = []

    def __init__(self):
        self.__class__._instances.append(self)

    
    def _kill(self):
        """Call this instead of __del__ to make sure it's not referenced anymore"""
        self.__class__._instances.remove(self)
        del self

    @classmethod
    def update_all(cls):
        for instance in cls._instances:
            print(instance)
            instance.update()

class Slave(Master):
    
    def __init__(self):
        super().__init__()
        print("Hello")

    def update(self):
        print("update")



test = Slave()
print(test._instances)
test2 = Slave()
test3 = Slave()
print(test._instances)
test._kill()
print(test2._instances)
print("Done!")
Master.update_all()