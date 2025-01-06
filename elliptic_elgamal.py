class EllipticCurve: 
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def add(self, P, Q):
        if P == "O": return Q
        if Q == "O": return P
        if P == Q:
            s = (3 * P[0]**2 + self.a) * pow(2 * P[1], -1, self.p) % self.p
        else:
            s = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, self.p) % self.p
        x = (s**2 - P[0] - Q[0]) % self.p
        y = (s * (P[0] - x) - P[1]) % self.p
        return x, y

    def mul_helper(self, n, P, acc):
        if i == 1:
            return add(self, P, acc)
        else:
            mul_helper(self, n-1, P, add(self, P, acc))

    def mul(self, n, P):
        curve.mul_helper(self, n, P, "O")

# Example usage
curve = EllipticCurve(a=2, b=3, p=17)
P = (5, 1)
Q = (6, 3)
R = curve.add(P, Q)
Z = curve.mul(3, P)
print(f"P + Q = {R}")
print(f"P * 3 = {Z}")