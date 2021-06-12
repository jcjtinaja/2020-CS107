class FibonacciIterator:

    def __init__(self,n):
        self.n = n
        self.prev = 0
        self.curr = 1
        self.idx = 0
    
    def __next__(self):
        if self.idx >= self.n:
            raise StopIteration()
        else:
            self.curr, self.prev = self.curr + self.prev, self.curr
            self.idx += 1
        return self.curr
    
    def __iter__(self):
        return self

class Fibonacci:

    def __init__(self,n):
        self.n = n
    
    def __iter__(self):
        return FibonacciIterator(self.n)

if __name__ == '__main__':

    fib = Fibonacci(10)
    print(list(iter(fib)))