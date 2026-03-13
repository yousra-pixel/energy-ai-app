import streamlit as st

st.title("AI Energy Advisor")

st.write("Assistant intelligent pour l'optimisation énergétique dans l'industrie")

consommation = st.slider("Consommation énergétique (kWh)", 50, 300, 150)
temperature = st.slider("Température industrielle (°C)", 10, 40, 25)
production = st.slider("Production (%)", 0, 100, 70)

st.subheader("Analyse intelligente")

if consommation > 220:
    st.error("Consommation très élevée. Réduire certaines machines.")
elif consommation > 180:
    st.warning("Consommation élevée. Optimiser les horaires de production.")
elif temperature > 30:
    st.warning("Température élevée. Améliorer la ventilation industrielle.")
elif production < 40:
    st.warning("Production faible avec forte consommation.")
else:
    st.success("Consommation énergétique optimale.")
