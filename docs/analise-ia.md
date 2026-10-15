# Análise comparativa e ético-técnica do uso de IA

## 1. Objetivo e método

Este documento analisa o uso de inteligência artificial no desenvolvimento
do CheckorKaput e compara ferramentas de apoio à programação.

O ChatGPT foi a única ferramenta de IA efetivamente utilizada pela equipe.
Claude Code, Codex CLI, Cursor e Antigravity foram avaliados documentalmente,
com base nas fontes oficiais relacionadas ao final.

Não foram realizados experimentos equivalentes entre as ferramentas.
Portanto, a comparação não estabelece um ranking de qualidade, velocidade
ou produtividade. As possibilidades de aplicação ao projeto são avaliações
da equipe, e não resultados medidos.

## 2. Matriz comparativa

| Ferramenta | Forma de trabalho | Pontos fortes | Limitações e cuidados | Aplicação ao SDD do CheckorKaput |
|---|---|---|---|---|
| ChatGPT — utilizado | Interação conversacional com análise de especificações, trechos de código e resultados fornecidos durante o trabalho. | Apoio à explicação de requisitos, planejamento, testes e documentação. | Contexto incompleto ou desatualizado pode produzir sugestões incorretas. A resposta precisa ser confrontada com os arquivos e resultados reais. | Foi utilizado para relacionar requisitos, propor alterações e interpretar validações. |
| Claude Code — avaliação documental [1] | Agente que pode ler arquivos, editar código e executar comandos no terminal e em outras interfaces. | Pode trabalhar em vários arquivos e consultar instruções do projeto. | O acesso operacional exige delimitação de permissões e revisão das alterações; execução automática não comprova correção. | Poderia consultar a especificação e executar mudanças e testes na mesma tarefa, sob revisão humana. |
| Codex CLI — avaliação documental [2] | Agente de programação executado pelo terminal, com acesso ao projeto conforme a configuração. | Aproxima análise, edição e execução de comandos do fluxo de desenvolvimento. | Os resultados dependem do contexto, das permissões e da validação; trabalhar no terminal não significa que todo processamento seja local. | Poderia apoiar tarefas delimitadas por issue e instruções de `AGENTS.md`, preservando branches e PRs. |
| Cursor — avaliação documental [3] | Editor com agente que utiliza ferramentas de desenvolvimento, incluindo edição e terminal. | Integra a assistência ao ambiente em que o código é inspecionado. | Comandos e mudanças precisam de revisão; os controles de segurança não eliminam falhas ou exposição de contexto. | Poderia apoiar a inspeção conjunta de implementação, testes e especificação. |
| Antigravity — avaliação documental [4] | Ambiente com agente e políticas configuráveis de execução de comandos e revisão. | Permite ajustar quando determinadas ações devem solicitar revisão. | Políticas permissivas ampliam o alcance de uma ação incorreta; solicitar aprovação não garante que o usuário perceba o risco. | Poderia apoiar tarefas com revisão dos resultados e permissões limitadas ao necessário. |

As capacidades documentadas não demonstram superioridade no CheckorKaput.
Uma comparação experimental futura exigiria a mesma tarefa, versão inicial,
critérios de aceite e ambiente para todas as ferramentas, registrando defeitos,
correções humanas e resultados dos testes.

## 3. Impacto observado no projeto

O ChatGPT auxiliou na interpretação da especificação, no planejamento de
alterações, na elaboração de testes e na documentação. O projeto registra
as regras dessa participação em `AGENTS.md`.

Um exemplo verificável é a issue #31 e a PR #36. A inspeção identificou
que a CLI anunciava remoção bem-sucedida mesmo quando a persistência
retornava uma lista vazia. A correção passou a conferir o resultado e
acrescentou tratamento para listas vazias e medicamentos inexistentes.

A suíte passou de 28 para 42 testes aprovados na validação local de
12/10/2026, com Ruff aprovado. A seção 14.7 de `docs/SPEC.md` registra
os comportamentos esclarecidos e os limites dos testes.

O benefício observado foi a ampliação dos cenários verificados e da
rastreabilidade entre requisito, correção e teste. O aumento da quantidade
de testes, isoladamente, não comprova aumento proporcional de qualidade.
Também não foi medido quanto tempo a IA economizou.

A existência de testes aprovados antes da descoberta do erro demonstra
que a suíte inicial não cobria todas as situações relevantes.

## 4. Alucinação, código inseguro e ações destrutivas

Um modelo pode inventar funções, interpretar incorretamente uma biblioteca
ou sugerir código plausível que descumpra uma regra de negócio. Também
pode gerar testes que apenas reproduzam a implementação, sem verificar
o comportamento realmente esperado.

No CheckorKaput, as sugestões devem ser confrontadas com `docs/SPEC.md`.
Testes não devem ser modificados apenas para acomodar um defeito.
É necessário conferir mensagens, efeitos no banco e casos de borda.

Com acesso a ferramentas, uma sugestão incorreta pode resultar em exclusão
de arquivos, perda de alterações ou operações indevidas no banco. As medidas
de redução de risco incluem branches específicas, inspeção do diff,
execução em ambiente de teste e revisão dos comandos antes de aplicá-los.

Arquivos, páginas e respostas externas também podem conter instruções
maliciosas destinadas ao agente. Esse conteúdo deve ser tratado como dado,
sem autorização para alterar as regras do projeto ou expor segredos.

## 5. Privacidade e confidencialidade

Enviar contexto ao modelo pode expor código privado, credenciais, logs
e informações pessoais. Neste projeto, registros de medicamentos e tomadas
podem revelar informações sobre a saúde de uma pessoa.

Por isso, a equipe deve compartilhar apenas o contexto necessário, utilizar
dados fictícios nos exemplos e remover identificadores e segredos de logs
e capturas de tela. Credenciais do Supabase não devem ser inseridas em
prompts, código ou documentos públicos.

O projeto prevê credenciais por configuração externa e testes com o cliente
do Supabase simulado. Isso reduz a necessidade de compartilhar acesso real,
mas não comprova a segurança das políticas do banco remoto.

Arquivos ignorados pelo Git ainda podem ser lidos ou enviados por outras
ferramentas. Antes de conectar um agente, é necessário verificar permissões,
tratamento de dados e configurações aplicáveis ao serviço utilizado.

## 6. Propriedade intelectual e direitos autorais

Código sugerido por IA não deve ser presumido original ou livre de
obrigações. A revisão deve considerar a procedência de trechos incorporados,
licenças de dependências e eventuais exigências de atribuição.

Os termos da OpenAI tratam dos direitos entre usuário e fornecedor sobre
entradas e saídas, mas também alertam que resultados podem não ser exclusivos
[5]. Isso não constitui garantia de ausência de direitos de terceiros.

Como referência internacional, o U.S. Copyright Office diferencia conteúdo
gerado por IA de contribuições humanas para a proteção autoral nos Estados
Unidos [6]. Essa orientação não resolve automaticamente a situação jurídica
de um projeto brasileiro.

No CheckorKaput, a conduta proposta é manter rastreabilidade das contribuições,
verificar licenças de material externo e declarar o auxílio da IA.
Não foi realizada auditoria jurídica ou de similaridade de todo o código.

## 7. Revisão e homologação humana no SDD

Conforme `AGENTS.md`, as decisões finais permanecem com a equipe.
O fluxo exige consultar a especificação, delimitar a tarefa, implementar,
executar testes e revisar as alterações antes da integração.

A homologação deve conferir os critérios de aceite e os fluxos reais,
além da aprovação do pytest e do Ruff. Os testes com serviços simulados
não comprovam disponibilidade, permissões ou integridade do Supabase real.

O integrante responsável pela revisão deve examinar o diff, a consistência
com os requisitos e as evidências do commit avaliado. A revisão por outro
modelo pode auxiliar, mas não substitui a responsabilidade humana.

A IA oferece apoio ao desenvolvimento; aceitar alterações sem compreendê-las
transfere erros para o projeto e enfraquece o aprendizado da equipe.

## 8. Evidências do projeto

- [Issue #31 — correções da CLI](https://github.com/gianluca-berria/CheckorKaput/issues/31)
- [PR #36 — implementação e testes](https://github.com/gianluca-berria/CheckorKaput/pull/36)
- [Especificação e refinamentos](SPEC.md)
- [Regras de atuação da IA](../AGENTS.md)

## 9. Fontes oficiais

[1] Anthropic. Claude Code: visão geral.
https://code.claude.com/docs/en/overview

[2] OpenAI. Codex: repositório oficial e documentação do agente.
https://github.com/openai/codex

[3] Cursor. Agent Security.
https://cursor.com/docs/agent/security

[4] Google. Antigravity: Agent settings.
https://antigravity.google/docs/agent-settings

[5] OpenAI. Terms of Use.
https://openai.com/policies/row-terms-of-use/

[6] U.S. Copyright Office. Copyrightability of AI-generated outputs.
https://www.copyright.gov/newsnet/2025/1060.html

As características das ferramentas e seus termos podem mudar. A comparação
representa a documentação consultada para esta análise, sem testes práticos
das quatro ferramentas comparadas.

## 10. Declaração de uso de IA

Este documento foi elaborado com auxílio do ChatGPT na pesquisa de fontes,
organização da comparação e redação. Sua revisão e homologação cabem aos
integrantes da equipe antes da integração ao repositório.
