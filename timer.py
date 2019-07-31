import threading
import time

def singleton(cls):
    obj = cls()
    # Always return the same object
    cls.__new__ = staticmethod(lambda cls: obj)
    # Disable __init__
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls

@singleton
class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.count = 10
    
    def setCount(self, count):
        self.count = count

    def getCount(self):
        return self.count

    def run(self):
        while self.count > 0 and not self.event.is_set():
            self.count -= 1
            self.event.wait(1)
    
    def stop(self):
        self.event.set()

@singleton
class Reset():
    def __init__(self):
        self.reset = False
    
    def setReset(self, mybool):
        self.reset = mybool

    def getReset(self):
        return self.reset