import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n_values = [1, 5, 20, 50, 80, 100]
trials = 100
lambda_val = 1

def sample_scaled_means(n, lambda_val=1, trials=100):
    # Sample n random numbers from Poisson(lambda) for 'trials' times
    samples = np.random.poisson(lambda_val, size=(trials, n))
    # Calculate scaled sample mean: (1/sqrt(n)) * sum(x_i)
    return samples.sum(axis=1) / np.sqrt(n)

fig, axes = plt.subplots(2, 3, figsize=(12, 10))
axes = axes.flatten()

for i, n in enumerate(n_values):
    scaled_means = sample_scaled_means(n, lambda_val, trials)
    
    # Theoretical mean and variance for Y_n = (1/sqrt(n)) * sum(X_i)
    # E[Y_n] = (1/sqrt(n)) * n * lambda = sqrt(n) * lambda
    # Var(Y_n) = (1/n) * n * lambda = lambda
    mu_theory = np.sqrt(n) * lambda_val
    sigma_theory = np.sqrt(lambda_val)
    
    # Plot histogram
    axes[i].hist(scaled_means, bins=50, density=True, alpha=0.6, color='black', label=f'Empirical (n={n})')
    
    # Plot Gaussian/Normal distribution with same mean and variance
    x = np.linspace(mu_theory - 4*sigma_theory, mu_theory + 4*sigma_theory, 200)
    axes[i].plot(x, norm.pdf(x, mu_theory, sigma_theory), 'r-', lw=2, label='Normal Distribution')
    
    axes[i].set_title(f'Distribution for $n={n}$')
    axes[i].set_xlabel('Scaled Sample Mean $\sqrt{n}\\bar{x}$')
    axes[i].set_ylabel('Probability Density')
    axes[i].legend()

plt.tight_layout()
plt.savefig('clt_poisson.png', dpi=300)

# Print mean and variance for the result
print(f"For n=100, Expected Mean: {np.sqrt(100)}, Actual Mean: {np.mean(sample_scaled_means(100))}")
print(f"For n=100, Expected Variance: {1.0}, Actual Variance: {np.var(sample_scaled_means(100))}")