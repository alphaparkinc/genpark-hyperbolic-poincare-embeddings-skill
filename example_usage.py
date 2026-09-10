from client import PoincareEmbedding

def main():
    print("=== Testing Poincaré Hyperbolic Geometry Engine ===")
    pe = PoincareEmbedding()

    root = [0.0, 0.0]
    leaf1 = [0.6, 0.0]
    leaf2 = [0.0, 0.6]

    d_root_leaf = pe.distance(root, leaf1)
    d_leaves = pe.distance(leaf1, leaf2)

    print(f"Distance root to leaf: {round(d_root_leaf, 4)}")
    print(f"Distance between leaves across tree: {round(d_leaves, 4)}")

    assert d_leaves > d_root_leaf
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
