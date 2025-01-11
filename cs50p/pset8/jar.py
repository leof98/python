class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity Error')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError('Surpass capacity')
        elif n > self.capacity:
            raise ValueError('Surpass capacity')
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError('Number\'s too high')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
