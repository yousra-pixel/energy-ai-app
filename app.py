import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="AI Energy Advisor", layout="centered")

st.title("AI Energy Advisor")
st.write("Assistant intelligent pour l'optimisation énergétique dans l'industrie")

st.header("Paramètres industriels")

consommation = st.slider("Consommation énergétique actuelle (kWh)", 50, 300, 150)
temperature = st.slider("Température industrielle (°C)", 10, 40, 25)
production = st.slider("Production (%)", 0, 100, 70)

st.header("Analyse intelligente")

if consommation > 220:
    st.error("Consommation très élevée. Recommandation : réduire certaines machines non essentielles.")
elif consommation > 180:
    st.warning("Consommation élevée. Suggestion : optimiser les horaires de production.")
elif temperature > 30:
    st.warning("Température élevée. Recommandation : améliorer la ventilation industrielle.")
elif production < 40:
    st.warning("Production faible avec forte consommation. Vérifier l'efficacité énergétique.")
else:
    st.success("Consommation énergétique optimale.")

st.header("Simulation des données énergétiques")

data = {
    "Heure": [8, 10, 12, 14, 16, 18, 20, 22],
    "Consommation_kWh": [120, 140, 170, consommation, 190, 160, 130, 110]
}

df = pd.DataFrame(data)

st.subheader("Tableau de données")
st.dataframe(df)

st.subheader("Graphique de consommation énergétique")
fig, ax = plt.subplots()
ax.plot(df["Heure"], df["Consommation_kWh"], marker="o")
ax.set_title("Consommation énergétique de l'usine")
ax.set_xlabel("Heure")
ax.set_ylabel("Consommation (kWh)")
ax.grid(True)
st.pyplot(fig)

st.header("Prédiction simple de consommation")

x = np.array(df["Heure"])
y = np.array(df["Consommation_kWh"])

coef = np.polyfit(x, y, 1)
model = np.poly1d(coef)

heure_future = st.slider("Choisir une heure future pour la prédiction", 23, 30, 24)
prediction = model(heure_future)

st.write(f"Prédiction de consommation à {heure_future}h : **{prediction:.2f} kWh**")

fig2, ax2 = plt.subplots()
ax2.plot(df["Heure"], df["Consommation_kWh"], marker="o", label="Données réelles")
ax2.plot(heure_future, prediction, marker="s", markersize=8, label="Prédiction")
ax2.set_title("Prédiction de la consommation énergétique")
ax2.set_xlabel("Heure")
ax2.set_ylabel("Consommation (kWh)")
ax2.grid(True)
ax2.legend()
st.pyplot(fig2)

st.header("Conclusion")
st.write(
    "Ce prototype montre comment l'intelligence artificielle peut aider l'industrie à analyser, "
    "visualiser et anticiper la consommation énergétique afin d'améliorer l'efficacité énergétique."
)
