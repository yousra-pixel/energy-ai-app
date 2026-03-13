import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="AI Energy Advisor", layout="centered")

st.title("AI Energy Advisor")
st.write("Assistant intelligent pour l'optimisation énergétique dans l'industrie")

# ----------------------------
# Partie 1 : paramètres rapides
# ----------------------------
st.header("Paramètres industriels")

consommation = st.slider("Consommation énergétique (kWh)", 50, 300, 150)
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

# ----------------------------
# Partie 2 : tableau modifiable
# ----------------------------
st.header("Données de l'usine")

default_data = pd.DataFrame({
    "Heure": [8, 10, 12, 14, 16, 18, 20, 22],
    "Consommation_kWh": [120, 140, 170, consommation, 190, 160, 130, 110]
})

edited_data = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

st.subheader("Tableau de données")
st.dataframe(edited_data, use_container_width=True)

# ----------------------------
# Partie 3 : graphique
# ----------------------------
st.subheader("Graphique de consommation énergétique")

fig, ax = plt.subplots()
ax.plot(edited_data["Heure"], edited_data["Consommation_kWh"], marker="o")
ax.set_title("Consommation énergétique de l'usine")
ax.set_xlabel("Heure")
ax.set_ylabel("Consommation (kWh)")
ax.grid(True)
st.pyplot(fig)

# ----------------------------
# Partie 4 : prédiction simple
# ----------------------------
st.header("Prédiction simple de consommation")

if len(edited_data) >= 2:
    x = np.array(edited_data["Heure"], dtype=float)
    y = np.array(edited_data["Consommation_kWh"], dtype=float)

    coef = np.polyfit(x, y, 1)
    model = np.poly1d(coef)

    heure_future = st.slider("Choisir une heure future pour la prédiction", 23, 30, 24)
    prediction = model(heure_future)

    st.write(f"Prédiction de consommation à {heure_future}h : **{prediction:.2f} kWh**")

    fig2, ax2 = plt.subplots()
    ax2.plot(x, y, marker="o", label="Données réelles")
    ax2.scatter(heure_future, prediction, color="red", s=100, label="Prédiction")
    ax2.set_title("Prédiction de la consommation énergétique")
    ax2.set_xlabel("Heure")
    ax2.set_ylabel("Consommation (kWh)")
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)
else:
    st.info("Ajoutez au moins deux lignes dans le tableau pour afficher la prédiction.")

# ----------------------------
# Conclusion
# ----------------------------
st.header("Conclusion")
st.write(
    "Ce prototype permet d'analyser les paramètres énergétiques, de modifier les données "
    "pour n'importe quelle usine, de visualiser la consommation et d'estimer une consommation future."
)
