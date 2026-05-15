Aplicação publicada: https://checkorkaput-fw7oxgsm84l32czslsqjtk.streamlit.app/

CheckorKaput

Uma aplicação CLI desenvolvida para auxiliar usuários no controle de medicamentos, horários e registros de uso, reduzindo esquecimentos e promovendo maior segurança no tratamento.

---

Problema:

Muitas pessoas, especialmente idosos, pacientes em tratamento contínuo ou indivíduos com rotinas intensas, enfrentam dificuldades para lembrar de tomar seus medicamentos nos horários corretos.

O esquecimento ou uso incorreto pode causar:

* agravamento de condições de saúde
* falha em tratamentos
* riscos à vida em casos mais críticos

---

Solução:

O "CheckorKaput" oferece uma forma simples e prática de:

* registrar medicamentos
* definir horários de uso
* acompanhar quando foram tomados

Tudo isso por meio de uma interface de linha de comando (CLI), leve e acessível.

---

Público-alvo:

* idosos
* pacientes em tratamento contínuo
* pessoas com rotinas ocupadas
* cuidadores

---

Funcionalidades:

* ➕ Adicionar medicamentos com horários
* 📋 Listar medicamentos cadastrados
* ✅ Marcar medicamento como tomado
* 💾 Persistência de dados em arquivo JSON

---

Tecnologias utilizadas:

* Python 3.12
* pytest (testes automatizados)
* ruff (lint/análise estática)
* Git e GitHub
* GitHub Actions (CI)

---

Instalação:

Clone o repositório:

```bash
git clone https://github.com/gianluca-berria/CheckorKaput.git
cd CheckorKaput
```

Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

Execução:

```bash
python src/main.py
```

---

Testes:

```bash
pytest
```

---

Lint (qualidade de código):

```bash
ruff check .
```

---

Integração Contínua (CI):

O projeto possui pipeline configurada no GitHub Actions que executa automaticamente:

* instalação de dependências
* verificação de lint
* execução dos testes

---

Versão:

```
1.0.0
```

---

Autor:

Gianluca Berria

---

Repositório:

https://github.com/gianluca-berria/CheckorKaput

---
