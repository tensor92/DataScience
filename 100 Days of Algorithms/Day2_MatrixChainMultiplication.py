# optimization problem that can be solved using dynamic programming.
# Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices.
# The problem is not to perform the multiplications, but to decide the sequence of the matrix multiplications.

#if A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix, then

#computing (AB)C needs (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations, (BETTER)
#computing A(BC) needs (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.

# Optimal Substructure (Hence Recursion)
# Overlapping Subproblems (Hence due to this and above we use Dynamic Programming)

# Time Complexity: O(n^3)
# Auxiliary Space: O(n^2)

def mult(chain):
    n = len(chain)

    # single matrix chain has zero cost
    aux = {(i, i): (0,) + chain[i] for i in range(n)}
    # i: length of subchain
    for i in range(1, n):
        # j: starting index of subchain
        for j in range(0, n - i):
            best = float('inf')
            # k: splitting point of subchain
            for k in range(j, j + i):
                # multiply subchains at splitting point
                lcost, lname, lrow, lcol = aux[j, k]
                rcost, rname, rrow, rcol = aux[k + 1, j + i]
                cost = lcost + rcost + lrow * lcol * rcol
                var = '(%s%s)' % (lname, rname)
                # pick the best one
                if cost < best:
                    best = cost
                    aux[j, j + i] = cost, var, lrow, rcol


    return dict(zip(['cost', 'order', 'rows', 'cols'], aux[0, n - 1]))

mult([('A', 10, 20), ('B', 20, 30), ('C', 30, 40)])




