import pandas as pd

import matplotlib.pyplot as plt


def obtener_resumen_mes_por_semana(promedios_por_semana):
    primera_semana_mes = promedios_por_semana.iloc[0]
    ultima_semana_mes = promedios_por_semana.iloc[-1]

    diferencia = ultima_semana_mes - primera_semana_mes
    diferencia.name = "Diferencia"

    resumen = pd.concat([primera_semana_mes, ultima_semana_mes, diferencia], axis=1)

    return resumen


def crear_graficos_pesos(pesos_con_promedios, metricas_a_graficar, colores_metricas):
    fig, axis = plt.subplots(1, 3, figsize=(20, 6))
    for i, metrica in enumerate(metricas_a_graficar):
        # Plot the first and last points
        first_point = pesos_con_promedios[metrica].iloc[0]
        last_point = pesos_con_promedios[metrica].iloc[-1]
        axis[i].scatter(pesos_con_promedios.index[0], first_point, color="blue", marker="o")
        axis[i].scatter(pesos_con_promedios.index[-1], last_point, color="blue", marker="o")

        # Annotate the first and last points with their values
        axis[i].annotate(
            f"{first_point:.2f}",
            (pesos_con_promedios.index[0], first_point),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )
        axis[i].annotate(
            f"{last_point:.2f}",
            (pesos_con_promedios.index[-1], last_point),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

        diferencia = last_point - first_point

        pesos_con_promedios.plot(
            y=metrica,
            ax=axis[i],
            title=f"{metrica} - Dif: {diferencia:.2f}",
            color=colores_metricas[i],
        )

        pesos_con_promedios.plot(y=f"{metrica}_promedios", style="--", ax=axis[i])

    plt.show()
    plt.tight_layout()

    return fig
