# Especificação Técnica — CheckorKaput

## 1. Visão Geral

O CheckorKaput é uma aplicação para auxílio no controle e consulta de medicamentos.

O sistema possui atualmente dois fluxos principais de utilização:

* uma interface de linha de comando (CLI), responsável pelo cadastro, listagem, remoção e registro de tomadas de medicamentos;
* uma interface web desenvolvida com Streamlit, responsável pela consulta informativa de medicamentos utilizando a API pública openFDA.

A aplicação utiliza Python como linguagem principal e possui infraestrutura de testes automatizados com pytest e integração contínua através do GitHub Actions.

Esta especificação estabelece os comportamentos, regras e componentes considerados na nova iteração do projeto, seguindo uma abordagem de Spec-Driven Development (SDD).

## 2. Problema

Pessoas que utilizam medicamentos de forma recorrente podem ter dificuldades para organizar seus horários de uso e manter um registro das doses já administradas.

Além disso, informações básicas sobre medicamentos podem estar dispersas em diferentes fontes, dificultando consultas rápidas pelo usuário.

O CheckorKaput busca oferecer mecanismos simples para registrar medicamentos e suas tomadas, bem como realizar consultas informativas utilizando uma fonte pública externa.

## 3. Objetivo

O objetivo do sistema é fornecer uma aplicação simples para:

* cadastrar medicamentos e seus respectivos horários;
* consultar os medicamentos cadastrados;
* registrar a tomada de um medicamento;
* remover medicamentos cadastrados;
* consultar o histórico de tomadas;
* consultar informações públicas sobre medicamentos através da API openFDA.

O sistema não tem como objetivo fornecer diagnóstico, prescrição, recomendação de tratamento ou substituir acompanhamento médico ou farmacêutico.

## 4. Escopo

Esta especificação descreve o estado atual (*As-Built*) do CheckorKaput, considerando a implementação existente no repositório.

O sistema possui duas interfaces independentes:

- **Interface CLI:** permite cadastrar, listar e remover medicamentos, registrar tomadas e consultar o histórico. As operações de persistência utilizam o Supabase.
- **Interface Web:** permite consultar informações de medicamentos por meio da API pública openFDA, utilizando o Streamlit.

A especificação documenta os requisitos funcionais e não funcionais implementados, as regras de negócio, os contratos observados no código, os componentes da arquitetura, as integrações externas e os testes automatizados existentes.

Também registra as limitações conhecidas e as decisões técnicas relevantes para compreender e manter a versão atual do projeto.

Não fazem parte do escopo funcionalidades futuras que ainda não estejam implementadas ou comprovadas pelo código e pelos testes.

## 5. Arquitetura atual

A arquitetura implementada do CheckorKaput é organizada em duas interfaces que utilizam integrações distintas.

### 5.1. Interface CLI

A interface de linha de comando está implementada em `src/main.py`. Ela apresenta o menu de operações e recebe as entradas do usuário.

As operações de persistência são delegadas ao módulo `src/database.py`, responsável por criar o cliente Supabase e executar as consultas nas tabelas utilizadas pelo sistema.

As funcionalidades disponíveis são:

- Cadastrar medicamentos com nome e horários.
- Listar medicamentos cadastrados.
- Registrar a tomada de um medicamento existente.
- Remover medicamentos cadastrados.
- Consultar o histórico de tomadas.

### 5.2. Interface Web

A interface Web está implementada em `streamlit_app.py`, utilizando o Streamlit.

Ela permite informar o nome genérico de um medicamento e consultar informações disponibilizadas pela API pública openFDA.

A comunicação com a API é realizada pelo módulo `src/drug_api.py`, que processa a resposta e retorna informações como nome genérico, nome comercial, fabricante, tipo de produto e aviso.

Essa interface possui finalidade exclusivamente informativa e não realiza diagnóstico ou recomendação de tratamento.

### 5.3. Persistência e integrações externas

A persistência da interface CLI utiliza o Supabase por meio da biblioteca `supabase-py`.

O módulo `src/database.py` consulta as tabelas `medicamentos` e `registros_tomada`. O código utiliza campos como `id`, `nome`, `horarios`, `created_at`, `medicamento_id` e `tomado_em`, além de uma consulta relacionada entre as duas tabelas para apresentar o histórico.

As credenciais são obtidas prioritariamente pelas variáveis de ambiente `SUPABASE_URL` e `SUPABASE_KEY`. Quando não estão disponíveis, o módulo tenta consultar os segredos do Streamlit (`st.secrets`).

A interface Web utiliza a API pública openFDA, por meio de requisições HTTP realizadas com a biblioteca Requests.

O repositório não contém scripts de criação do banco, migrações ou definição completa do esquema SQL. Portanto, os tipos, as restrições, as políticas de acesso e os relacionamentos físicos do banco remoto não são especificados nesta documentação.

### 5.4. Testes automatizados

Os testes estão organizados no diretório `tests/` e verificam comportamentos da interface CLI, operações do módulo de persistência e integração com a API openFDA.

As integrações externas são simuladas por meio de mocks e objetos de teste, permitindo validar os comportamentos sem depender de chamadas reais ao Supabase ou à API openFDA.

A interface Streamlit não possui testes automatizados específicos no conjunto atual.

### 5.5. Estrutura principal do projeto

- `src/main.py`: menu e fluxo da interface CLI.
- `src/database.py`: operações de persistência no Supabase.
- `src/drug_api.py`: consulta e tratamento das respostas da API openFDA.
- `streamlit_app.py`: interface Web com Streamlit.
- `tests/`: testes automatizados.
- `docs/`: especificações e documentação técnica.

## 6. Requisitos funcionais

Os requisitos funcionais abaixo descrevem as funcionalidades presentes na implementação atual.

| ID | Requisito | Implementação |
|---|---|---|
| RF-01 | Cadastrar medicamentos | O usuário informa o nome e um ou mais horários. Os dados são enviados à tabela `medicamentos` do Supabase. |
| RF-02 | Listar medicamentos | O sistema consulta os medicamentos cadastrados e apresenta seus nomes e horários na CLI. |
| RF-03 | Registrar tomada | O usuário seleciona um medicamento existente pelo ID. O sistema registra a tomada na tabela `registros_tomada`. |
| RF-04 | Remover medicamento | O usuário seleciona um medicamento existente pelo ID e solicita sua remoção. |
| RF-05 | Consultar histórico | O sistema consulta os registros de tomada e apresenta os dados retornados pelo Supabase. |
| RF-06 | Consultar informações de medicamentos | A interface Web permite pesquisar um medicamento pelo nome genérico na API pública openFDA. |
| RF-07 | Apresentar informações da consulta | A interface Web apresenta nome genérico, nome comercial, fabricante, tipo de produto e aviso, quando disponibilizados pela API. |

As funcionalidades de cadastro, listagem, registro de tomada, remoção e histórico pertencem à interface CLI. A consulta à openFDA pertence à interface Web e não representa uma integração com o cadastro de medicamentos do Supabase.

## 7. Requisitos não funcionais

Os requisitos não funcionais descrevem características técnicas e operacionais observadas na implementação atual.

| ID | Requisito | Situação na implementação |
|---|---|---|
| RNF-01 | Compatibilidade com Python 3.12 | O ambiente de CI e a imagem Docker utilizam Python 3.12. |
| RNF-02 | Testes automatizados | O projeto utiliza pytest. A execução atual da suíte apresenta 36 testes aprovados. |
| RNF-03 | Integração contínua | O GitHub Actions executa verificações com Ruff e pytest. |
| RNF-04 | Empacotamento com Docker | O repositório possui Dockerfile baseado em `python:3.12-slim`. A validação local depende de um ambiente com Docker instalado. |
| RNF-05 | Proteção de credenciais | As credenciais do Supabase são obtidas por variáveis de ambiente ou pelos segredos do Streamlit, sem necessidade de mantê-las diretamente no código-fonte. |
| RNF-06 | Isolamento de integrações externas nos testes | Os testes utilizam mocks e objetos simulados para verificar os comportamentos sem depender de serviços externos reais. |

A existência de configurações e arquivos de infraestrutura não representa, por si só, comprovação de execução em todos os ambientes. As validações devem ser registradas conforme as evidências disponíveis.

## 8. Regras de negócio

As regras abaixo refletem as validações observadas no código da versão atual.

| ID | Regra | Comportamento implementado |
|---|---|---|
| RN-01 | Nome obrigatório | O cadastro rejeita nomes vazios ou compostos apenas por espaços. |
| RN-02 | Horário obrigatório | O cadastro exige pelo menos um horário válido. |
| RN-03 | Formato de horário | Os horários devem seguir o formato `HH:MM`, com horas entre `00` e `23` e minutos entre `00` e `59`. |
| RN-04 | Medicamento existente para registrar tomada | O sistema verifica a existência do medicamento antes de inserir o registro de tomada. |
| RN-05 | Medicamento existente para remoção | A CLI verifica se o ID informado pertence a um medicamento listado antes de solicitar a remoção. |
| RN-06 | Consulta openFDA com entrada | A função de consulta rejeita nomes vazios ou compostos apenas por espaços. |
| RN-07 | Consulta sem resultados | Quando a API retorna HTTP 404 ou não apresenta resultados, a função retorna `None`. |
| RN-08 | Uso informativo | A consulta apresenta informações disponibilizadas pela API e não realiza diagnóstico nem recomenda tratamento. |

As regras de validação da CLI e as validações internas do módulo de persistência não são necessariamente idênticas. A documentação considera o comportamento efetivamente observado em cada camada.

## 9. Contratos

Esta seção descreve os contratos observados nos módulos da implementação atual. Os retornos apresentados correspondem às estruturas utilizadas pelo código, não a uma definição completa do esquema físico do Supabase.

### 9.1. Cadastro de medicamento

A função `cadastrar_medicamento(nome, horarios)`, em `src/database.py`, recebe o nome do medicamento e uma lista de horários.

- Remove espaços excedentes do nome e dos horários.
- Rejeita nome vazio, lista de horários vazia e horários fora do padrão `HH:MM`.
- Insere os dados na tabela `medicamentos`.
- Retorna o primeiro registro disponibilizado pela resposta do Supabase.
- A implementação acessa diretamente o primeiro elemento da resposta (`resposta.data[0]`), sem verificar se a lista está vazia. Portanto, uma resposta sem registros pode gerar `IndexError`.

### 9.2. Listagem de medicamentos

A função `listar_medicamentos()` consulta a tabela `medicamentos`, seleciona os campos disponíveis (`*`) e ordena os resultados por `created_at`, em ordem decrescente.

Retorna a lista de registros fornecida pelo Supabase.

### 9.3. Registro de tomada

A função `registrar_tomada(medicamento_id)`:

1. Remove espaços excedentes do ID.
2. Rejeita um ID vazio.
3. Verifica se o medicamento existe na tabela `medicamentos`.
4. Insere o ID em `medicamento_id`, na tabela `registros_tomada`.
5. Retorna o primeiro registro inserido.

Caso o medicamento não exista, gera `ValueError`. Caso a resposta da inserção não contenha dados, gera `RuntimeError`.

### 9.4. Remoção de medicamento

A função `remover_medicamento(medicamento_id)` solicita a exclusão do registro na tabela `medicamentos`, filtrando pelo campo `id`.

Retorna os dados fornecidos pela resposta do Supabase. A validação prévia da existência do medicamento é realizada pela interface CLI.

A função de persistência não realiza validação interna de ID vazio ou de existência do medicamento. Essas verificações são responsabilidade da CLI. Se nenhum registro corresponder ao ID informado, a resposta do Supabase poderá retornar uma lista vazia.

### 9.5. Consulta ao histórico

A função `listar_historico()` consulta a tabela `registros_tomada`, selecionando `id`, `tomado_em` e o nome relacionado do medicamento (`medicamentos(nome)`).

Os registros são ordenados por `tomado_em`, em ordem decrescente, e retornados conforme a resposta do Supabase.

### 9.6. Consulta à API openFDA

A função `consultar_medicamento(nome)`, em `src/drug_api.py`, recebe o nome genérico do medicamento.

A requisição utiliza o endpoint `https://api.fda.gov/drug/label.json`, com os parâmetros:

- `search`: pesquisa pelo campo `openfda.generic_name`.
- `limit`: limita a consulta a um resultado.
- `timeout`: define o limite de espera da requisição em 10 segundos.

Quando encontra um resultado, retorna um dicionário com os campos `nome_generico`, `nome_marca`, `fabricante`, `tipo_produto` e `aviso`.

Quando recebe HTTP 404 ou uma resposta sem resultados, retorna `None`. Outros erros HTTP podem ser propagados pela biblioteca Requests.

### 9.7. Configuração do Supabase

A conexão utiliza as credenciais `SUPABASE_URL` e `SUPABASE_KEY`.

O código procura primeiro as variáveis de ambiente e, quando não estão disponíveis, tenta obter os valores por meio de `st.secrets`. Se as credenciais não forem encontradas, gera `RuntimeError`.

Os detalhes físicos do banco remoto, como tipos de dados, chaves, restrições e políticas de acesso, não são definidos pelos contratos Python descritos nesta seção.

## 10. Componentes

### 10.1. Interface CLI — `src/main.py`

Responsável por apresentar o menu de operações, receber as entradas do usuário e encaminhar as solicitações ao módulo de persistência.

As opções disponíveis são cadastro, listagem, registro de tomada, remoção, consulta ao histórico e encerramento.

Nas operações de registro de tomada e remoção, a CLI apresenta os medicamentos cadastrados e verifica o ID informado antes de executar a operação.

### 10.2. Persistência — `src/database.py`

Responsável pela comunicação com o Supabase e pelas operações sobre as tabelas `medicamentos` e `registros_tomada`.

O módulo implementa cadastro, listagem, remoção, registro de tomada, consulta ao histórico e obtenção das credenciais necessárias à conexão.

### 10.3. Integração openFDA — `src/drug_api.py`

Responsável por consultar a API pública openFDA, tratar respostas sem resultados e organizar os campos relevantes da primeira ocorrência retornada.

A requisição utiliza tempo limite de 10 segundos. Erros HTTP diferentes de 404 e outras falhas da biblioteca Requests podem ser propagados para a camada chamadora.

### 10.4. Interface Web — `streamlit_app.py`

Responsável pela interface de consulta informativa de medicamentos.

A aplicação valida a entrada antes da consulta, apresenta os dados retornados pela openFDA, informa quando não há resultados e exibe uma mensagem genérica quando ocorre uma exceção.

### 10.5. Testes automatizados — `tests/`

O diretório contém testes para:

- Comportamentos do menu CLI.
- Integração entre CLI e operações de persistência.
- Validações de medicamentos inexistentes.
- Operações do módulo de banco de dados.
- Integração simulada com a API openFDA.

As dependências externas são simuladas nos testes. Não há testes automatizados específicos para a interface Streamlit no conjunto atual.

### 10.6. Componentes legados

A implementação atual utiliza o Supabase como persistência da CLI. Componentes locais legados removidos durante a evolução do projeto não fazem parte da arquitetura descrita nesta especificação.

## 11. Fluxos

### 11.1. Fluxo de cadastro de medicamento

1. O usuário seleciona a opção de cadastro na CLI.
2. Informa o nome do medicamento e os horários separados por vírgula.
3. A CLI encaminha os dados para `cadastrar_medicamento()`.
4. O módulo de persistência valida os dados e solicita a inserção ao Supabase.
5. A CLI apresenta uma mensagem de sucesso ou de erro.

### 11.2. Fluxo de listagem

1. O usuário seleciona a opção de listagem.
2. A CLI chama `listar_medicamentos()`.
3. O módulo consulta a tabela `medicamentos`.
4. A CLI apresenta os medicamentos e seus horários ou informa que não existem registros.

### 11.3. Fluxo de registro de tomada

1. O usuário seleciona a opção de registrar tomada.
2. A CLI consulta os medicamentos cadastrados.
3. O usuário informa o ID do medicamento.
4. A CLI verifica se o ID está entre os medicamentos listados.
5. O módulo de persistência verifica novamente a existência do medicamento.
6. Se o medicamento existir, o sistema solicita a inserção do registro na tabela `registros_tomada`.

### 11.4. Fluxo de remoção

1. O usuário seleciona a opção de remoção.
2. A CLI consulta os medicamentos cadastrados.
3. O usuário informa o ID do medicamento.
4. A CLI verifica se o ID está entre os medicamentos listados.
5. O módulo solicita a exclusão do registro no Supabase.
6. A CLI apresenta a confirmação somente quando a resposta contém registros removidos.

### 11.5. Fluxo de consulta ao histórico

1. O usuário seleciona a opção de histórico.
2. A CLI chama `listar_historico()`.
3. O módulo consulta os registros de tomada e o nome relacionado do medicamento.
4. A CLI apresenta os dados retornados ou informa que não existem registros.

### 11.6. Fluxo de consulta pela interface Web

1. O usuário informa o nome genérico do medicamento no campo da aplicação Streamlit.
2. Seleciona o botão de consulta.
3. A interface verifica se o campo está preenchido.
4. A função `consultar_medicamento()` realiza a requisição à API openFDA.
5. A interface apresenta as informações encontradas, informa a ausência de resultados ou exibe uma mensagem genérica em caso de erro.

## 12. Fora do escopo

As funcionalidades abaixo não fazem parte da implementação atual do CheckorKaput:

- Diagnóstico de doenças ou condições de saúde.
- Prescrição, recomendação ou alteração de tratamentos e dosagens.
- Garantia de disponibilidade ou entrega de notificações nos horários cadastrados.
- Integração entre a consulta informativa da openFDA e o cadastro de medicamentos no Supabase.
- Consulta a múltiplos resultados da openFDA, pois a implementação limita a requisição a um resultado.
- Funcionamento da persistência da CLI sem conexão com o Supabase.
- Definição ou administração automática do esquema físico do banco remoto.
- Testes automatizados específicos da interface Streamlit.
- Funcionalidades que não estejam presentes no código atual ou comprovadas pelos testes disponíveis.

O CheckorKaput é uma ferramenta acadêmica de organização e consulta informativa. Não substitui orientação de profissionais de saúde.

## 13. Rastreabilidade

A tabela relaciona os requisitos funcionais aos principais módulos e testes existentes no repositório.

| Requisito | Implementação | Evidência de teste |
|---|---|---|
| RF-01 — Cadastrar medicamentos | `src/main.py` e `src/database.py` | `test_cli_database_integration.py` e `test_database.py` |
| RF-02 — Listar medicamentos | `src/main.py` e `src/database.py` | `test_main.py` e `test_database.py` |
| RF-03 — Registrar tomada | `src/main.py` e `src/database.py` | `test_cli_database_integration.py`, `test_cli_missing_medications.py` e `test_database_missing_medications.py` |
| RF-04 — Remover medicamento | `src/main.py` e `src/database.py` | `test_cli_database_integration.py` e `test_cli_missing_medications.py` |
| RF-05 — Consultar histórico | `src/main.py` e `src/database.py` | `test_database.py` |
| RF-06 — Consultar informações de medicamentos | `src/drug_api.py` e `streamlit_app.py` | `test_drug_api_integration.py` |
| RF-07 — Apresentar informações da consulta | `src/drug_api.py` e `streamlit_app.py` | Tratamento dos campos verificado em `test_drug_api_integration.py`; apresentação visual sem teste automatizado específico. |

### 13.1. Cobertura dos testes

Na validação realizada durante esta documentação, a suíte apresentou **36 testes aprovados**.

Os testes verificam operações da CLI, regras de persistência e integração simulada com a openFDA.

A suíte atual não comprova:

- A disponibilidade real do Supabase ou da API openFDA.
- A estrutura física completa do banco remoto.
- O comportamento visual e a interação da interface Streamlit.
- Todos os cenários de falha possíveis das integrações externas.

A aprovação dos testes demonstra os comportamentos cobertos pelos testes automatizados, não a ausência de defeitos em todo o sistema.

## 14. Refinamentos da Especificação

### 14.1 Normalização e validação de horários

Os testes da PR #26 revelaram que a implementação aceitava entradas incompatíveis com RN-02 e RN-03.

Ficou explicitado que:

* espaços no início e no fim de cada horário devem ser removidos;
* entradas vazias após a normalização não são horários válidos;
* deve restar pelo menos um horário válido;
* o formato deve conter exatamente dois dígitos para a hora e dois para os minutos;
* a hora deve estar entre `00` e `23`;
* os minutos devem estar entre `00` e `59`.

Esse refinamento não altera a regra original; esclarece seus limites e registra a correção motivada pelos testes.

### 14.2 Limite dos testes de integração

Os testes de integração podem executar conjuntamente componentes internos reais, mantendo simulados somente os limites externos.

A PR #26 validou a integração entre a CLI e a camada de persistência, substituindo apenas o cliente do Supabase. Assim, o RNF-06 é preservado sem reduzir o teste a uma única unidade isolada.

### 14.3 Ambiente padronizado

A PR #25 confirmou que o ambiente Docker deve permitir executar:

* a interface CLI;
* a interface Streamlit;
* o pytest;
* o Ruff.

Credenciais deverão ser fornecidas em tempo de execução e não poderão ser incluídas na imagem.

### 14.4 Evidências da integração contínua

A PR #27 refinou a aplicação do RNF-03.

O pipeline deverá:

* executar em pushes e Pull Requests;
* utilizar Python 3.12;
* falhar quando o lint ou algum teste falhar;
* produzir relatório JUnit XML;
* manter o relatório como artefato utilizável na entrega.

### 14.5 Histórico

| Data       | Origem | Resultado                                                                         |
| ---------- | ------ | --------------------------------------------------------------------------------- |
| 2026-09-13 | PR #25 | Ambiente Docker construído e fluxos da aplicação validados.                       |
| 2026-09-13 | PR #26 | Casos de borda revelaram e motivaram a correção da validação de horários.         |
| 2026-09-13 | PR #26 | Definido o limite entre componentes internos reais e serviços externos simulados. |
| 2026-09-13 | PR #27 | Pipeline validado com logs e artefato de testes disponível.                       |

### 14.6 Decisões arquiteturais relacionadas

* [ADR-001 — Ambiente reproduzível com Docker](adr/ADR-001-ambiente-docker.md)
* [ADR-002 — Test harness com pytest e GitHub Actions](adr/ADR-002-test-harness-e-ci.md)

### 14.7 Operações com medicamentos inexistentes — Issue #31

A inspeção da CLI identificou que a remoção anunciava sucesso mesmo quando
a persistência retornava uma lista vazia. Também faltavam validação explícita
de existência no registro de tomada e tratamento de listas vazias nas duas
operações.

Foram corrigidos os comportamentos relacionados a RF-03, RF-04, RN-04 e RN-05:

- listas vazias apresentam mensagem informativa sem solicitar identificador;
- a CLI normaliza o identificador e rejeita IDs ausentes da listagem;
- a remoção somente anuncia sucesso quando retorna registros removidos;
- a persistência rejeita identificadores vazios e consulta a existência do
  medicamento antes de inserir uma tomada;
- respostas de inserção vazias produzem erro controlado.

Os testes de regressão cobrem os fluxos válidos e os casos de borda, incluindo
remoção sem resultado e medicamento ausente na consulta feita após a listagem.

Os testes de integração executam CLI e persistência reais, simulando apenas
o cliente externo. Não comprovam a configuração do Supabase nem a proteção
contra exclusão concorrente entre consulta e inserção; esta última depende
também da integridade referencial no banco.

Validação local em Docker em 12/10/2026: 42 testes aprovados e Ruff sem erros.
Este registro esclarece a aplicação das regras existentes, sem ampliar o
escopo funcional.

### 14.8 Higienização dos componentes legados — Issue #44

A remoção de `src/reminder.py`, `src/storage.py` e `data/meds.json` conclui a
limpeza prevista na issue #8. A inspeção confirmou que apenas os testes de
`reminder.py` importavam esses componentes; a CLI já utilizava `src/database.py`.

Os cenários de cadastro, nome obrigatório, registro de tomada, remoção e
medicamento inexistente (RF-01, RF-03, RF-04 e RN-01 a RN-05) permanecem
cobertos na camada atual. O cadastro com múltiplos horários foi incorporado
ao teste de persistência. Não há alteração dos contratos públicos atuais.

O documento duplicado de experiência e governança foi removido. Evidências
históricas da Entrega 2 permanecem como registro da versão então validada e
não representam a composição da suíte após esta limpeza.

### 14.9. Validação da versão atual

Durante a atualização desta especificação, foram executadas as seguintes verificações no ambiente Python 3.12:

| Verificação | Comando | Resultado |
|---|---|---|
| Testes automatizados | `python -m pytest -q` | 36 testes aprovados |
| Análise estática | `python -m ruff check .` | Todas as verificações aprovadas |

Esses resultados representam a validação realizada no ambiente local durante a atualização da documentação.

A validação não incluiu a execução de uma imagem Docker neste ambiente, pois o Docker não estava disponível. Também não representa uma verificação de disponibilidade dos serviços externos Supabase e openFDA.

Os resultados devem ser reavaliados caso ocorram alterações no código ou nos testes após este registro.
