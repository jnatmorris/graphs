import networkit as nk
import time

# Parameters
n = 1_000_000       # Number of nodes
avg_degree = 20     # Expected average degree

# Generate degree sequence
degree_sequence = [avg_degree] * n

# Initialize Chung-Lu generator
generator = nk.generators.ChungLuGenerator(degree_sequence)

# Generate graph and measure execution time
start = time.perf_counter()
G = generator.generate()
end = time.perf_counter()

# Results
print("Number of nodes:", G.numberOfNodes())
print("Number of edges:", G.numberOfEdges())
print("Generation time:", round(end - start, 3), "seconds")

# Theoretical expected number of edges
expected_edges = n * avg_degree / 2
print("Expected number of edges:", expected_edges)