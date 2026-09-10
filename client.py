import math

class PoincareEmbedding:
    """
    Poincare Disk Hyperbolic Distance.
    d(u, v) = arcosh(1 + 2 * ||u - v||^2 / ((1 - ||u||^2) * (1 - ||v||^2))).
    Captures hierarchical trees in continuous hyperbolic space with minimal distortion.
    """
    def distance(self, u, v, eps=1e-5):
        sq_u = sum(x*x for x in u)
        sq_v = sum(x*x for x in v)
        sq_u = min(1.0 - eps, sq_u)
        sq_v = min(1.0 - eps, sq_v)
        sq_diff = sum((x - y)**2 for x, y in zip(u, v))

        alpha = 1.0 - sq_u
        beta = 1.0 - sq_v
        gamma = 1.0 + 2.0 * sq_diff / (alpha * beta)
        gamma = max(1.0, gamma)
        return math.log(gamma + math.sqrt(gamma*gamma - 1.0))
