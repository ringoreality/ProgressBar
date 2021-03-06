import sys
class ProgressBar:
    """progress bar class to visualise progress in a loop"""
    def __init__(self,start,end,width):
        self.start = start
        self.end = end - 1
        self.width = width
        self._set(0.)
    def show(self):
        sys.stdout.write('\r[%s%s] %.2f %%'%('-'*int(self.p*self.width),' '*(self.width-int(self.width*self.p)),100*self.p))
        sys.stdout.flush()
        if (self.p>=1):
            sys.stdout.write('\n')
            sys.stdout.flush()
    def _set(self, i):
        self.p = 1. * (i-self.start) / (self.end-self.start)
    def update(self, i):
        self._set(i)
        self.show()

pb = ProgressBar(0, 1000000, 40)
for i in range(0,1000000):
	pb.update(i)
