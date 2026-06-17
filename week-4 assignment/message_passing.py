
import torch

"""
Simple Message Passing with adjacency matrix.
x: (N, F) node features
A: (N, N) adjacency matrix (0/1 or weighted)
"""

def message_passing_layer(x, A, W=None, add_self_loops=True):
    N = A.shape[0]

    if add_self_loops:
        A = A + torch.eye(N)

    deg = A.sum(dim=1, keepdim=True)
    deg_inv = torch.pow(deg + 1e-8, -1)

    A_norm = A * deg_inv  # row-normalized adjacency

    if W is None:
        W = torch.eye(x.shape[1])

    x_transformed = x @ W
    out = A_norm @ x_transformed
    return out


if __name__ == "__main__":
    x = torch.randn(4, 3)
    A = torch.tensor([
        [0,1,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [0,1,0,0]
    ], dtype=torch.float32)

    out = message_passing_layer(x, A)
    print(out)
