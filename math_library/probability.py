"""Soul Formation (化神期) – Probability and statistics.
Distributions (normal, uniform, exponential), sampling, moments, Bayesian update.
"""

import numpy as np
from scipy import stats

def normal_pdf(x, mu=0, sigma=1):
    return stats.norm.pdf(x, mu, sigma)

def normal_cdf(x, mu=0, sigma=1):
    return stats.norm.cdf(x, mu, sigma)

def uniform_pdf(x, low=0, high=1):
    return stats.uniform.pdf(x, low, high-low)

def exponential_pdf(x, scale=1):
    return stats.expon.pdf(x, scale=scale)

def sample_normal(n, mu=0, sigma=1):
    return np.random.normal(mu, sigma, n)

def sample_uniform(n, low=0, high=1):
    return np.random.uniform(low, high, n)

def mean(data):
    return np.mean(data)

def variance(data, ddof=0):
    return np.var(data, ddof=ddof)

def covariance(x, y):
    return np.cov(x, y)[0,1]

def correlation(x, y):
    return np.corrcoef(x, y)[0,1]

def confidence_interval_normal(data, confidence=0.95):
    n = len(data)
    mean_val = np.mean(data)
    sem = stats.sem(data)
    margin = sem * stats.t.ppf((1+confidence)/2, n-1)
    return mean_val - margin, mean_val + margin

def bayes_update(prior, likelihood, evidence):
    """P(A|B) = P(B|A) * P(A) / P(B)."""
    return (likelihood * prior) / evidence
