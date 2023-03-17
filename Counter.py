class Counter:

    def start_from(self, value=0):
        self.value = value
        print(self.value)

    def increment(self, value):
        value += 1
        print(value)

    def display(self, value=0):
        value += 0
        print(f'Текущее значение счетчика = {value + 1}')

    def reset(self, suma=1):
        self.suma = 0
        print(self.suma)

c1 = Counter()
c1.start_from()
c1.increment(0)
c1.display(0)
c1.increment(1)
c1.display(1)
c1.reset()
c1.display(-1)

c2 = Counter()
c2.start_from(3)
c2.display(2)
c2.increment(3)
c2.display(3)

