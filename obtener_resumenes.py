import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.rcParams["figure.figsize"] = (12, 6)

METRICAS_RELEVANTES = ["weight", "fatRate", "muscleRate"]
COLORES = ["#30343F", "#89023E", "#EA638C"]


def leer_y_formatear_pesos_amaz_fit():
    df = pd.read_csv("input/BODY.csv")

    df["time"] = df["time"].str.replace("+0000", "")
    df["time"] = pd.to_datetime(df["time"])
    df["week"] = df["time"].dt.isocalendar().week
    df["nombre_dia"] = df["time"].dt.day_name("es_MX")
    
    return df
