def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i]-y[i])
    return res

def jaccard_dist(x, y):
    x_set = set(x)
    y_set = set(y)
    jac_dist = len(x_set.intersection(y_set)) / len(x_set.union(y_set))
    return 1-jac_dist

def cosine_sim(x, y):
    dot_product = 0
    nx = 0
    ny = 0

    for a, b in zip(x,y):
        dot_product += a*b
        nx += a**2
        ny += b**2

    return dot_product/((nx * ny) **0.5)

# Feel free to add more
