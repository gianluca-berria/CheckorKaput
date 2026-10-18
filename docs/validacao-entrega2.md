# Validação da Entrega 2 — CheckorKaput

## 1. Identificação

- Issue: #35.
- Responsável: Gianluca Berria.
- Data da execução: 17/10/2026.
- Commit-base validado: aff64cc70a5afcd3d149bb490995e628564495fd.
- Branch: test/issue-35-validacao-final.
- Ambiente: Fedora e Docker, com imagem baseada em python:3.12-slim.

O commit-base identifica o código executado. Esta alteração acrescenta
documentação e evidências, sem modificar a implementação.

## 2. Resultados

| Verificação | Resultado |
|---|---|
| Build Docker | Aprovado |
| pytest | 42 testes aprovados em 0,70 s |
| Aprovação da suíte executada | 100% |
| Ruff | All checks passed! |
| CLI | Menu apresentado e encerramento pela opção 6 |
| Streamlit health check | Resposta ok observada |
| Consulta por acetaminophen | Informações apresentadas |
| Consulta por zzzzcheckorkaput123456 | Ausência de resultado informada |
| Campo vazio na consulta web | Validação sem interromper a aplicação |

As três consultas web foram verificadas manualmente e confirmadas pelo
responsável. Não representam testes automatizados da interface.

## 3. Rastreabilidade dos requisitos

| Requisito | Cenários verificados | Limites |
|---|---|---|
| RF-01 — Cadastro | Cadastro válido, nome vazio, horários ausentes, em branco ou inválidos; integração CLI/persistência | Supabase simulado |
| RF-02 — Listagem | Persistência com registros; CLI com registros e lista vazia | Supabase simulado |
| RF-03 — Tomada | Fluxo válido, ID vazio ou inexistente, inserção sem retorno e medicamento ausente após listagem | Integridade do banco real não verificada |
| RF-04 — Remoção | Fluxo válido, ID inexistente, lista vazia e remoção sem retorno | Supabase simulado |
| RF-05 — Histórico | Retorno do histórico na persistência | Histórico vazio e apresentação pela CLI sem teste específico identificado |
| RF-06 — Consulta externa | Resposta simulada, parâmetros, ausência de resultados e HTTP 404; consulta vazia manual | Outros erros HTTP e timeout sem teste específico identificado |
| RF-07 — Informações externas | Extração de dados simulados e consulta manual na interface | Campos ausentes e aviso informativo sem teste específico identificado |

Os testes de src/reminder.py cobrem componentes legados e não substituem
os testes dos fluxos atuais com Supabase.

Esta tabela relaciona os cenários identificados aos requisitos. Não constitui
medição de cobertura de linhas nem comprovação de cobertura integral.

## 4. Execução

A imagem foi construída com docker build -t checkorkaput .

Dentro da imagem foram executados:

- python -m pytest -q --junitxml=/evidencias/test-results.xml
  -o cache_dir=/tmp/pytest-cache;
- ruff check .;
- python -m pytest --collect-only -q;
- python -m src.main, recebendo a opção 6 pela entrada padrão;
- streamlit run streamlit_app.py --server.address=0.0.0.0.

O relatório JUnit foi preservado por montagem de diretório.
O Streamlit foi publicado em 127.0.0.1:8502 e sua rota
/_stcore/health foi consultada com curl.

## 5. Integração contínua

O GitHub Actions apresentou conclusão success para o commit-base aff64cc:

[Execução do CI](https://github.com/gianluca-berria/CheckorKaput/actions/runs/39048456674)

O resultado corresponde ao commit indicado. A execução do CI da PR deste
relatório também deverá ser conferida antes do merge.

## 6. Evidências preservadas

Diretório: [evidencias/issue-35/](evidencias/issue-35/).

- build.log: construção da imagem.
- pytest.log: resultado dos 42 testes.
- test-results.xml: relatório JUnit.
- ruff.log: análise estática.
- cli.log: abertura e encerramento.
- cenarios.txt: relação dos testes coletados.
- web-manual.txt: resultados confirmados das consultas e do health check.

O registro completo do ambiente permanece na pasta local de evidências.
Credenciais do Supabase não foram necessárias para estas verificações.

## 7. Limites e conclusão

Os 42 testes executados passaram. Esse resultado não garante ausência de
defeitos nem cobertura completa dos requisitos.

As operações da CLI contra o Supabase real não foram executadas nesta rodada.
Não foram comprovadas a configuração remota, as políticas de acesso ou as
restrições de integridade do banco.

Também não foram avaliados carga, concorrência, indisponibilidade real dos
serviços ou segurança por auditoria especializada. As lacunas de cenários
permanecem explicitamente registradas na tabela de requisitos.

A validação comprova o build, a aprovação da suíte, o lint, a abertura da CLI
e os cenários web descritos. A homologação humana e a revisão da PR são
necessárias antes da integração.
