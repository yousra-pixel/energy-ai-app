import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Energy Advisor", layout="centered")

st.title("AI Energy Advisor")
st.write("Assistant intelligent pour l'optimisation énergétique dans l'industrie")

# ----------------------------
# Partie 1 : paramètres rapides
# ----------------------------
st.header("Paramètres industriels")

consommation = st.slider("Consommation énergétique de référence (kWh)", 50, 500, 150)
temperature = st.slider("Température industrielle (°C)", 10, 40, 25)
production = st.slider("Production (%)", 0, 100, 70)

st.header("Analyse intelligente")

if consommation > 350:
    st.error("Consommation très élevée. Recommandation : réduire certaines machines non essentielles.")
elif consommation > 250:
    st.warning("Consommation élevée. Suggestion : optimiser les horaires de production.")
elif temperature > 30:
    st.warning("Température élevée. Recommandation : améliorer la ventilation industrielle.")
elif production < 40:
    st.warning("Production faible avec forte consommation. Vérifier l'efficacité énergétique.")
else:
    st.success("Consommation énergétique acceptable.")

# ----------------------------
# Partie 2 : données annuelles
# ----------------------------
st.header("Données mensuelles de l'usine")

default_data = pd.DataFrame({
    "Mois": [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ],
    "Consommation_kWh": [
        consommation, 140, 170, 160, 180, 200,
        220, 210, 190, 175, 160, 150
    ]
})

default_data.index = range(1, len(default_data) + 1)

edited_data = st.data_editor(
    default_data,
    num_rows="fixed",
    use_container_width=True
)

# ----------------------------
# Partie 3 : énergie annuelle totale
# ----------------------------
total_annuel = edited_data["Consommation_kWh"].sum()

st.subheader("Énergie totale annuelle")
st.metric(label="Consommation totale annuelle", value=f"{total_annuel:.2f} kWh")

# ----------------------------
# Partie 4 : graphique mensuel
# ----------------------------
st.subheader("Consommation énergétique annuelle de l'usine")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(edited_data["Mois"], edited_data["Consommation_kWh"], marker="o")
ax.set_title("Consommation énergétique mensuelle")
ax.set_xlabel("Mois")
ax.set_ylabel("Consommation (kWh)")
ax.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig)

# ----------------------------
# Conclusion
# ----------------------------
st.header("Conclusion")
st.write(
    "Ce prototype permet d'analyser les paramètres énergétiques d'une usine, "
    "de modifier les consommations mensuelles de janvier à décembre, "
    "et de calculer la consommation énergétique totale annuelle."
)
