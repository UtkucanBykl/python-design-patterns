class Singleton(type):

    _instance = None

    def __call__(self):
        if not self._instance:
            print('Create new instance')
            self._instance = super().__call__()
        print('You have already instance')
        return self._instance


class DatabaseConnect(metaclass=Singleton):
    def connect(self):
        pass

if __name__ == '__main__':
    db1 = DatabaseConnect() # Create new instance
    db2 = DatabaseConnect() # You have already instance

    print(db1 is db2)
