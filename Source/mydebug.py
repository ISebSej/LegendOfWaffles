"""A simple File containing some debug print statements"""
import time
class mydebugger:
    def __init__(self, debugstate, frametime):
        self.debugstate = debugstate
        self.frametime  = frametime

    def prnt(self, *args):
        if self.debugstate:
            print(args)

    def tick(self):
        self.t = time.time()

    def tock(self, type):
        if self.frametime:
            deltat = time.time() - self.t
            if type == 0:
                print(deltat)
            elif type == 1:
                print(1/deltat)
