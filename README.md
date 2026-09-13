# CheckorKaput

Aplicação desenvolvida para auxiliar no controle de medicamentos, horários e registros de uso, buscando reduzir esquecimentos e facilitar o acompanhamento da rotina de tratamento.

## Aplicação publicada

A aplicação Streamlit do projeto está publicada em:

https://checkorkaput-fw7oxgsm84l32czslsqjtk.streamlit.app/

---

## Problema

Muitas pessoas, especialmente idosos, pacientes em tratamento contínuo ou pessoas com rotinas ocupadas, podem ter dificuldade para lembrar dos horários dos medicamentos.

O CheckorKaput foi desenvolvido para auxiliar nesse acompanhamento por meio do cadastro de medicamentos, horários e registros de tomadas.

---

## Solução

O projeto possui uma aplicação CLI para gerenciamento dos medicamentos e registros de tomadas, além de uma interface Streamlit para consulta informativa de medicamentos por meio de uma API pública.

Entre as funcionalidades do sistema estão:

- Cadastro de medicamentos e horários;
- Listagem de medicamentos;
- Registro de medicamento tomado;
- Remoção de medicamentos;
- Consulta do histórico de tomadas;
- Consulta informativa de medicamentos por API pública;
- Persistência dos dados utilizando Supabase/PostgreSQL.

---

## Público-alvo

- Idosos;
- Pacientes em tratamento contínuo;
- Pessoas com rotinas ocupadas;
- Cuidadores.

---

## Equipe

- Gianluca Berria
- Carlos 
- Emmanuel Avelino

---

## Arquitetura do projeto

A estrutura principal do projeto é organizada da seguinte forma:

```text
CheckorKaput/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   └── SPEC.md
├── src/
│   ├── database.py
│   ├── drug_api.py
│   ├── main.py
│   ├── reminder.py
│   └── storage.py
├── tests/
├── AGENTS.md
├── pytest.ini
├── requirements.txt
├── streamlit_app.py
└── README.md
```

### Principais componentes

- `src/main.py`: entrada principal da aplicação CLI e menu de operações.
- `src/database.py`: funções relacionadas à persistência e consulta dos dados.
- `src/drug_api.py`: integração com a API pública de medicamentos.
- `src/reminder.py`: funcionalidades relacionadas aos lembretes e horários.
- `src/storage.py`: funcionalidades auxiliares de armazenamento.
- `streamlit_app.py`: interface Streamlit para consulta informativa de medicamentos.
- `tests/`: testes automatizados do projeto.
- `docs/SPEC.md`: especificação técnica do sistema.
- `AGENTS.md`: configuração e orientações do fluxo de desenvolvimento com agente de IA.
- `.github/workflows/ci.yml`: configuração do processo de integração contínua.

---

## Tecnologias utilizadas

- Python
- pytest
- Ruff
- Git
- GitHub
- GitHub Actions
- Streamlit
- Supabase/PostgreSQL
- API pública de medicamentos

---

## Pré-requisitos

É necessário ter Python instalado para executar o projeto localmente.

Recomenda-se utilizar um ambiente virtual para instalar as dependências do projeto.

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/gianluca-berria/CheckorKaput.git
cd CheckorKaput
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração do Supabase

A aplicação utiliza variáveis de ambiente para acessar o Supabase.

Configure:

```text
SUPABASE_URL
SUPABASE_KEY
```

No PowerShell, por exemplo:

```powershell
$env:SUPABASE_URL="sua_url_do_supabase"
$env:SUPABASE_KEY="sua_chave_do_supabase"
```

As credenciais não devem ser versionadas no repositório.

---

## Execução da CLI

Com o ambiente virtual ativado:

```bash
python src/main.py
```

A CLI permite realizar as operações disponíveis no sistema, incluindo cadastro, listagem, registro de tomadas, remoção e consulta do histórico.

---

## Execução do Streamlit

Para executar a interface Streamlit localmente:

```bash
streamlit run streamlit_app.py
```

A interface possui foco na consulta informativa de medicamentos utilizando uma API pública.

---

## Testes automatizados

O projeto utiliza `pytest` para execução dos testes.

Execute:

```bash
python -m pytest
```

Para executar os testes diretamente com pytest:

```bash
pytest
```

Os testes estão organizados no diretório `tests/`.

---

## Lint

O projeto utiliza Ruff para análise estática e verificação de qualidade do código.

Execute:

```bash
ruff check .
```

---

## Integração Contínua

O projeto possui configuração de GitHub Actions para automatizar verificações do código.

O workflow está definido em:

```text
.github/workflows/ci.yml
```

Entre as verificações estão a instalação das dependências, análise com Ruff e execução dos testes automatizados.

---

## Governança de Branches e Pull Requests

O projeto utiliza branches específicas para organizar o desenvolvimento.

### `main`

A branch `main` representa a versão estável do projeto.

Alterações devem ser incorporadas por meio de Pull Requests e revisão de outro integrante da equipe.

### `develop`

A branch `develop` é utilizada como branch de integração.

As alterações desenvolvidas nas branches específicas das tarefas são encaminhadas primeiro para `develop`.

### Branches de tarefas

Cada Issue deve ser desenvolvida em uma branch própria.

Exemplos:

- `12`
- `15`
- `19`

### Fluxo

```text
main
  ↑
  │ Pull Request + revisão
  │
develop
  ↑
  │ Pull Request + revisão
  │
branch da tarefa
```

O fluxo adotado é:

1. Criar uma branch para a Issue.
2. Desenvolver a alteração na branch.
3. Executar testes e verificações.
4. Enviar a branch para o GitHub.
5. Abrir Pull Request para `develop`.
6. Solicitar revisão de outro integrante.
7. Integrar após aprovação.
8. Após validação, integrar `develop` em `main` por Pull Request.

---

## Especificação técnica

A especificação técnica do projeto está documentada em:

```text
docs/SPEC.md
```

O documento descreve as definições técnicas e estruturais utilizadas como referência para o desenvolvimento do sistema.

---

## Agente de IA e SDD

O projeto possui o arquivo:

```text
AGENTS.md
```

Esse arquivo contém as orientações utilizadas no fluxo de desenvolvimento com agente de IA e na abordagem de SDD adotada no projeto.

---

## Docker

No estado atual do projeto utilizado para esta documentação, não foi identificado um `Dockerfile` no repositório.

Portanto, a execução principal documentada neste README é realizada diretamente pelo ambiente Python.

---

## ADRs

No estado atual do projeto utilizado para esta documentação, não foi identificada uma estrutura de ADRs no repositório.

Caso decisões arquiteturais sejam registradas posteriormente em ADRs, elas deverão ser adicionadas à documentação do projeto e referenciadas nesta seção.

---

## Evidências

As evidências do desenvolvimento devem ser registradas por meio dos Pull Requests, Issues, resultados dos testes automatizados e demais registros do processo de desenvolvimento.

Os testes podem ser executados com:

```bash
python -m pytest
```

E a verificação de qualidade pode ser executada com:

```bash
ruff check .
```

---

## Repositório

https://github.com/gianluca-berria/CheckorKaput

---

## Versão

1.0.0
