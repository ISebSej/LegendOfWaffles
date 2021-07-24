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

    def tock(self):
        if self.frametime:
            print(time.time() - self.t)
