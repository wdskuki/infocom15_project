providers & newcomer selection in distributed storage systems

---

k_i: file i split into k_i original blocks
n_i: file i's original k_i blocks encoding into n_i encoded blocks (n_i >= k_i) 
d_i: if any block of file i is lost, the newcomer should collected at least d_i blocks and then can regenerate lost block (k_i <= d_i < n_i)

N: all nodes num in DSS(N >> n_i)

---
fullConnectedGraph(N): get N node's full connected graph(FCG); return a matrix with zero link weight
randomLinkWeight(G, b1, b2): link weight uniform distributed between [b1, b2], M is a FCG, and return FCG

