# CheckorKaput

[![Test Harness](https://github.com/gianluca-berria/CheckorKaput/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/gianluca-berria/CheckorKaput/actions/workflows/ci.yml)

Aplicação em Python para auxiliar no cadastro, acompanhamento e consulta informativa de medicamentos.

•⁠  ⁠[Aplicação web publicada](https://checkorkaput-fw7oxgsm84l32czslsqjtk.streamlit.app/)
•⁠  ⁠[Especificação técnica](docs/SPEC.md)
•⁠  ⁠[Execuções do GitHub Actions](https://github.com/gianluca-berria/CheckorKaput/actions)

## Visão geral

O CheckorKaput possui dois fluxos principais:

•⁠  ⁠uma interface de linha de comando para cadastrar, listar e remover medicamentos, registrar tomadas e consultar o histórico;
•⁠  ⁠uma interface web em Streamlit para consultar informações públicas sobre medicamentos na API openFDA.

A persistência principal utiliza Supabase. Os componentes de armazenamento em JSON pertencem à implementação anterior e são mantidos temporariamente como legado.

As informações consultadas na openFDA possuem caráter exclusivamente informativo. O sistema não fornece diagnóstico, prescrição ou recomendação de tratamento e não substitui orientação médica ou farmacêutica.

## Funcionalidades

### Interface CLI

•⁠  ⁠cadastrar medicamentos e horários;
•⁠  ⁠validar nome e horários informados;
•⁠  ⁠listar medicamentos cadastrados;
•⁠  ⁠registrar tomadas;
•⁠  ⁠remover medicamentos;
•⁠  ⁠consultar o histórico de tomadas;
•⁠  ⁠armazenar dados no Supabase.

### Interface web

•⁠  ⁠consultar medicamentos pelo nome genérico;
•⁠  ⁠apresentar nome genérico, nome comercial, fabricante, tipo de produto e avisos;
•⁠  ⁠informar quando campos não estiverem disponíveis;
•⁠  ⁠tratar medicamentos não encontrados e falhas da API;
•⁠  ⁠exibir aviso sobre o caráter informativo da consulta.

## Arquitetura

| Componente         | Responsabilidade                                                 |
| ------------------ | ---------------------------------------------------------------- |
| ⁠ src/main.py ⁠      | Interface CLI e interação com o usuário                          |
| ⁠ src/database.py ⁠  | Persistência de medicamentos e tomadas no Supabase               |
| ⁠ src/drug_api.py ⁠  | Validação e integração com a API openFDA                         |
| ⁠ streamlit_app.py ⁠ | Interface web para consulta informativa                          |
| ⁠ tests/ ⁠           | Testes unitários, casos de borda e testes de integração          |
| ⁠ src/reminder.py ⁠  | Componente legado de manipulação em memória                      |
| ⁠ src/storage.py ⁠   | Componente legado de persistência em JSON                        |
| ⁠ data/meds.json ⁠   | Dados mantidos para compatibilidade com a implementação anterior |

As responsabilidades, contratos e regras do sistema estão detalhados em [⁠ docs/SPEC.md ⁠](docs/SPEC.md).

## Tecnologias

•⁠  ⁠Python 3.12;
•⁠  ⁠Streamlit;
•⁠  ⁠Supabase;
•⁠  ⁠Requests;
•⁠  ⁠pytest;
•⁠  ⁠Ruff;
•⁠  ⁠Docker;
•⁠  ⁠GitHub Actions.

## Preparação do ambiente local

### Requisitos

•⁠  ⁠Git;
•⁠  ⁠Python 3.12;
•⁠  ⁠Docker, caso seja utilizado o ambiente padronizado.

### Clonar o repositório

⁠ bash
git clone https://github.com/gianluca-berria/CheckorKaput.git
cd CheckorKaput
git switch develop
 ⁠

### Criar o ambiente virtual

Linux ou macOS:

⁠ bash
python3.12 -m venv venv
source venv/bin/activate
 ⁠

Windows PowerShell:

⁠ powershell
py -3.12 -m venv venv
venv\Scripts\Activate.ps1
 ⁠

### Instalar as dependências

⁠ bash
python -m pip install -r requirements.txt
 ⁠

## Configuração do Supabase

A interface CLI requer as variáveis ⁠ SUPABASE_URL ⁠ e ⁠ SUPABASE_KEY ⁠.

Crie um arquivo ⁠ .env ⁠ na raiz do projeto:

⁠ env
SUPABASE_URL=sua_url
SUPABASE_KEY=sua_chave
 ⁠

O arquivo ⁠ .env ⁠ está ignorado pelo Git e não deve ser enviado ao repositório.

No ambiente local, exporte as variáveis antes de iniciar a CLI:

⁠ bash
set -a
source .env
set +a
 ⁠

No Windows PowerShell:

⁠ powershell
$env:SUPABASE_URL="sua_url"
$env:SUPABASE_KEY="sua_chave"
 ⁠

## Execução

### Interface CLI

⁠ bash
python -m src.main
 ⁠

### Interface web

⁠ bash
streamlit run streamlit_app.py
 ⁠

A interface ficará disponível em ⁠ http://localhost:8501 ⁠.

## Testes e qualidade

### Executar a suíte

⁠ bash
python -m pytest -q
 ⁠

### Executar o Ruff

⁠ bash
ruff check .
 ⁠

## Ambiente Docker

O ⁠ Dockerfile ⁠ fornece um ambiente padronizado com Python 3.12 e todas as dependências necessárias.

### Construir a imagem

⁠ bash
docker build -t checkorkaput .
 ⁠

Em sistemas que exigem privilégios administrativos:

⁠ bash
sudo docker build -t checkorkaput .
 ⁠

### Executar a CLI

⁠ bash
docker run --rm -it --env-file .env checkorkaput
 ⁠

### Executar a interface web

⁠ bash
docker run --rm -p 8501:8501 checkorkaput \
  streamlit run streamlit_app.py --server.address=0.0.0.0
 ⁠

### Executar os testes

⁠ bash
docker run --rm checkorkaput pytest -q
 ⁠

### Executar o Ruff

⁠ bash
docker run --rm checkorkaput ruff check .
 ⁠

## Test harness e evidências

A suíte atual cobre:

•⁠  ⁠regras de cadastro e validação;
•⁠  ⁠horários ausentes, vazios e inválidos;
•⁠  ⁠persistência simulada;
•⁠  ⁠fluxos da CLI;
•⁠  ⁠integração entre CLI e camada de persistência;
•⁠  ⁠consulta e tratamento de respostas da openFDA;
•⁠  ⁠componentes legados ainda mantidos.

Validação realizada em 13 de setembro de 2026 no ambiente Docker:

⁠ text
............................                                             [100%]
28 passed in 0.52s
 ⁠

Verificação de qualidade:

⁠ text
All checks passed!
 ⁠

## Integração contínua

O workflow [⁠ .github/workflows/ci.yml ⁠](.github/workflows/ci.yml) é executado em pushes e Pull Requests.

O pipeline:

1.⁠ ⁠prepara o Python 3.12;
2.⁠ ⁠instala as dependências;
3.⁠ ⁠executa o Ruff;
4.⁠ ⁠executa o pytest;
5.⁠ ⁠gera um relatório JUnit XML;
6.⁠ ⁠armazena o relatório como artefato durante 30 dias.

Uma falha no lint ou nos testes resulta em falha do pipeline.

### Evidência do pipeline

A execução mais recente da ⁠ develop ⁠ foi concluída com sucesso:

•⁠  ⁠[GitHub Actions — execução 57](https://github.com/gianluca-berria/CheckorKaput/actions/runs/34779301931)
•⁠  ⁠resultado: ⁠ success ⁠;
•⁠  ⁠artefato gerado: ⁠ pytest-results ⁠;
•⁠  ⁠estado do artefato: disponível.

## Desenvolvimento orientado pela especificação

O projeto segue Spec-Driven Development:

1.⁠ ⁠a tarefa é registrada em uma issue;
2.⁠ ⁠a equipe consulta [⁠ docs/SPEC.md ⁠](docs/SPEC.md);
3.⁠ ⁠uma branch específica é criada a partir da ⁠ develop ⁠;
4.⁠ ⁠código, testes e documentação são mantidos consistentes;
5.⁠ ⁠pytest e Ruff são executados;
6.⁠ ⁠a alteração é enviada por Pull Request;
7.⁠ ⁠outro integrante realiza a revisão;
8.⁠ ⁠a mudança aprovada é integrada à ⁠ develop ⁠;
9.⁠ ⁠alterações estáveis seguem da ⁠ develop ⁠ para a ⁠ main ⁠.

## Agente de IA

O ChatGPT foi utilizado como agente auxiliar durante a Entrega 1 para:

•⁠  ⁠analisar a especificação;
•⁠  ⁠planejar alterações;
•⁠  ⁠auxiliar na geração e revisão de código;
•⁠  ⁠propor casos de teste;
•⁠  ⁠auxiliar na documentação;
•⁠  ⁠revisar resultados de execução.

As regras de atuação do agente estão registradas em [⁠ AGENTS.md ⁠](AGENTS.md). As decisões finais e a revisão das alterações permanecem sob responsabilidade dos integrantes da equipe.

## Governança de branches

| Branch      | Finalidade                            |
| ----------- | ------------------------------------- |
| ⁠ main ⁠      | Versão estável                        |
| ⁠ develop ⁠   | Integração das alterações da iteração |
| ⁠ feature/* ⁠ | Funcionalidades                       |
| ⁠ test/* ⁠    | Testes                                |
| ⁠ docs/* ⁠    | Documentação                          |
| ⁠ ci/* ⁠      | Integração contínua                   |
| ⁠ chore/* ⁠   | Ambiente e manutenção                 |

Commits diretos na ⁠ main ⁠ devem ser evitados. As mudanças entram primeiro na ⁠ develop ⁠ por Pull Request e revisão de outro integrante.

## Decisões arquiteturais

•⁠  ⁠[ADR-001 — Ambiente reproduzível com Docker](docs/adr/ADR-001-ambiente-docker.md)
•⁠  ⁠[ADR-002 — Test harness com pytest e GitHub Actions](docs/adr/ADR-002-test-harness-e-ci.md)

Os refinamentos decorrentes das revisões e dos testes estão registrados na seção 14 da [especificação técnica](docs/SPEC.md).

## Pull Requests da Entrega 1

•⁠  ⁠[PR #20 — Especificação técnica SDD](https://github.com/gianluca-berria/CheckorKaput/pull/20)
•⁠  ⁠[PR #21 — Configuração do agente de IA](https://github.com/gianluca-berria/CheckorKaput/pull/21)
•⁠  ⁠[PR #23 — Expansão inicial dos testes](https://github.com/gianluca-berria/CheckorKaput/pull/23)
•⁠  ⁠[PR #24 — Governança de branches](https://github.com/gianluca-berria/CheckorKaput/pull/24)
•⁠  ⁠[PR #25 — Ambiente Docker](https://github.com/gianluca-berria/CheckorKaput/pull/25)
•⁠  ⁠[PR #26 — Casos de borda e integração](https://github.com/gianluca-berria/CheckorKaput/pull/26)
•⁠  ⁠[PR #27 — Test harness no GitHub Actions](https://github.com/gianluca-berria/CheckorKaput/pull/27)
•⁠  ⁠[PR #28 — ADRs e refinamentos](https://github.com/gianluca-berria/CheckorKaput/pull/28)

## Equipe

•⁠  ⁠Gianluca Berria — [⁠ gianluca-berria ⁠](https://github.com/gianluca-berria)
•⁠  ⁠Emmanuel Avelino — [⁠ DevManell ⁠](https://github.com/DevManell)

## Versão

⁠ 1.0.0 ⁠
