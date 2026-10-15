# Experiência da equipe e evidências de governança

## 1. Objetivo

Este documento registra aprendizados do desenvolvimento colaborativo do CheckorKaput e reúne referências verificáveis sobre organização do trabalho, qualidade, decisões técnicas e governança do repositório.

O relato usa como evidência os arquivos versionados e as Issues públicas do GitHub consultadas para esta entrega. Uma Issue descreve uma demanda e seus critérios; sozinha, ela não comprova que a tarefa foi concluída. Da mesma forma, a existência de testes ou de um workflow não comprova, por si só, que houve aprovação humana de um Pull Request.

**Repositório:** [gianluca-berria/CheckorKaput](https://github.com/gianluca-berria/CheckorKaput)

## 2. Equipe e responsabilidades

| Integrante / referência | Responsabilidade registrada ou observável | Evidência e limite |
|---|---|---|
| **Gianluca Berria (`gianluca-berria`)** | Responsável pelo repositório e autor de Issues que descrevem entregas e critérios. | [Repositório](https://github.com/gianluca-berria/CheckorKaput) e [Issue #34](https://github.com/gianluca-berria/CheckorKaput/issues/34). A autoria das Issues não prova, isoladamente, a autoria de todo o código. |
| **DevManell** | Atribuído à Issue de documentação e governança #34. | [Issue #34](https://github.com/gianluca-berria/CheckorKaput/issues/34). A atribuição confirma a responsabilidade pela tarefa, não a conclusão nem uma revisão já realizada. |
| **ChatGPT (IA auxiliar)** | Apoio à análise de requisitos, elaboração/revisão de documentação, sugestões de implementação e testes. | [AGENTS.md](../AGENTS.md) descreve o papel esperado da IA e determina revisão humana. O uso da IA não substitui decisões nem aprovação dos integrantes. |

> **Para completar antes do merge:** revisar o histórico de commits e Pull Requests e acrescentar, se necessário, quais arquivos ou commits cada integrante implementou/revisou. Não atribuir autoria técnica sem evidência no GitHub.

## 3. Organização do trabalho e entregas iterativas

O histórico público do repositório contém Issues que ajudam a reconstruir a evolução do trabalho. Os links abaixo são evidências das demandas e dos critérios definidos; o status atual de cada uma deve ser conferido no GitHub antes de afirmar que foi concluída.

| Etapa / tema | Evidência | O que registra |
|---|---|---|
| Consulta informativa de medicamentos por API pública | [Issue #1](https://github.com/gianluca-berria/CheckorKaput/issues/1) e [Issue/PR relacionado #2](https://github.com/gianluca-berria/CheckorKaput/issues/2) | A Issue #1 foi encerrada como concluída por meio do item #2, conforme o histórico exibido pelo GitHub. |
| Organização e ampliação dos testes | [Issue #15](https://github.com/gianluca-berria/CheckorKaput/issues/15) | Define a revisão do test harness e a separação/identificação de testes unitários e de integração. |
| Integração contínua | [Issue #17](https://github.com/gianluca-berria/CheckorKaput/issues/17) | Registra os critérios esperados para executar testes automaticamente em pushes e Pull Requests. |
| README e evidências da primeira entrega | [Issue #19](https://github.com/gianluca-berria/CheckorKaput/issues/19) | Lista requisitos de instalação, execução, Docker, CI, IA e evidências de testes. |
| Experiência e governança | [Issue #34](https://github.com/gianluca-berria/CheckorKaput/issues/34) | Solicita registrar responsabilidades, aprendizados, critérios de merge e evidências de revisão entre pares. |

O projeto também mantém a [especificação técnica](SPEC.md), o arquivo [AGENTS.md](../AGENTS.md), os ADRs em `docs/adr/`, testes automatizados e um workflow de CI em `.github/workflows/ci.yml`. Esses artefatos tornam os requisitos, as regras de trabalho e as verificações técnicas mais explícitos.

## 4. Fluxo de desenvolvimento e governança

O processo esperado para cada mudança é:

1. Abrir ou identificar uma Issue com objetivo e critérios de aceite.
2. Consultar `docs/SPEC.md` e identificar os componentes afetados.
3. Criar uma branch específica para a tarefa, sem desenvolver diretamente na branch principal de integração.
4. Implementar a mudança mantendo o escopo da Issue.
5. Criar ou atualizar testes pertinentes.
6. Executar `ruff check .` e `python -m pytest -q` localmente.
7. Abrir um Pull Request que descreva a alteração e vincule a Issue correspondente.
8. Solicitar revisão de outro integrante; resolver comentários e registrar a aprovação.
9. Confirmar que as verificações automatizadas passaram e que os critérios de aceite foram atendidos.
10. Fazer o merge conforme as regras do repositório e verificar o resultado integrado.

O workflow [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) está configurado para rodar em `push` e `pull_request`, instalar as dependências com Python 3.12, executar Ruff e pytest e publicar o relatório de testes como artefato. O arquivo de configuração comprova que o pipeline foi definido; o resultado de uma execução específica deve ser comprovado pelo [histórico do GitHub Actions](https://github.com/gianluca-berria/CheckorKaput/actions).

### Critérios mínimos antes do merge

- A alteração está relacionada a uma Issue e atende aos critérios de aceite descritos.
- O código respeita a especificação e não introduz mudanças fora do escopo sem justificativa.
- Testes novos ou existentes cobrem o comportamento alterado e os casos de borda relevantes.
- `ruff check .` e `python -m pytest -q` passam no ambiente previsto pelo projeto, ou as falhas remanescentes estão explicadas e aceitas explicitamente.
- Nenhuma credencial ou segredo foi incluído no repositório.
- README, especificação e ADRs foram atualizados quando a mudança afeta seu conteúdo.
- O Pull Request foi revisado por outro integrante e os comentários pertinentes foram resolvidos.
- A CI do Pull Request passou antes do merge.

Esses critérios estão alinhados ao processo descrito em `AGENTS.md` e à configuração do workflow. A aprovação de uma revisão específica deve ser confirmada no próprio Pull Request.

## 5. Desafios técnicos e aprendizados

### Integração com serviços externos

O projeto depende do Supabase para a persistência principal da CLI e da API pública openFDA para consultas informativas. Essas dependências introduzem riscos de configuração, conectividade e indisponibilidade. Por isso, as variáveis de ambiente não devem ser versionadas, e as falhas dos serviços precisam ser tratadas sem expor segredos.

**Aprendizado:** separar a integração externa da lógica principal e testar respostas de sucesso, dados ausentes e erros ajuda a tornar o comportamento mais previsível.

### Testes e integração contínua

O projeto mantém testes para regras de negócio, fluxo da CLI, persistência e consulta à API, além de um workflow automatizado.

**Aprendizado:** os testes locais e a CI são verificações complementares. A existência dos arquivos de teste não substitui a consulta dos resultados reais de execução, e uma execução bem-sucedida deve ser registrada com seu link ou log.

### Documentação e rastreabilidade

As Issues definem demandas e critérios; a especificação descreve o comportamento esperado; os ADRs registram decisões técnicas; os testes verificam comportamentos; e os Pull Requests devem relacionar a implementação a esses registros.

**Aprendizado:** manter esses artefatos alinhados facilita a integração entre integrantes e reduz ambiguidades durante a revisão.

### Colaboração

O trabalho colaborativo exige divisão explícita das tarefas, comunicação sobre bloqueios e revisão antes da integração. A atribuição de uma Issue é um indício de responsabilidade, mas a participação efetiva deve ser demonstrada pelo histórico de commits, comentários e revisões.

## 6. Uso de IA e responsabilidade humana

O projeto identifica o ChatGPT como ferramenta auxiliar no `AGENTS.md`. A IA pode ajudar a interpretar requisitos, sugerir soluções, produzir rascunhos de documentação e testes e apontar inconsistências.

A responsabilidade final permanece com os integrantes da equipe. Antes de integrar qualquer conteúdo gerado ou sugerido pela IA, uma pessoa deve:

- comparar a proposta com `docs/SPEC.md` e o código existente;
- verificar se os exemplos e comandos são válidos;
- executar os testes e as verificações de qualidade aplicáveis;
- revisar segurança, dependências e tratamento de erros;
- decidir se a mudança atende aos critérios de aceite;
- aprovar ou solicitar alterações no Pull Request.

A utilização de IA não deve ser descrita como revisão humana, execução de testes ou aprovação de merge. Essas ações exigem evidências próprias no repositório.

## 7. Evidências verificáveis

- [Repositório CheckorKaput](https://github.com/gianluca-berria/CheckorKaput)
- [Issue #1 — integração com API pública](https://github.com/gianluca-berria/CheckorKaput/issues/1)
- [Issue #2 — item relacionado à conclusão da Issue #1](https://github.com/gianluca-berria/CheckorKaput/issues/2)
- [Issue #15 — test harness](https://github.com/gianluca-berria/CheckorKaput/issues/15)
- [Issue #17 — GitHub Actions / CI](https://github.com/gianluca-berria/CheckorKaput/issues/17)
- [Issue #19 — README e evidências da entrega](https://github.com/gianluca-berria/CheckorKaput/issues/19)
- [Issue #34 — experiência e governança](https://github.com/gianluca-berria/CheckorKaput/issues/34)
- [Execuções do GitHub Actions](https://github.com/gianluca-berria/CheckorKaput/actions)
- [Pull Requests do repositório](https://github.com/gianluca-berria/CheckorKaput/pulls)
- [Especificação técnica](SPEC.md)
- [Instruções para contribuição assistida por IA](../AGENTS.md)
- [ADR-001 — ambiente Docker](adr/ADR-001-ambiente-docker.md)
- [ADR-002 — test harness e CI](adr/ADR-002-test-harness-e-ci.md)

### Evidências ainda a confirmar

Na consulta pública usada para preparar este documento, não foi possível confirmar um Pull Request específico para a Issue #34 nem uma aprovação de revisão por pares para essa entrega. Antes de marcar a Issue como concluída, incluir o link do Pull Request real e identificar a revisão/aprovação de outro integrante.

Também é necessário anexar ou vincular uma execução bem-sucedida e recente da CI se a entrega exigir prova de que os testes passaram. Não usar uma saída de teste antiga como prova de uma execução atual.

## 8. Limitações do registro

Este documento não substitui o histórico completo do Git. Ele resume evidências públicas identificáveis, mas não atribui cada commit a uma pessoa nem presume reuniões, revisões ou aprovações que não estejam registradas. Se forem encontradas evidências adicionais no histórico de branches, commits, comentários ou Pull Requests, este relato deverá ser atualizado para refletir esses registros.

## 9. Revisão deste documento

Antes do merge, outro integrante deve revisar este documento e confirmar:

- se a divisão de responsabilidades corresponde ao trabalho real;
- se as iterações e os links estão corretos;
- se os critérios descritos correspondem ao processo realmente usado;
- se as ausências de evidência estão registradas com transparência;
- se o README aponta para este arquivo.

**Status:** rascunho para revisão da equipe. A conclusão da Issue depende da validação das evidências e da revisão por pares no GitHub.
