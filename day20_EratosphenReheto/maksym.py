class Eratosphen:
    def __init__(self , n):
        self.array = [1] * n
        self.n = n
        self.is_prime = [1] * self.n
        self.is_prime[0] = self.is_prime[1] = 0
        self.lp = [0] * (n + 1)
        self.primes = []

    def calc_number_of_factor(self):
        """Calculate number of factors and return which are prime"""
        primes = []
        for i in range(2,int( (self.n)**(0.5) )+1 ):
            for j in range(i , self.n , i):
                self.array[j] += 1
                if j == i and self.array[j] == 2:
                    primes.append(j)
        return primes

    def find_primes(self):
        limit = int(self.n**0.5) + 1

        for i in range(2, limit):
            if self.is_prime[i]:
                self.is_prime[i*i : self.n : i] = [0] * len(self.is_prime[i*i : self.n : i])

        return [num for num, prime in enumerate(self.is_prime) if prime]

    def euler_search(self):

        for i in range(2, self.n + 1):
            if self.lp[i] == 0:
                self.lp[i] = i
                self.primes.append(i)

            for p in self.primes:
                x = i * p

                # Якщо вийшли за межі діапазону - зупиняємось
                if x > self.n:
                    break

                # Позначаємо найменший дільник для складеного числа x
                self.lp[x] = p

                # Якщо i ділиться на p без остачі, то p є найменшим дільником i.
                # Це означає, що для наступних чисел (i * наступне_p)
                # найменшим дільником все одно буде p, а не "наступне_p".
                # Тому ми перериваємо цикл, щоб уникнути повторного викреслення.
                if i % p == 0:
                    break

        return self.primes


if __name__ == "__main__":
    print(Eratosphen(100).euler_search())
