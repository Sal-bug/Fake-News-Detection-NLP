import numpy as np
import sys

embedding_path = sys.argv[1] # '/data/medg/misc/jindi/nlp/embeddings/counter-fitted-vectors.txt'

embeddings = []
with open(embedding_path, 'r') as ifile:
    for line in ifile:
        embedding = [float(num) for num in line.strip().split()[1:]]
        embeddings.append(embedding)
embeddings = np.array(embeddings)
print(embeddings.T.shape)
norm = np.linalg.norm(embeddings, axis=1, keepdims=True)
embeddings = np.asarray(embeddings / norm, "float32")

# The following may cause stack overflow problem.
# product = np.dot(embeddings, embeddings.T)
# The following function may tackle the problem ???
def chunk_gemm(A, B, csize):
    out = np.empty((A.shape[0],B.shape[1]), dtype=A.dtype)
    for i in range(0, A.shape[0], csize):
        iend = i+csize
        for j in range(0, B.shape[1], csize):
            jend = j+csize
            out[i:iend, j:jend] = np.dot(A[i:iend], B[:,j:jend])
    return out
product = chunk_gemm(embeddings, embeddings.T, 1000)
print(embeddings.T.shape)
np.save(('cos_sim_counter_fitting.npy'), product)
