# Validação Final — Entrega 3

## 1. Identificação

- **Projeto:** CheckorKaput
- **Versão de lançamento:** 2.0.0
- **Branch de validação:** develop
- **Commit validado:** `ce6cd079cfb6aa58a37b6bc7c54e2ac24b91e91e`
- **Data da validação:** 31/10/2026
- **Ambiente:** Fedora 44, Docker 29.9.2 e Python 3.12.16 (imagem `python:3.12-slim`).

## 2. Testes automatizados

A suíte completa foi executada no ambiente Docker, com os seguintes resultados:

- **Pytest:** 41 testes aprovados.
- **Ruff:** todas as verificações aprovadas.
- **Cobertura:** 81% no total.

Comandos utilizados:

```bash
sudo docker run --rm checkorkaput:homologacao python -m pytest -v

sudo docker run --rm checkorkaput:homologacao ruff check .

sudo docker run --rm checkorkaput:homologacao python -m pytest --cov --cov-report=term-missing
```

## 3. Validação de execução

### 3.1. Docker

A imagem Docker foi construída com sucesso:

```bash
sudo docker build -t checkorkaput:homologacao .
```

A execução da aplicação CLI foi confirmada, com apresentação do menu e encerramento normal.

### 3.2. Interface Web

A aplicação Streamlit foi iniciada em contêiner Docker e acessada pelo navegador, confirmando a disponibilidade da interface.

### 3.3. API externa

A consulta à API pública openFDA foi testada pela interface web, com retorno de resultados para o medicamento pesquisado.

### 3.4. Supabase

A comunicação com o Supabase havia sido testada previamente e confirmada em funcionamento normal. Os testes automatizados da camada de persistência também foram aprovados.

## 4. Integração contínua

A execução da CI no commit validado foi concluída com sucesso.

- **Workflow:** Lint e testes — Python 3.12
- **Resultado:** aprovado.
- **Execução:** [GitHub Actions](https://github.com/gianluca-berria/CheckorKaput/actions/runs/41092552114)

## 5. Resultado da homologação

Os testes automatizados, as verificações estáticas e os fluxos de execução da aplicação foram concluídos com resultados satisfatórios.

A integração com o Supabase foi confirmada em teste anterior. A execução desta homologação não realizou uma nova validação independente dessa comunicação.

A validação foi realizada na branch `develop`. A integração final na `main` e a publicação da release estável `v2.0.0` deverão ocorrer após a aprovação e o merge da PR de entrega final.

## 6. Conclusão

O projeto apresenta condições satisfatórias para a conclusão da Entrega 3 e publicação da versão estável 2.0.0, condicionadas à integração final na branch principal e à publicação da respectiva release.
