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

## 4. Escopo desta Iteração

Esta iteração utiliza como baseline a implementação já existente do CheckorKaput e busca formalizar seu desenvolvimento através de Spec-Driven Development.

Fazem parte do escopo desta iteração:

* documentação formal dos requisitos e regras de negócio;
* definição dos contratos de entrada e saída dos principais componentes;
* documentação da arquitetura e responsabilidades dos componentes;
* padronização do ambiente de execução;
* reorganização e expansão da infraestrutura de testes;
* inclusão de cenários de borda e testes de integração;
* execução automatizada dos testes através de integração contínua;
* registro das principais decisões arquiteturais;
* documentação do uso de agente de IA durante o desenvolvimento.

Funcionalidades não relacionadas aos objetivos definidos nesta especificação deverão ser tratadas como evoluções futuras do projeto.

## 5. Estado Atual da Arquitetura

A implementação atual é composta pelos seguintes elementos principais:

* `src/main.py`: interface de linha de comando e ponto de entrada das funcionalidades de gerenciamento de medicamentos;
* `src/database.py`: camada de acesso ao Supabase, responsável pela persistência dos medicamentos e registros de tomada;
* `src/drug_api.py`: integração com a API pública openFDA para consulta de informações sobre medicamentos;
* `streamlit_app.py`: interface web para consulta de medicamentos utilizando `src/drug_api.py`;
* `src/reminder.py`: implementação anterior das regras de manipulação de medicamentos em memória;
* `src/storage.py`: mecanismo anterior de persistência utilizando arquivo JSON;
* `tests/`: suíte de testes automatizados do sistema.

Os módulos `src/reminder.py` e `src/storage.py`, assim como o arquivo `data/meds.json`, pertencem a uma implementação anterior do projeto e são mantidos temporariamente por compatibilidade e suporte aos testes existentes.

A arquitetura utilizada como referência para novas alterações nesta iteração deverá priorizar os componentes atualmente utilizados pela aplicação.

## 6. Requisitos Funcionais

### RF-01 — Cadastrar medicamento

O sistema deve permitir o cadastro de um medicamento informando seu nome e pelo menos um horário de uso.

### RF-02 — Listar medicamentos

O sistema deve permitir a consulta dos medicamentos cadastrados, apresentando ao menos o nome e os horários associados a cada medicamento.

### RF-03 — Registrar tomada

O sistema deve permitir registrar que um medicamento cadastrado foi tomado.

O registro deve estar associado ao medicamento correspondente.

### RF-04 — Remover medicamento

O sistema deve permitir a remoção de um medicamento previamente cadastrado.

### RF-05 — Consultar histórico de tomadas

O sistema deve permitir consultar os registros de tomadas realizados anteriormente.

O histórico deve permitir identificar o medicamento relacionado e o momento em que a tomada foi registrada.

### RF-06 — Consultar informações de medicamento

O sistema deve permitir consultar informações públicas sobre um medicamento através da API openFDA utilizando seu nome genérico.

### RF-07 — Exibir informações obtidas da API

Quando a consulta à API openFDA retornar um medicamento, o sistema deve apresentar, quando disponíveis:

* nome genérico;
* nome comercial;
* fabricante;
* tipo de produto;
* avisos relacionados ao medicamento.

Quando determinada informação não estiver disponível, o sistema deverá apresentar uma indicação correspondente em vez de interromper a execução.

## 7. Requisitos Não Funcionais

### RNF-01 — Plataforma

A aplicação deve ser compatível com Python 3.12.

### RNF-02 — Testabilidade

Os comportamentos definidos nesta especificação devem possuir suporte para validação através de testes automatizados utilizando pytest.

### RNF-03 — Integração Contínua

A suíte de testes e as verificações de qualidade deverão poder ser executadas automaticamente através do GitHub Actions.

### RNF-04 — Reprodutibilidade

O projeto deverá possuir um ambiente padronizado que permita executar a aplicação e seus testes independentemente da configuração específica da máquina do desenvolvedor.

Nesta iteração, essa padronização será realizada utilizando Docker.

### RNF-05 — Configuração de credenciais

Credenciais e chaves necessárias para serviços externos não deverão ser armazenadas diretamente no código-fonte.

As configurações de acesso ao Supabase deverão ser fornecidas através de variáveis de ambiente ou mecanismo equivalente de gerenciamento de segredos.

### RNF-06 — Independência de serviços externos nos testes

Os testes automatizados não deverão depender da disponibilidade imprevisível de serviços externos para concluir a suíte principal com sucesso.

Integrações externas deverão ser isoladas ou simuladas quando necessário.

## 8. Regras de Negócio

### RN-01 — Nome obrigatório

Um medicamento não poderá ser cadastrado com nome vazio ou composto apenas por espaços em branco.

### RN-02 — Horário obrigatório

Todo medicamento cadastrado deverá possuir pelo menos um horário de uso informado.

Entradas vazias não deverão ser consideradas horários válidos.

### RN-03 — Formato de horário

Os horários informados para um medicamento deverão utilizar um formato de hora válido no padrão `HH:MM`.

Valores que não representem horários válidos deverão ser rejeitados.

### RN-04 — Registro de tomada

Uma tomada somente deverá ser registrada para um medicamento existente.

Tentativas de registrar uma tomada para um medicamento inexistente deverão resultar em erro controlado ou indicação de que o medicamento não foi encontrado.

### RN-05 — Remoção de medicamento

Somente medicamentos existentes poderão ser removidos.

Quando o identificador informado não corresponder a um medicamento cadastrado, o sistema deverá indicar que nenhum medicamento foi encontrado em vez de informar sucesso na operação.

### RN-06 — Consulta externa

A consulta à API openFDA deverá exigir um nome de medicamento não vazio.

Consultas vazias ou compostas apenas por espaços deverão ser rejeitadas antes da requisição ao serviço externo.

### RN-07 — Medicamento não encontrado na API

Quando a API não retornar resultados para o medicamento consultado, o sistema deverá tratar a situação como medicamento não encontrado, sem causar encerramento inesperado da aplicação.

### RN-08 — Caráter informativo

As informações obtidas através da API openFDA possuem finalidade exclusivamente informativa e não deverão ser apresentadas como diagnóstico, prescrição ou recomendação de tratamento.

## 9. Contratos de Entrada e Saída

### 9.1 Cadastro de medicamento

**Entrada:**

* `nome`: texto contendo o nome do medicamento;
* `horarios`: lista contendo um ou mais horários no formato `HH:MM`.

**Saída esperada:**

* medicamento cadastrado com identificador persistente;
* confirmação de sucesso ao usuário.

**Erros esperados:**

* nome vazio;
* ausência de horários válidos;
* horário em formato inválido;
* falha de comunicação com a camada de persistência.

---

### 9.2 Listagem de medicamentos

**Entrada:**

* não requer dados adicionais do usuário.

**Saída esperada:**

Uma coleção de medicamentos cadastrados contendo, no mínimo:

* identificador;
* nome;
* horários associados.

Quando não existirem medicamentos cadastrados, o sistema deverá informar que nenhum medicamento foi encontrado.

---

### 9.3 Registro de tomada

**Entrada:**

* identificador de um medicamento existente.

**Saída esperada:**

* criação de um registro de tomada associado ao medicamento;
* data e hora do registro deverão ser mantidas pela camada de persistência;
* confirmação da operação ao usuário.

**Erros esperados:**

* identificador inexistente ou inválido;
* falha na persistência do registro.

---

### 9.4 Remoção de medicamento

**Entrada:**

* identificador do medicamento a ser removido.

**Saída esperada:**

* confirmação da remoção quando o medicamento existir.

**Erros esperados:**

* identificador inexistente ou inválido;
* falha de comunicação com a camada de persistência.

---

### 9.5 Consulta do histórico

**Entrada:**

* não requer dados adicionais do usuário.

**Saída esperada:**

Uma coleção de registros de tomada contendo informações que permitam identificar:

* o medicamento relacionado;
* o momento em que a tomada foi registrada.

Quando não houver registros, o sistema deverá informar que o histórico está vazio.

---

### 9.6 Consulta de medicamento na openFDA

**Entrada:**

* nome genérico do medicamento em formato textual.

**Saída esperada:**

Quando encontrado, um objeto contendo:

* `nome_generico`;
* `nome_marca`;
* `fabricante`;
* `tipo_produto`;
* `aviso`.

Campos não disponíveis deverão utilizar a indicação `Não informado`.

Quando nenhum resultado for encontrado, a operação deverá retornar uma indicação de ausência de resultado.

**Erros esperados:**

* nome vazio;
* indisponibilidade da API;
* erro HTTP;
* resposta inválida do serviço externo.

## 10. Componentes do Sistema

### 10.1 Interface CLI — `src/main.py`

Responsável pela interação com o usuário através do terminal.

Suas responsabilidades incluem:

* apresentar o menu principal;
* coletar dados de entrada;
* solicitar operações à camada de banco de dados;
* apresentar resultados e mensagens de erro ao usuário.

A interface não deverá ser responsável pela implementação direta da persistência.

### 10.2 Persistência — `src/database.py`

Responsável pela comunicação com o Supabase.

Suas responsabilidades incluem:

* criação do cliente de conexão;
* cadastro de medicamentos;
* listagem de medicamentos;
* remoção de medicamentos;
* registro de tomadas;
* consulta ao histórico de tomadas.

As credenciais utilizadas para conexão não deverão ser armazenadas diretamente no código-fonte.

### 10.3 Integração openFDA — `src/drug_api.py`

Responsável pela comunicação com a API pública openFDA.

Suas responsabilidades incluem:

* validar a entrada básica da consulta;
* realizar a requisição HTTP;
* tratar resultados ausentes;
* extrair os campos utilizados pela aplicação;
* fornecer uma estrutura de dados simplificada para a camada de interface.

### 10.4 Interface Web — `streamlit_app.py`

Responsável pela interação web para consulta informativa de medicamentos.

Suas responsabilidades incluem:

* receber o nome do medicamento;
* solicitar a consulta a `src/drug_api.py`;
* exibir os dados retornados;
* informar quando nenhum medicamento for encontrado;
* tratar falhas de consulta sem encerrar inesperadamente a aplicação;
* apresentar aviso de caráter exclusivamente informativo.

### 10.5 Testes — `tests/`

Responsável pela validação automatizada dos comportamentos do sistema.

Durante esta iteração, a estrutura será reorganizada para distinguir testes unitários e testes de integração.

Os testes deverão possuir relação rastreável com os requisitos e regras definidos nesta especificação.

### 10.6 Componentes legados

Os arquivos:

* `src/reminder.py`;
* `src/storage.py`;
* `data/meds.json`;

fazem parte de uma implementação anterior do CheckorKaput.

Eles poderão permanecer no repositório durante esta iteração enquanto houver dependências ou testes relacionados a seu comportamento.

Novas funcionalidades não deverão depender desses componentes sem decisão arquitetural explícita.

## 11. Fluxos Principais

### 11.1 Cadastro de medicamento

1. O usuário seleciona a opção de cadastro.
2. A interface solicita o nome do medicamento.
3. A interface solicita os horários.
4. As entradas são validadas.
5. A camada de persistência registra o medicamento.
6. O sistema informa o resultado da operação.

### 11.2 Registro de tomada

1. O usuário solicita a listagem de medicamentos.
2. O sistema apresenta os medicamentos e seus identificadores.
3. O usuário seleciona um medicamento.
4. O sistema verifica a existência do medicamento.
5. Um registro de tomada é criado.
6. O sistema confirma a operação.

### 11.3 Consulta informativa

1. O usuário informa o nome genérico de um medicamento na interface web.
2. A entrada é validada.
3. O componente de integração realiza uma consulta à openFDA.
4. O resultado é tratado e simplificado.
5. A interface apresenta as informações disponíveis.
6. Caso nenhum resultado seja encontrado, o usuário é informado.

## 12. Fora de Escopo

Não fazem parte dos objetivos desta iteração:

* diagnóstico médico;
* recomendação de medicamentos;
* definição automática de doses;
* alteração de tratamentos;
* autenticação de usuários;
* notificações automáticas de horário;
* substituição de orientação médica ou farmacêutica;
* desenvolvimento de novas funcionalidades que não sejam necessárias para atender aos requisitos definidos nesta especificação.

Essas funcionalidades poderão ser consideradas em futuras evoluções do projeto mediante nova especificação.

## 13. Rastreabilidade

A tabela abaixo relaciona os requisitos funcionais às regras de negócio e às validações previstas para esta iteração.

| Requisito                                    | Regras relacionadas | Validação prevista                                                          |
| -------------------------------------------- | ------------------- | --------------------------------------------------------------------------- |
| RF-01 — Cadastrar medicamento                | RN-01, RN-02, RN-03 | Cadastro válido, nome vazio, ausência de horário e horário inválido         |
| RF-02 — Listar medicamentos                  | —                   | Listagem com registros e listagem vazia                                     |
| RF-03 — Registrar tomada                     | RN-04               | Registro para medicamento existente e tentativa com medicamento inexistente |
| RF-04 — Remover medicamento                  | RN-05               | Remoção de medicamento existente e tentativa com identificador inexistente  |
| RF-05 — Consultar histórico                  | —                   | Consulta com registros e histórico vazio                                    |
| RF-06 — Consultar informações de medicamento | RN-06, RN-07        | Consulta válida, entrada vazia e medicamento não encontrado                 |
| RF-07 — Exibir informações obtidas da API    | RN-07, RN-08        | Tratamento dos campos retornados, campos ausentes e ausência de resultado   |
