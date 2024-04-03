import numpy as np
import random
import matplotlib.pyplot as plt



# Define a road network as a graph
class RoadNetwork():
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.pheromone_matrix = np.ones((num_nodes, num_nodes))  # Pheromone matrix between nodes
        self.distance_matrix = np.random.rand(num_nodes, num_nodes)  # Distance matrix between nodes
        self.fuel_consumption_matrix = np.random.rand(num_nodes, num_nodes)  # Fuel consumption matrix between nodes
        self.time_matrix = np.random.rand(num_nodes, num_nodes)  # Time matrix between nodes

# Define parameters
num_ants = 10
num_iterations = 100
alpha = 1.0  # Weight for pheromone influence
beta = 2.0   # Weight for distance influence
gamma = 1.0  # Weight for fuel consumption
delta = 1.0  # Weight for time taken
evaporation_rate = 0.5
pheromone_const = 1.0

# Initialize road network
road_network = RoadNetwork(num_nodes=10)  # Adjust num_nodes as needed

# Define a function to calculate route cost considering fuel consumption and time
def route_cost(route, road_network):
    total_cost = 0
    total_fuel_consumption = 0
    total_time_taken = 0

    for i in range(len(route) - 1):
        node1 = route[i]
        node2 = route[i + 1]
        total_cost += (road_network.distance_matrix[node1][node2] +
                       road_network.fuel_consumption_matrix[node1][node2] +
                       road_network.time_matrix[node1][node2])
        total_fuel_consumption += road_network.fuel_consumption_matrix[node1][node2]
        total_time_taken += road_network.time_matrix[node1][node2]

    return total_cost, total_fuel_consumption, total_time_taken

# ACO algorithm for traffic flow optimization
def ant_colony_optimization(road_network, num_ants, num_iterations):
    best_route = None
    shortest_cost = float("inf")
    all_costs = []
    all_fuel_consumption = []
    all_time_taken = []

    for iteration in range(num_iterations):
        ant_routes = []
        for ant in range(num_ants):
            visited_nodes = set()
            current_node = random.randint(0, road_network.num_nodes - 1)
            route = [current_node]
            total_cost = 0
            total_fuel_consumption = 0
            total_time_taken = 0

            while len(visited_nodes) < road_network.num_nodes - 1:
                unvisited_nodes = set(range(road_network.num_nodes)) - visited_nodes
                probabilities = []

                for node in unvisited_nodes:
                    pheromone_level = road_network.pheromone_matrix[current_node][node]
                    dist = road_network.distance_matrix[current_node][node]
                    fuel_consumption = road_network.fuel_consumption_matrix[current_node][node]
                    time_taken = road_network.time_matrix[current_node][node]

                    prob = (pheromone_level * alpha) * ((1 / dist) * beta) * ((1 / fuel_consumption) * gamma) * ((1 / time_taken) * delta)
                    probabilities.append((node, prob))

                total_prob = sum(prob for _, prob in probabilities)
                probabilities = [(node, prob / total_prob) for node, prob in probabilities]

                next_node = random.choices(*zip(*probabilities))[0]
                visited_nodes.add(current_node)
                route.append(next_node)

                delta_cost, delta_fuel_consumption, delta_time_taken = route_cost([current_node, next_node], road_network)
                total_cost += delta_cost
                total_fuel_consumption += delta_fuel_consumption
                total_time_taken += delta_time_taken
                current_node = next_node

            ant_routes.append((route, total_cost))
            all_fuel_consumption.append(total_fuel_consumption)
            all_time_taken.append(total_time_taken)

        # Update pheromone levels
        for i in range(road_network.num_nodes):
            for j in range(road_network.num_nodes):
                if i != j:
                    road_network.pheromone_matrix[i][j] *= (1 - evaporation_rate)

        for route, cost in ant_routes:
            for i in range(len(route) - 1):
                road_network.pheromone_matrix[route[i]][route[i + 1]] += pheromone_const / cost

        # Find the best route in this iteration
        min_cost_route = min(ant_routes, key=lambda x: x[1])
        if min_cost_route[1] < shortest_cost:
            best_route = min_cost_route[0]
            shortest_cost = min_cost_route[1]

        all_costs.append(shortest_cost)

    return best_route, all_costs, all_fuel_consumption, all_time_taken


# ACO with RL algorithm
def aco_with_rl(road_network, num_ants, num_iterations):
    best_route = None
    shortest_cost = float("inf")
    all_costs = []

    for iteration in range(num_iterations):
        ant_routes = []
        for ant in range(num_ants):
            visited_nodes = set()
            current_node = random.randint(0, road_network.num_nodes - 1)
            route = [current_node]
            total_cost = 0

            while len(visited_nodes) < road_network.num_nodes - 1:
                unvisited_nodes = set(range(road_network.num_nodes)) - visited_nodes
                probabilities = []

                for node in unvisited_nodes:
                    # Placeholder for RL-based decision-making
                    RL_decision = random.uniform(0, 1)  # Replace with your RL function
                    pheromone_level = road_network.pheromone_matrix[current_node][node]
                    dist = road_network.distance_matrix[current_node][node]
                    fuel_consumption = road_network.fuel_consumption_matrix[current_node][node]
                    time_taken = road_network.time_matrix[current_node][node]

                    prob = (RL_decision * pheromone_level * alpha * (1 / dist) * beta * (1 / fuel_consumption) * gamma * (1 / time_taken) * delta)
                    probabilities.append((node, prob))

                total_prob = sum(prob for _, prob in probabilities)
                probabilities = [(node, prob / total_prob) for node, prob in probabilities]

                next_node = random.choices(*zip(*probabilities))[0]
                visited_nodes.add(current_node)
                route.append(next_node)

                delta_cost, _, _ = route_cost([current_node, next_node], road_network)
                total_cost += delta_cost
                current_node = next_node

            ant_routes.append((route, total_cost))

        # Update pheromone levels
        for i in range(road_network.num_nodes):
            for j in range(road_network.num_nodes):
                if i != j:
                    road_network.pheromone_matrix[i][j] *= (1 - evaporation_rate)

        for route, cost in ant_routes:
            for i in range(len(route) - 1):
                road_network.pheromone_matrix[route[i]][route[i + 1]] += pheromone_const / cost

        # Find the best route in this iteration
        min_cost_route = min(ant_routes, key=lambda x: x[1])
        if min_cost_route[1] < shortest_cost:
            best_route = min_cost_route[0]
            shortest_cost = min_cost_route[1]

        all_costs.append(shortest_cost)

    return best_route, shortest_cost, all_costs

# Comparison function for ACO and ACO-RL

aco_best_route, aco_all_costs, aco_all_fuel_consumption, aco_all_time_taken = ant_colony_optimization(road_network, num_ants, num_iterations)
aco_rl_best_route, aco_rl_shortest_cost, aco_rl_all_costs = aco_with_rl(road_network, num_ants, num_iterations)

# Plot comparison graphs for ACO vs. ACO-RL
plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.plot(range(len(aco_all_costs)), aco_all_costs, label="ACO")
plt.plot(range(len(aco_rl_all_costs)), aco_rl_all_costs, label="ACO-RL")
plt.title("Comparison of Shortest Cost")
plt.xlabel("Iteration")
plt.ylabel("Shortest Cost")
plt.legend()
plt.grid(True)

plt.subplot(232)
plt.plot(range(len(aco_all_fuel_consumption)), aco_all_fuel_consumption, label="ACO")
#plt.plot(range(len(aco_rl_all_fuel_consumption)), aco_rl_all_fuel_consumption, label="ACO-RL")
plt.title("Comparison of Fuel Consumption")
plt.xlabel("Iteration")
plt.ylabel("Total Fuel Consumption")
plt.legend()
plt.grid(True)

plt.subplot(233)
plt.plot(range(len(aco_all_time_taken)), aco_all_time_taken, label="ACO")
#plt.plot(range(len(aco_rl_all_time_taken)), aco_rl_all_time_taken, label="ACO-RL")
plt.title("Comparison of Time Taken")
plt.xlabel("Iteration")
plt.ylabel("Total Time Taken")
plt.legend()
plt.grid(True)

# Additional plots if needed

plt.tight_layout()
plt.show()

