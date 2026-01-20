class FenwickTree:
    def __init__(self , max_size):
        self.size = max_size
        self.fenw = [None] * max_size

    def sum(self, idx):
        F = self.fenw
        running_sum = 0
        while idx > 0:
            running_sum += F[idx]
            right_most_set_bit = (idx & -idx)
            idx -= right_most_set_bit
        return running_sum

    def add(self , idx, X):
        F = self.fenw
        while idx < len(F):
            F[idx] += X
            right_most_set_bit = (idx & -idx)
            idx += right_most_set_bit

    def range_query(self, l, r):
        return sum(r) - sum(l - 1)

    def clear(self):
        self.fenw = [None] * self.size

    def add_range(self , L , R , val):
        self.add(L , val)
        self.add(R+1 , -val)

    def make_query(self, idx , L : list , R : list , val : list , m : int):
        if L[idx] <= R[idx]:
            self.add_range(L[idx] , R[idx] , val[idx])
        else:
            self.add_range(1 , R[idx] , val[idx])
            self.add_range(L[idx] , m , val[idx])


if __name__ == "__main__":
    
