import math
import numpy as np
import matplotlib.pyplot as plt


# 1) Modelo Exponencial
def crecimiento_exponencial(N0, k, t):
    """
    N(t) = N0 * e^(k * t)
    """
    return N0 * np.exp(k * t)


# 2) Modelo Logistico
def crecimiento_logistico(N0, K, r, t):
    """
    N(t) = K / (1 + ((K - N0) / N0) * e^(-r * t))
    """
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))


# 3) Función logaritmica inversa (TIEMPO PARA LLEGAR A UN N)
def tiempo_para_poblacion(N, N0, k):
    """
    t = (1/k) * ln(N / N0)
    """
    if N <= N0:
        raise ValueError("La población objetivo debe ser mayor a la inicial.")
    return (1 / k) * math.log(N / N0)


# 4) Ejemplo de Simulación
if __name__ == "__main__":
    # Parámetros
    N0 = 100        # población inicial
    k = 0.3         # tasa exponencial
    r = 0.2         # tasa logística
    K = 5000        # capacidad máxima ecológica
    tiempo = np.linspace(0, 30, 300)

    # Simulaciones
    exp_data = crecimiento_exponencial(N0, k, tiempo)
    log_data = crecimiento_logistico(N0, K, r, tiempo)

    # Tiempo para alcanzar cierta población
    N_objetivo = 2000
    t_obj = tiempo_para_poblacion(N_objetivo, N0, k)
    print(f"Tiempo estimado para alcanzar {N_objetivo} bacterias (modelo exponencial): {t_obj:.2f} horas")


    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, exp_data, label="Crecimiento Exponencial")
    plt.plot(tiempo, log_data, label="Crecimiento Logístico")
    plt.axhline(N_objetivo, color="gray", linestyle="--", label=f"Población objetivo = {N_objetivo}")
    plt.title("Modelos de Crecimiento Bacteriano")
    plt.xlabel("Tiempo (horas)")
    plt.ylabel("Número de bacterias")
    plt.legend()
    plt.grid()
    plt.show()
