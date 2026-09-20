# Day 9 - Prefix Sum Optimization

numbers = [10, 20, 15, 30, 25, 40, 35, 50]

# -------------------------
# Brute Force
# -------------------------

def brute_force_sum(numbers, left, right):
    total = 0

    for i in range(left, right + 1):
        total += numbers[i]

    return total


# -------------------------
# Prefix Sum
# -------------------------

def build_prefix_sum(numbers):
    prefix = [0]

    for number in numbers:
        prefix.append(prefix[-1] + number)

    return prefix


def prefix_sum_query(prefix, left, right):
    return prefix[right + 1] - prefix[left]


# Build Prefix Sum Array
prefix = build_prefix_sum(numbers)

print("Original Array:")
print(numbers)

print("\nPrefix Sum Array:")
print(prefix)


# Multiple Queries
queries = [
    (0, 3),
    (2, 5),
    (1, 6),
    (4, 7)
]

print("\nQuery Results:")

for left, right in queries:

    brute_result = brute_force_sum(numbers, left, right)
    optimized_result = prefix_sum_query(prefix, left, right)

    print(f"\nRange {left} to {right}")
    print("Brute Force :", brute_result)
    print("Prefix Sum  :", optimized_result)