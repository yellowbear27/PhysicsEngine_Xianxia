"""Golden Core (金丹期) – Fourier theory.
1D and 2D FFT, power spectral density, convolution, correlation.
"""

import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2, fftfreq
from scipy.signal import convolve, correlate

def fourier_transform_1d(signal, dt=1.0):
    """Return frequencies and complex spectrum."""
    n = len(signal)
    freq = fftfreq(n, dt)
    spectrum = fft(signal)
    return freq, spectrum

def inverse_fourier_transform_1d(spectrum, dt=1.0):
    """Inverse 1D FFT (time‑domain signal)."""
    return ifft(spectrum)

def fourier_transform_2d(signal, dx=1.0, dy=1.0):
    """2D FFT."""
    return fft2(signal)

def inverse_fourier_transform_2d(spectrum):
    return ifft2(spectrum)

def convolution_1d(a, b, mode='full'):
    return convolve(a, b, mode=mode)

def correlation_1d(a, b, mode='full'):
    return correlate(a, b, mode=mode)

def power_spectral_density(signal, dt=1.0):
    freq, spectrum = fourier_transform_1d(signal, dt)
    psd = np.abs(spectrum)**2
    return freq, psd
