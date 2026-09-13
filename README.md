Aplicação publicada: [https://checkorkaput-fw7oxgsm84l32czslsqjtk.streamlit.app/](https://checkorkaput-fw7oxgsm84l32czslsqjtk.streamlit.app/)

# CheckorKaput

Uma aplicação CLI desenvolvida para auxiliar usuários no controle de medicamentos, horários e registros de uso, reduzindo esquecimentos e promovendo maior segurança no tratamento.

---

## Problema

Muitas pessoas, especialmente idosos, pacientes em tratamento contínuo ou indivíduos com rotinas intensas, enfrentam dificuldades para lembrar de tomar seus medicamentos nos horários corretos.

O esquecimento ou uso incorreto pode causar:

* agravamento de condições de saúde
* falha em tratamentos
* riscos à vida em casos mais críticos

---

## Solução

O "CheckorKaput" oferece uma forma simples e prática de:

* registrar medicamentos
* definir horários de uso
* acompanhar quando foram tomados

Tudo isso por meio de uma interface de linha de comando (CLI), leve e acessível.

---

## Público-alvo

* idosos
* pacientes em tratamento contínuo
* pessoas com rotinas ocupadas
* cuidadores

---

## Funcionalidades

* ➕ Adicionar medicamentos com horários
* 📋 Listar medicamentos cadastrados
* ✅ Marcar medicamento como tomado
* 💾 Persistência de dados em arquivo JSON

---

## Tecnologias utilizadas

* Python 3.12
* pytest (testes automatizados)
* ruff (lint/análise estática)
* Git e GitHub
* GitHub Actions (CI)

---

## Instalação

Clone o repositório:

git clone [https://github.com/gianluca-berria/CheckorKaput.git](https://github.com/gianluca-berria/CheckorKaput.git)

cd CheckorKaput

Crie e ative o ambiente virtual:

python3 -m venv venv

source venv/bin/activate

---

## Execução

python src/main.py

---

## Testes

pytest

---

## Lint (qualidade de código)

ruff check .

---

## Integração Contínua (CI)

O projeto possui pipeline configurada no GitHub Actions que executa automaticamente:

* instalação de dependências
* verificação de lint
* execução dos testes

---

## Governança de Branches e Pull Requests

O projeto utiliza um fluxo de versionamento baseado em branches para organizar o desenvolvimento e manter a branch principal estável.

### Branch `main`

A branch `main` representa a versão estável do projeto.

As alterações não devem ser realizadas diretamente nessa branch. As mudanças devem ser incorporadas por meio de Pull Requests após revisão de outro integrante da equipe.

### Branch `develop`

A branch `develop` é utilizada como branch de integração do projeto.

As alterações desenvolvidas nas branches específicas das tarefas são integradas primeiro na `develop`, permitindo que as mudanças sejam revisadas e validadas antes de serem encaminhadas para a `main`.

### Branches específicas

Cada tarefa ou Issue deve ser desenvolvida em uma branch própria.

Exemplos:

* `12`
* `15`
* `19`

Essas branches devem conter somente as alterações relacionadas à tarefa correspondente.

### Fluxo de desenvolvimento

main
↑
│ Pull Request + revisão
│
develop
↑
│ Pull Request + revisão
│
branch específica da tarefa

O processo de desenvolvimento segue estas etapas:

1. Criar uma branch específica para a Issue ou tarefa.
2. Realizar as alterações nessa branch.
3. Executar os testes e verificações necessárias.
4. Enviar a branch para o GitHub.
5. Abrir um Pull Request para a branch `develop`.
6. Solicitar a revisão de outro integrante da equipe.
7. Após a aprovação, realizar a integração da alteração.
8. Quando as alterações estiverem estáveis, a `develop` poderá ser integrada à `main` por meio de Pull Request.

### Revisão dos Pull Requests

Os Pull Requests devem ser revisados por outro integrante da equipe antes da integração.

A revisão deve verificar:

* funcionamento da alteração
* qualidade do código
* testes
* possíveis problemas ou regressões
* atendimento aos requisitos da Issue

Sempre que possível, a branch `main` deve permanecer protegida contra commits diretos, priorizando o uso de Pull Requests e revisão por outro integrante.

---

## Versão

1.0.0

---

## Equipe

* Gianluca Berria
* Carlos
* Emmanuel Avelino

---

## Repositório

[https://github.com/gianluca-berria/CheckorKaput](https://github.com/gianluca-berria/CheckorKaput)
