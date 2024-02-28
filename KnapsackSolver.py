import matplotlib.pyplot as plt
import numpy as np

class KnapsackSolver:
    def __init__(self, weights, values, capacity):
        """
        Initialise une instance du problème du sac à dos.
        
        Args:
            weights (list): Liste des poids des objets.
            values (list): Liste des valeurs des objets.
            capacity (int): Capacité maximale du sac à dos.
        """
        self.weights = weights  # Poids des objets
        self.values = values  # Valeurs des objets
        self.capacity = capacity  # Capacité du sac à dos
        self.initial_capacity = capacity  # Capacité de départ du sac à dos
        self.n = len(weights)  # Nombre d'objets
        self.dp = [[0] * (capacity + 1) for _ in range(self.n + 1)]  # Tableau pour la programmation dynamique
        self.selected_items = []  # Liste pour stocker les objets sélectionnés
        
    def solve(self):
        """
        Résout le problème du sac à dos et renvoie la valeur totale des objets, les objets sélectionnés avec leur valeur
        et leur poids respectif, ainsi que la capacité restante du sac à dos.
        
        Returns:
            tuple: Un tuple contenant la valeur totale du sac à dos, la liste des objets sélectionnés avec leur valeur
            et leur poids respectif, ainsi que la capacité restante du sac à dos.
        """
        # Résolution du problème du sac à dos avec la programmation dynamique
        for i in range(1, self.n + 1):
            for w in range(1, self.capacity + 1):
                if self.weights[i - 1] <= w:
                    # Si le poids de l'objet est inférieur ou égal à la capacité restante, on peut le prendre
                    self.dp[i][w] = max(self.values[i - 1] + self.dp[i - 1][w - self.weights[i - 1]], self.dp[i - 1][w])
                else:
                    # Sinon, on ne peut pas prendre l'objet
                    self.dp[i][w] = self.dp[i - 1][w]
        
        # Retourne la valeur optimale du sac à dos et les objets sélectionnés avec leur valeur et leur poids
        total_value = self.dp[self.n][self.initial_capacity]
        total_weight = 0
        for i in range(self.n, 0, -1):
            if self.dp[i][self.initial_capacity] != self.dp[i - 1][self.initial_capacity] and self.initial_capacity >= self.weights[i - 1]:
                # Vérifie si l'objet a été sélectionné et si la capacité est suffisante pour l'ajouter
                self.selected_items.append((self.values[i - 1], self.weights[i - 1]))
                total_weight += self.weights[i - 1]
                self.initial_capacity -= self.weights[i - 1]
        
        remaining_capacity = self.capacity - total_weight  # Calcul de la capacité restante du sac à dos
        return total_value, self.selected_items, total_weight, remaining_capacity

class KnapsackTester:
    def __init__(self, num_instances, num_items):
        """
        Initialise un testeur pour résoudre plusieurs instances du problème du sac à dos.
        
        Args:
            num_instances (int): Nombre d'instances à tester.
            num_items (int): Nombre d'objets dans chaque instance.
        """
        self.num_instances = num_instances  # Nombre d'instances à tester
        self.num_items = num_items  # Nombre d'objets dans chaque instance

    def test(self):
        """
        Teste plusieurs instances du problème du sac à dos et renvoie les résultats.
        
        Returns:
            list: Liste des résultats pour toutes les instances testées.
        """
        capacities = np.random.randint(50, 100, size=self.num_instances)  # Capacités aléatoires pour chaque instance
        weights = [np.random.randint(1, 20, size=self.num_items) for _ in range(self.num_instances)]  # Poids aléatoires pour chaque instance
        values = [np.random.randint(1, 50, size=self.num_items) for _ in range(self.num_instances)]  # Valeurs aléatoires pour chaque instance
        results = []

        for i in range(self.num_instances):
            # Pour chaque instance, résoudre le problème du sac à dos et enregistrer le résultat
            solver = KnapsackSolver(weights[i], values[i], capacities[i])
            result = solver.solve()
            results.append(result)

        return results  # Retourne les résultats pour toutes les instances testées

# Génération de la même séquence de nombres aléatoires à chaque exécution pour une reproductibilité
np.random.seed(10)

num_instances = 10  # Nombre d'instances à tester
num_items = 10  # Nombre d'objets dans chaque instance
tester = KnapsackTester(num_instances, num_items)  # Création d'une instance du testeur
results = tester.test()  # Exécution du test
instances = [i+1 for i in range(num_instances)]  # Liste des instances pour l'axe x du graphique

# Affichage des résultats
for i, result in enumerate(results):
    total_value, selected_items, total_weight, remaining_capacity = result
    print(f"Instance {i+1}:")
    print(f"  Capacité de départ du sac à dos: {result[3] + result[2]}")  # Affichage de la capacité de départ
    print(f"  Capacité restante du sac à dos: {remaining_capacity}")  # Affichage de la capacité restante
    print(f"  Valeur totale du sac à dos: {total_value}")
    print("  Objets sélectionnés:")
    for item in selected_items:
        value, weight = item
        print(f"    - Valeur: {value}, Poids: {weight}")
    print(f"  Somme des poids des objets sélectionnés: {total_weight}")
    print()

# Tracé du graphique des résultats
plt.plot(instances, [result[0] for result in results], marker='o', label=f'{num_items} items')

plt.title('Résultats du Problème du Sac à Dos')
plt.xlabel('Instance')
plt.ylabel('Valeur Optimale')
plt.xticks(instances)
plt.grid(True)
plt.legend()
plt.show()

