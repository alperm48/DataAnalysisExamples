import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt

# Parametreler
num_points = 1000
x = np.linspace(0, 10, num_points)
signal = np.sin(x)
noise = np.random.normal(0, 0.5, num_points)
noisy_signal = signal + noise

# Medyan filtresi uygulama
filtered_signal = medfilt(noisy_signal, kernel_size=11)  # Çekirdek boyutunu değiştirerek sonucu etkileyebilirsiniz

# Grafik çizimi
plt.figure(figsize=(10, 6))
plt.plot(x, signal, label="Orijinal Sinyal")
plt.plot(x, noisy_signal, label="Gürültülü Sinyal", color='orange', alpha=0.6)
plt.plot(x, filtered_signal, label="Filtrelenmiş Sinyal", color='green', linewidth=1.5)
plt.legend()
plt.xlabel("Zaman")
plt.ylabel("Genlik")
plt.title("Orijinal, Gürültülü ve Filtrelenmiş Sinyal")
plt.show()
