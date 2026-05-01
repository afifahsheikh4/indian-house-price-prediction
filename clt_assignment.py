"""
CEP Assignment: Central Limit Theorem - Indian House Prices
Course: ES111 Software Tool
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
import math

# ============================================
# MANUAL STATISTICS FUNCTIONS
# ============================================

def manual_sum(data):
    total = 0
    for value in data:
        total += value
    return total

def manual_mean(data):
    if len(data) == 0:
        return 0
    return manual_sum(data) / len(data)

def manual_variance(data):
    if len(data) < 2:
        return 0
    mean = manual_mean(data)
    squared_diff_sum = 0
    for value in data:
        squared_diff_sum += (value - mean) ** 2
    return squared_diff_sum / (len(data) - 1)

def manual_std(data):
    return math.sqrt(manual_variance(data))

# ============================================
# PART A: LOAD DATA
# ============================================

print("="*60)
print("CENTRAL LIMIT THEOREM DEMONSTRATION")
print("Indian House Price Analysis")
print("="*60)

# Load the CSV file
df = pd.read_csv('IndianHousePrices.csv')
prices = df['Price'].dropna().tolist()
prices = [p for p in prices if p > 0]

print(f"\n✅ Loaded {len(prices)} valid house prices")
print(f"   Minimum price: ₹{min(prices):.2f}")
print(f"   Maximum price: ₹{max(prices):.2f}")

# Calculate statistics MANUALLY
population_mean = manual_mean(prices)
population_variance = manual_variance(prices)
population_std = manual_std(prices)

print(f"\n📊 Population Statistics (Manual Calculations):")
print(f"   Number of houses: {len(prices)}")
print(f"   Mean price (μ): ₹{population_mean:.2f}")
print(f"   Variance (σ²): {population_variance:.2f}")
print(f"   Standard Deviation (σ): ₹{population_std:.2f}")

# Plot original data histogram
plt.figure(figsize=(12, 6))
plt.hist(prices, bins=50, edgecolor='black', alpha=0.7, color='skyblue')
plt.axvline(population_mean, color='red', linestyle='--', linewidth=2, 
            label=f'Mean: ₹{population_mean:.2f}')
plt.title('Original Indian House Price Distribution', fontsize=14)
plt.xlabel('House Price (₹)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('1_original_distribution.png', dpi=150)
plt.close()
print("\n✅ Saved: 1_original_distribution.png")

# ============================================
# PART C: SAMPLING DISTRIBUTIONS
# ============================================

print("\n" + "="*60)
print("PART C: Sampling Distributions")
print("="*60)

sample_sizes = [5, 10, 30, 100]
num_samples = 1000

for N in sample_sizes:
    print(f"\n📊 Processing N = {N}...")
    sample_means = []
    
    for _ in range(num_samples):
        sample = [random.choice(prices) for _ in range(N)]
        sample_mean = manual_mean(sample)
        sample_means.append(sample_mean)
    
    mean_of_means = manual_mean(sample_means)
    std_of_means = manual_std(sample_means)
    theoretical_std = population_std / math.sqrt(N)
    
    print(f"   Mean of sample means: {mean_of_means:.2f}")
    print(f"   Std of means: {std_of_means:.2f}")
    print(f"   Theoretical SE (σ/√n): {theoretical_std:.2f}")
    
    plt.figure(figsize=(12, 6))
    plt.hist(sample_means, bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
    plt.axvline(mean_of_means, color='red', linestyle='--', linewidth=2,
                label=f'Mean of Means: {mean_of_means:.2f}')
    plt.axvline(population_mean, color='blue', linestyle='-', linewidth=2,
                label=f'Population Mean: {population_mean:.2f}')
    plt.title(f'Sampling Distribution (N={N}, 1000 samples)', fontsize=14)
    plt.xlabel('Sample Mean (₹)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'2_sampling_dist_N{N}.png', dpi=150)
    plt.close()
    print(f"   ✅ Saved: 2_sampling_dist_N{N}.png")

print("\n✅ Part C Complete!")

# ============================================
# PART D: Z-VALUE DISTRIBUTIONS
# ============================================

print("\n" + "="*60)
print("PART D: Z-value Distributions")
print("="*60)

z_sample_sizes = [10, 30, 100]

for N in z_sample_sizes:
    print(f"\n📊 Processing Z-values for N = {N}...")
    z_values = []
    
    for _ in range(num_samples):
        sample = [random.choice(prices) for _ in range(N)]
        sample_mean = manual_mean(sample)
        z = (sample_mean - population_mean) / (population_std / math.sqrt(N))
        z_values.append(z)
    
    z_mean = manual_mean(z_values)
    z_std = manual_std(z_values)
    
    print(f"   Mean of z-values: {z_mean:.3f}")
    print(f"   Std of z-values: {z_std:.3f}")
    
    plt.figure(figsize=(12, 6))
    plt.hist(z_values, bins=30, edgecolor='black', alpha=0.7, density=True, color='lightcoral')
    plt.title(f'Z-value Distribution (N={N})', fontsize=14)
    plt.xlabel('Z-value', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    
    # Standard normal curve
    x = [i/10 for i in range(-40, 41)]
    normal_y = [1/math.sqrt(2*math.pi) * math.exp(-xi**2/2) for xi in x]
    plt.plot(x, normal_y, 'b-', linewidth=2, label='Standard Normal')
    plt.axvline(0, color='red', linestyle='--', linewidth=1, alpha=0.5)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'3_z_distribution_N{N}.png', dpi=150)
    plt.close()
    print(f"   ✅ Saved: 3_z_distribution_N{N}.png")

print("\n✅ Part D Complete!")

# ============================================
# FINAL SUMMARY
# ============================================

print("\n" + "="*60)
print("✅ ASSIGNMENT COMPLETE!")
print("="*60)

print("\n📁 8 PNG files saved:")
print("   1_original_distribution.png")
print("   2_sampling_dist_N5.png")
print("   2_sampling_dist_N10.png")
print("   2_sampling_dist_N30.png")
print("   2_sampling_dist_N100.png")
print("   3_z_distribution_N10.png")
print("   3_z_distribution_N30.png")
print("   3_z_distribution_N100.png")

print(f"\n📊 Population Statistics:")
print(f"   Mean (μ): ₹{population_mean:.2f}")
print(f"   Std Dev (σ): ₹{population_std:.2f}")
print(f"   Variance (σ²): {population_variance:.2f}")