import streamlit as st 
import pandas as pd
from sklearn .linear_model import LinearRegression

df = pd.read_csv("investimento.csv")

modelo = LinearRegression()
x = df[["tempo"]]
y = df[["renda"]]

modelo.fit(x, y)

st.title("Prevendo a renda de investimentos")
st.divider()

tempo = st.number_input("Digite o tempo de investimento a ser previsto: ")

if tempo:
    renda_prevista = modelo.predict([[tempo]])[0][0]
    st.write(f"O valor final da aplicação em {tempo} meses é de {renda_prevista:.2f} R$.")