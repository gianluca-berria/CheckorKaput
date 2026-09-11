# AGENTS.md

## 1. Agente utilizado

O projeto CheckorKaput utiliza o ChatGPT como agente de IA auxiliar durante o processo de desenvolvimento.

O agente atua como ferramenta de apoio para análise da especificação, planejamento de alterações, geração e revisão de código, criação de testes e documentação.

As decisões finais sobre alterações no projeto permanecem sob responsabilidade dos integrantes da equipe.

## 2. Fonte principal de contexto

Antes de propor ou implementar alterações funcionais, o agente deve consultar:

- `docs/SPEC.md`

A especificação técnica é a principal fonte de verdade para requisitos funcionais, requisitos não funcionais, regras de negócio, contratos e responsabilidades dos componentes.

Caso haja divergência entre a implementação existente e a especificação, a divergência deverá ser identificada explicitamente antes de qualquer alteração.

## 3. Fluxo de desenvolvimento

Ao trabalhar em uma tarefa, o agente deverá seguir o seguinte fluxo:

1. identificar a Issue relacionada;
2. consultar `docs/SPEC.md`;
3. identificar os requisitos e regras afetados;
4. analisar o código existente antes de propor alterações;
5. implementar apenas o necessário para atender à especificação;
6. criar ou atualizar testes relacionados;
7. executar a suíte de testes;
8. verificar se código, testes e especificação permanecem consistentes;
9. registrar eventual necessidade de refinamento da especificação.

## 4. Regras para alteração de código

O agente deverá:

- preservar a arquitetura existente quando não houver motivo documentado para alterá-la;
- evitar alterações fora do escopo da Issue;
- manter compatibilidade com Python 3.12;
- respeitar as responsabilidades dos componentes definidas em `docs/SPEC.md`;
- evitar adicionar dependências sem necessidade justificada;
- não inserir credenciais, tokens ou chaves diretamente no código-fonte;
- comunicar quando uma alteração proposta exigir decisão arquitetural.

## 5. Regras para testes

O agente deverá:

- criar ou atualizar testes quando uma alteração modificar comportamento do sistema;
- relacionar testes, quando possível, aos requisitos ou regras definidos em `docs/SPEC.md`;
- incluir cenários principais e casos de borda relevantes;
- manter os testes independentes entre si;
- evitar dependência imprevisível de serviços externos;
- utilizar mocks ou mecanismos equivalentes quando necessário para isolar serviços externos.

O agente não deverá alterar um teste apenas para fazê-lo passar quando a falha indicar um defeito real na implementação.

Nesse caso, a implementação ou a especificação deverá ser analisada.

## 6. Alterações na especificação

A especificação não deverá ser modificada apenas para justificar posteriormente um comportamento já implementado.

Quando testes, revisão de código ou decisões da equipe demonstrarem necessidade de mudança nos requisitos, o refinamento deverá ser realizado explicitamente e documentado.

## 7. Componentes legados

Os componentes:

- `src/reminder.py`;
- `src/storage.py`;
- `data/meds.json`;

são considerados parte de uma implementação anterior do projeto.

Novas funcionalidades não deverão depender desses componentes sem decisão arquitetural explícita.

## 8. Restrições

O agente não deverá:

- implementar funcionalidades sem relação com a Issue em execução;
- ignorar requisitos definidos em `docs/SPEC.md`;
- remover validações somente para fazer testes passarem;
- modificar testes apenas para acomodar comportamento incorreto;
- armazenar segredos no repositório;
- realizar grandes refatorações sem justificativa;
- apresentar como concluída uma tarefa cujos testes estejam falhando.

## 9. Revisão humana

Todo conteúdo produzido com auxílio do agente deverá ser revisado por um integrante da equipe antes de ser integrado às branches principais do projeto.

Pull Requests deverão seguir as regras de revisão definidas pela governança do repositório.

## 10. Rastreabilidade

Ao propor alterações de comportamento, o agente deverá identificar, quando aplicável, os requisitos funcionais, requisitos não funcionais e regras de negócio relacionados em `docs/SPEC.md`.

Alterações que modifiquem comportamento previsto deverão manter consistência entre especificação, implementação e testes.
