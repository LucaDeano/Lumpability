def lump_neural_network(N):
    k, S, W, b, A = N['k'], N['S'], N['W'], N['b'], N['A']

    # Initialize the equivalence classes for the first layer
    S_prime = {0: {i: [s_i] for i, s_i in enumerate(S[0])}}

    # Initialize the dictionaries for O and W_tilde
    O = {}
    W_tilde = {}

    # Fill O and W_tilde for the first layer
    for Si in S_prime[0]:
        for sj in S[1]:
            O[(Si, sj)] = W[1][(S_prime[0][Si][0], sj)]
            W_tilde[(Si, (sj,))] = W[1][(S_prime[0][Si][0], sj)]

    # Initialize dictionaries for the output
    W_prime = {}
    b_prime = {}
    A_prime = {}

    # Process each layer
    for l in range(1, k):
        S_prime[l] = {}
        Sl = list(S[l])
        b_prime[l] = {}
        A_prime[l] = {}
        W_prime[l] = {}

        while Sl:
            s = Sl.pop(0)
            C = [s]
            b_prime[l][tuple(C)] = b[l][s]
            A_prime[l][tuple(C)] = A[l][s]

            for S_prime_l_minus_1 in S_prime[l - 1]:
                W_prime[l][(S_prime_l_minus_1, tuple(C))] = W_tilde[(S_prime_l_minus_1, (s,))]

            for s_prime in Sl[:]:
                rho_s_prime = b[l][s] / b[l][s_prime]
                consistent = True

                for S_prime_l_minus_1 in S_prime[l - 1]:
                    if rho_s_prime * O[(S_prime_l_minus_1, s_prime)] != O[(S_prime_l_minus_1, s)]:
                        consistent = False
                        break

                if consistent:
                    C.append(s_prime)
                    Sl.remove(s_prime)
                    S_prime[s_prime] = rho_s_prime

            S_prime[l][tuple(C)] = C

        if l + 1 < k: # if not the last layer
            for C in S_prime[l]:
                for s_prime in S[l + 1]:
                    O[(C, s_prime)] = sum(W[l + 1][(r, s_prime)] for r in C)
                    W_tilde[(C, (s_prime,))] = sum(S_prime.get(r, 1) * W[l + 1][(r, s_prime)] for r in C)

    return k, S_prime, W_prime, b_prime, A_prime

# Example neural network structure to be lumped
N = {
    'k': 4,
    'S': [{0, 1}, {2, 3}, {4, 5}, {6}],
    'W': {
        1: {(0, 2): 0.1, (1, 3): 0.2, (0, 3): 0.3, (1, 2): 0.4},
        2: {(2, 4): 0.5, (3, 4): 0.6, (2, 5): 1, (3, 5): 1.2},
        3: {(4, 6): 0.7, (5, 6): 0.8}
    },
    'b': {
        1: {2: 0.1, 3: 0.2},
        2: {4: 0.3, 5: 0.6},
        3: {6: 0.4}
    },
    'A': {
        1: {2: 'ReLU', 3: 'ReLU'},
        2: {4: 'ReLU', 5: 'ReLU'},
        3: {6: 'ReLU'}
    }
}

k, S_prime, W_prime, b_prime, A_prime = lump_neural_network(N)
#print(k)
print(S_prime)
#print(W_prime)
#print(b_prime)
#print(A_prime)
