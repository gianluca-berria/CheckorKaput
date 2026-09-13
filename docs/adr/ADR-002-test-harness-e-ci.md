# ADR-002 — Test harness com pytest e GitHub Actions

* **Status:** Aceita
* **Data:** 2026-09-13

## Contexto

A suíte precisava validar regras de negócio, casos de borda e integração entre componentes sem depender da disponibilidade do Supabase ou da openFDA.

Também era necessário detectar regressões automaticamente em pushes e Pull Requests e preservar evidências de execução.

## Decisão

Utilizar pytest como ferramenta principal do test harness.

Testes unitários deverão simular dependências externas. Testes de integração poderão executar componentes internos reais, simulando somente o limite externo, como o cliente Supabase ou uma requisição HTTP.

O GitHub Actions executará, com Python 3.12:

1. instalação das dependências;
2. verificação com Ruff;
3. execução da suíte;
4. geração de relatório JUnit XML;
5. armazenamento do relatório como artefato por 30 dias.

Falhas do Ruff ou do pytest deverão resultar em falha do pipeline.

## Alternativas consideradas

### Testes conectados aos serviços reais

Aumentariam o realismo, mas exigiriam credenciais e dependeriam da rede e da disponibilidade dos serviços.

### Validação exclusivamente manual

Não fornece repetibilidade nem detecção automática de regressões.

### Módulo unittest

Evitaria uma dependência adicional, porém o projeto já utiliza pytest e seus recursos de parametrização, monkeypatch e fixtures.

## Consequências

* testes rápidos, determinísticos e independentes da rede;
* ausência de credenciais reais na suíte;
* integração contínua em pushes e Pull Requests;
* relatórios disponíveis como evidência;
* necessidade de manter os mocks coerentes com os contratos externos;
* testes reais dos serviços poderão ser mantidos separadamente no futuro.

## Validação

Os casos de borda e o teste de integração foram implementados e aprovados na [PR #26](https://github.com/gianluca-berria/CheckorKaput/pull/26).

O pipeline foi atualizado e aprovado na [PR #27](https://github.com/gianluca-berria/CheckorKaput/pull/27).

A execução da `develop` foi concluída com sucesso e produziu o artefato `pytest-results`: [execução do GitHub Actions](https://github.com/gianluca-berria/CheckorKaput/actions/runs/34778422979).

## Relação com a especificação

Atende aos requisitos RNF-02, RNF-03 e RNF-06 e valida especialmente RN-02 e RN-03.
