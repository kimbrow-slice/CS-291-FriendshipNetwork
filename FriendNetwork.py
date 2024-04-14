import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sys


# Create our structure for the names we will utilize
names = ["Jeff", "Zach", "Molly", "Michelle", "Michael", "Artie", "Ryan"]

# Matrix with friendship weights
matrix = np.array([
    [0, 9, 0, 0, 4, 0, 0],  # Jeff is friends with Zach with strength 9 and Michael with strength 4
    [9, 0, 5, 0, 6, 4, 0],  # Zach is friends with Jeff with strength 9, Molly with strength 5, Michael with strength 6, and Artie with strength 4
    [0, 5, 0, 7, 0, 0, 0],  # Molly is friends with Zach with strength 5 and Michelle with strength 7
    [0, 0, 7, 0, 0, 0, 0],  # Michelle is friends with Molly with strength 7
    [4, 6, 0, 0, 0, 8, 0],  # Michael is friends with Jeff with strength 4 and Zach with strength 6
    [0, 4, 0, 0, 8, 0, 0],  # Artie is friends with Zach with strength 4
    [0, 0, 0, 0, 0, 0, 0],  # Ryan is isolated
])

# Create the graph
G = nx.Graph()
for idx, name in enumerate(names):
    G.add_node(name)  # Adding nodes with labels

# Adding edges based on non-zero entries in the matrix
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        if matrix[i][j] != 0:
            G.add_edge(names[i], names[j], weight=matrix[i][j])

# Visualization of the graph
pos = nx.spring_layout(G)  # Node position layout for the graph
edges = G.edges(data=True)
weights = [ed[2]['weight'] for ed in edges]

# Drawing nodes, edges and labels
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, 
        edge_color=weights, width=6.0, edge_cmap=plt.cm.Blues)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in edges})
plt.title('Visual Representation of Friendship Network')
plt.show()

# Analysis of the graph
total_friendships = nx.number_of_edges(G)
degrees = G.degree()
most_popular_person = max(degrees, key=lambda x: x[1])[0]
isolated_individuals = list(nx.isolates(G))
average_strength = sum(weights) / total_friendships if total_friendships > 0 else 0

# List of friendship pairs with their respective strengths
friendship_pairs = [(names[i], names[j], matrix[i][j]) for i in range(len(matrix)) for j in range(i+1, len(matrix)) if matrix[i][j] != 0]

# Output results
print("Total Friendships:", total_friendships)
print("Friendship Pairs (and strengths):", friendship_pairs)
print("Most Popular Person:", most_popular_person)
print("Isolated Individuals:", isolated_individuals)
print("Average Strength of Friendships:", average_strength)
sys.stdout.flush()  # Flush the output buffer
