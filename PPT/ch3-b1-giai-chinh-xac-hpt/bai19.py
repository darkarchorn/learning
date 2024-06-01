import numpy as np

# Given matrices and vectors
A = np.array([
    [1, 2, 0, 3],
    [1, 0, 2, 2],
    [0, 0, 1, 1]
])

x = np.array([1000, 500, 350, 400])
b = np.array([3500, 2700, 900])

# Part a: Check if current food supply meets the average daily consumption
consumed_resources = np.dot(A, x)
sufficient_food = np.all(consumed_resources <= b)
print(f"Is there sufficient food? {sufficient_food}")

# Part b: Maximum number of animals that can be added
slack = b - consumed_resources
# Calculate the number of additional animals that can be added for each species
max_additional_animals = np.floor(slack / np.dot(A, np.ones(x.shape)))
print(f"Maximum additional animals for each species: {max_additional_animals}")

# Part c: If species 1 became extinct, find the increase for remaining species
x_extinct = x.copy()
x_extinct[0] = 0
remaining_food = b - np.dot(A, x_extinct)

# Ignore the column corresponding to the extinct species in A
A_remaining = A[:, 1:]

# Initialize an array to store the increase in remaining species
remaining_x_increase = np.zeros(A_remaining.shape[1])

# Calculate the possible increase for each remaining species
for i in range(A_remaining.shape[1]):
    if np.all(A_remaining[:, i] == 0):
        remaining_x_increase[i] = np.inf  # Infinite increase possible if no food required
    else:
        possible_increase = remaining_food / A_remaining[:, i]
        possible_increase[~np.isfinite(possible_increase)] = np.inf  # Handle division by zero
        remaining_x_increase[i] = np.min(possible_increase)

print(f"Increase in each of the remaining species: {remaining_x_increase}")
