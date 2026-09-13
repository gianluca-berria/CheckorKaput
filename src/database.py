import os
import re

from supabase import Client, create_client


PADRAO_HORARIO = re.compile(r"(?:[01]\d|2[0-3]):[0-5]\d")


def _get_secret(name: str) -> str:
    value = os.getenv(name)

    if value:
        return value

    try:
        import streamlit as st

        value = st.secrets.get(name)
    except Exception:
        value = None

    if not value:
        raise RuntimeError(f"Variável {name} não configurada.")

    return value


def get_client() -> Client:
    url = _get_secret("SUPABASE_URL")
    key = _get_secret("SUPABASE_KEY")
    return create_client(url, key)


def cadastrar_medicamento(nome: str, horarios: list[str]) -> dict:
    nome = nome.strip()

    if not nome:
        raise ValueError("Nome do medicamento não pode ser vazio.")

    if not horarios:
        raise ValueError("Informe pelo menos um horário.")

    horarios = [horario.strip() for horario in horarios if horario.strip()]

    if not horarios:
        raise ValueError("Informe pelo menos um horário.")

    if any(PADRAO_HORARIO.fullmatch(horario) is None for horario in horarios):
        raise ValueError("Horário inválido. Use o formato HH:MM.")

    dados = {
        "nome": nome,
        "horarios": horarios,
    }

    resposta = get_client().table("medicamentos").insert(dados).execute()
    return resposta.data[0]


def listar_medicamentos() -> list[dict]:
    resposta = (
        get_client()
        .table("medicamentos")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return resposta.data


def remover_medicamento(medicamento_id: str) -> list[dict]:
    resposta = (
        get_client().table("medicamentos").delete().eq("id", medicamento_id).execute()
    )

    return resposta.data


def registrar_tomada(medicamento_id: str) -> dict:
    dados = {
        "medicamento_id": medicamento_id,
    }

    resposta = get_client().table("registros_tomada").insert(dados).execute()
    return resposta.data[0]


def listar_historico() -> list[dict]:
    resposta = (
        get_client()
        .table("registros_tomada")
        .select("id, tomado_em, medicamentos(nome)")
        .order("tomado_em", desc=True)
        .execute()
    )

    return resposta.data
