import requests
import streamlit as st
import json


cotacoes=requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes=cotacoes.json()

dolar=cotacoes['USDBRL']["bid"]
dolar_tempo=cotacoes['USDBRL']['create_date']


euro=cotacoes['EURBRL']["bid"]
euro_tempo=cotacoes['EURBRL']['create_date']

bitcoin=cotacoes['BTCBRL']["bid"]
bitcoin_tempo=cotacoes['BTCBRL']["create_date"]

st.sidebar.title('Menu')

op1=st.sidebar.selectbox("Selecione o que você deseja",("Consultar cotação","CEP"))

if op1=="Consultar cotação":

    op = st.selectbox("Moedas", ("Dólar","Euro","Bitcoin"))

    if op == "Dólar":
        st.write("O valor do Dolár está: {}".format(dolar))
        st.write("Atualizado em: {}".format(dolar_tempo))


    if op == "Euro":
        st.write("O valor do Euro está {}".format(euro))
        st.write("Atulizado em: {}".format(euro_tempo))

    if op == "Bitcoin":
        st.write("O valor do Bitcoin está {}".format(bitcoin))
        st.write("Atualizado em: {}".format(bitcoin_tempo))

if op1=="CEP":
    
    cep_input=st.text_input("Digite o CEP para consulta: ")
    cep=requests.get("https://cep.awesomeapi.com.br/json/{}".format(cep_input))
    cep=cep.json()
    #cep_rua=cep['adress']
    #cep_state=cep['state']
    #cep_district=cep['district']
    #cep_city=cep['city']

    if len(cep_input) != 8:
        st.write("Quantidade de digitos invalida")
    st.write("Rua:  Estado: {}".format(cep))

   