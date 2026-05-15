import streamlit as st

from src.drug_api import consultar_medicamento


st.set_page_config(page_title="CheckorKaput", page_icon="💊")

st.title("CheckorKaput")
st.write("Aplicação para consulta informativa de medicamentos usando API pública.")

st.warning(
    "As informações exibidas são apenas informativas e não substituem "
    "orientação médica ou farmacêutica."
)

nome = st.text_input(
    "Digite o nome genérico do medicamento",
    placeholder="Exemplo: acetaminophen",
)

if st.button("Consultar medicamento"):
    if not nome.strip():
        st.error("Digite o nome de um medicamento.")
    else:
        try:
            resultado = consultar_medicamento(nome)

            if resultado is None:
                st.warning("Medicamento não encontrado na API.")
            else:
                st.subheader("Informações encontradas")
                st.write(f"**Nome genérico:** {resultado['nome_generico']}")
                st.write(f"**Nome comercial:** {resultado['nome_marca']}")
                st.write(f"**Fabricante:** {resultado['fabricante']}")
                st.write(f"**Tipo de produto:** {resultado['tipo_produto']}")
                st.write(f"**Aviso:** {resultado['aviso']}")

        except Exception:
            st.error("Erro ao consultar a API pública.")
