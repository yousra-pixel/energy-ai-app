import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("AI Energy Advisor")

st.write("Analyse et prédiction de la consommation énergétique industrielle")

st.header("Entrer les données de consommation")

data = pd.DataFrame({
    "Heure":[8,10,12,14,16,18,20,22],
    "Consommation_kWh":[120,140,170,174,190,160,130,110]
})

# tableau modifiable
edited_data = st.data_editor(data, num_rows="dynamic")

st.header("Tableau de données modifié")
st.dataframe(edited_data)

# graphique
st.header("Graphique de consommation")

fig, ax = plt.subplots()

ax.plot(
    edited_data["Heure"],
    edited_data["Consommation_kWh"],
    marker="o"
)

ax.set_xlabel("Heure")
ax.set_ylabel("Consommation (kWh)")
ax.set_title("Consommation énergétique de l'usine")

st.pyplot(fig)

# prédiction simple
st.header("Prédiction de consommation")

x = np.array(edited_data["Heure"])
y = np.array(edited_data["Consommation_kWh"])

coef = np.polyfit(x, y, 1)
model = np.poly1d(coef)

future_hour = st.slider("Choisir une heure future", 23, 30, 24)

prediction = model(future_hour)

st.write(f"Consommation prédite à {future_hour}h : **{prediction:.2f} kWh**")

# graphique prédiction
fig2, ax2 = plt.subplots()

ax2.plot(x, y, marker="o", label="Données réelles")

ax2.scatter(future_hour, prediction, color="red", label="Prédiction")

ax2.set_xlabel("Heure")
ax2.set_ylabel("Consommation (kWh)")
ax2.set_title("Prédiction de la consommation")

ax2.legend()

st.pyplot(fig2)
