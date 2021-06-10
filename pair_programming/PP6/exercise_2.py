class ExpFunction:

    def __init__(self,r):
        self.r = r

    def forward(self,x):
        return (x**self.r, self.r*(x**(self.r-1)))

if __name__ == '__main__':

    f = ExpFunction(4)
    fwd = f.forward(3)
    print(fwd)