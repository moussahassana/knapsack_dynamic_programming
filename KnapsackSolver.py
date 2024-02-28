import matplotlib.pyplot as plt
import numpy as np

class KnapsackSolver:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)
        self.dp = [[0] * (capacity + 1) for _ in range(self.n + 1)]
        
    def solve(self):
        for i in range(1, self.n + 1):
            for w in range(1, self.capacity + 1):
                if self.weights[i - 1] <= w:
                    self.dp[i][w] = max(self.values[i - 1] + self.dp[i - 1][w - self.weights[i - 1]], self.dp[i - 1][w])
                else:
                    self.dp[i][w] = self.dp[i - 1][w]
        return self.dp[self.n][self.capacity]

class KnapsackTester:
    def __init__(self, num_instances, num_items):
        self.num_instances = num_instances
        self.num_items = num_items

    def test(self):
        capacities = np.random.randint(50, 100, size=self.num_instances)
        weights = [np.random.randint(1, 20, size=self.num_items) for _ in range(self.num_instances)]
        values = [np.random.randint(1, 50, size=self.num_items) for _ in range(self.num_instances)]
        results = []

        for i in range(self.num_instances):
            solver = KnapsackSolver(weights[i], values[i], capacities[i])
            result = solver.solve()
            results.append(result)

        return results

np.random.seed(42)

num_instances = 10
num_items = 10
tester = KnapsackTester(num_instances, num_items)
results = tester.test()
instances = [i+1 for i in range(num_instances)]

plt.plot(instances, results, marker='o', label=f'{num_items} items')

plt.title('Résultats du Problème du Sac à Dos')
plt.xlabel('Instance')
plt.ylabel('Valeur Optimale')
plt.xticks(instances)
plt.grid(True)
plt.legend()
plt.show()
