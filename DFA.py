'''
A deterministic finite automaton M is a 5-tuple, (Q, Σ, δ, q0, F), consisting of

a finite set of states Q
a finite set of input symbols called the alphabet Σ
a transition function δ : Q × Σ → Q
an initial or start state q0
final state F
'''


class DFA:
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.F = F
    def __repr__(self):
        return "DFA"+self.Q
    def run(self, w):
        q = self.q0
        while w != "":
            q = self.delta[(q, w[0])]
            w = w[1:]
        return q in self.F


Q = {0, 1, 2}
sigma = {"a", "b"}
q0 = 0
F = {0, 1}
delta = {
    (0, "a"): 0,
    (0, "b"): 1,
    (1, "a"): 2,
    (1, "b"): 1,
    (2, "a"): 2,
    (2, "b"): 2,
}

D0 = DFA(Q, sigma, delta, q0, F)
print(D0.run("aaaba"))