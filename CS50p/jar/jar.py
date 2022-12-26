class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return ""

        return "🍪" * self.size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) > 0:
            self._capacity = capacity
        else:
            raise ValueError(f"That capacity is not valid")

    @size.setter
    def size(self, size):
        self._size = size
        if self.size > self.capacity:
            self._size = 12
            raise ValueError("Too many cookies in the jar")

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number of cookies not valid")
        if n > self.capacity:
            raise ValueError("Wanna add too many")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Wanna take too many")
        if n < 0:
            raise ValueError("Number of cookies not valid")
        else:
            self.size -= n


def main():
    jar = Jar()
    jar.deposit(5)

    print(jar.size)


if __name__ == "__main__":
    main()
