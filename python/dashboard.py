import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Datos", layout="wide")
st.title("Dashboard de Datos desde Excel")

uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx", "xls", "csv"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.subheader("Vista previa de los datos")
    st.dataframe(df)

    # Estadísticas básicas
    st.subheader("Estadísticas básicas")
    st.write(df.describe(include='all'))

    # Gráfico de barras para columnas numéricas
    num_cols = df.select_dtypes(include='number').columns.tolist()
    if num_cols:
        col = st.selectbox("Selecciona columna numérica para gráfico de barras", num_cols)
        fig = px.bar(df, x=df.columns[0], y=col, title=f"Gráfico de barras de {col}")
        st.plotly_chart(fig, use_container_width=True)

    # Gráfico de pastel para columna categórica
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    if cat_cols:
        col_cat = st.selectbox("Selecciona columna categórica para gráfico de pastel", cat_cols)
        fig2 = px.pie(df, names=col_cat, title=f"Distribución de {col_cat}")
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("Sube un archivo para ver el dashboard.")
