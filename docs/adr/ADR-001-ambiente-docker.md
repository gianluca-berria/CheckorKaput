# ADR-001 — Ambiente reproduzível com Docker

* **Status:** Aceita
* **Data:** 2026-09-13

## Contexto

O CheckorKaput precisava ser executado e testado independentemente da versão do Python, das dependências e da configuração existente na máquina de cada integrante.

A especificação definiu Python 3.12 como plataforma e Docker como mecanismo de padronização do ambiente.

## Decisão

Adotar uma imagem baseada em `python:3.12-slim`, construída pelo `Dockerfile` do repositório.

A imagem instala as dependências declaradas no `requirements.txt` e permite executar:

* a interface CLI;
* a interface Streamlit;
* a suíte com pytest;
* a verificação de qualidade com Ruff.

Credenciais do Supabase são fornecidas em tempo de execução. Arquivos `.env`, segredos do Streamlit, ambientes virtuais e caches são excluídos da imagem pelo `.dockerignore`.

## Alternativas consideradas

### Ambiente virtual local

É mais leve, mas continua dependente da versão do Python e da configuração da máquina.

### Docker Compose

Seria apropriado para vários serviços locais, porém o projeto utiliza Supabase e openFDA externamente e não necessita orquestrar contêineres adicionais.

### Dev Container

Facilitaria a integração com editores compatíveis, mas acrescentaria configuração além do necessário para esta entrega.

## Consequências

* ambiente consistente entre os integrantes e o CI;
* dependências locais deixam de interferir nos testes;
* necessidade de Docker para utilizar o ambiente padronizado;
* maior tempo e espaço para construir a imagem;
* a tag `python:3.12-slim` pode receber atualizações, portanto a construção não é necessariamente idêntica byte a byte.

## Validação

A decisão foi implementada e aprovada na [PR #25](https://github.com/gianluca-berria/CheckorKaput/pull/25).

Foram validados a construção da imagem, a execução da CLI, a saúde da interface Streamlit, o pytest e o Ruff.

## Relação com a especificação

Atende aos requisitos RNF-01, RNF-04 e RNF-05.
