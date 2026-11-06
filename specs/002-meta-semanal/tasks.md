---
description: "Tarefas para implementar metas semanais por hábito"
---

# Tarefas: Meta Semanal

**Entrada**: Documentos de design em `/specs/002-meta-semanal/`

**Pré-requisitos**: `plan.md`, `spec.md`, `research.md`, `data-model.md` e `contracts/web.md`

**Organização**: Tarefas agrupadas por história de usuário para permitir implementação e validação incremental.

**Formato**: `- [ ] [ID] [P?] [Story?] Descrição com caminho do arquivo`

## Fase 1: Preparação

**Objetivo**: Reutilizar o projeto Flask existente, sem criar estrutura ou dependências adicionais.

O projeto já contém `app.py`, `schema.sql`, `templates/index.html`, `tests/test_app.py` e as dependências Flask/pytest em `requirements.txt`; não há tarefas de inicialização necessárias.

---

## Fase 2: Fundação — compatibilidade do banco

**Objetivo**: Preparar o SQLite para armazenar metas sem apagar ou recriar dados existentes. Esta fase bloqueia as histórias de usuário.

- [X] T001 [P] Adicionar `weekly_goal INTEGER NULL CHECK (weekly_goal IS NULL OR weekly_goal BETWEEN 1 AND 7)` à tabela `habit` criada em `schema.sql`; a meta deve ser nula ou, quando presente, um inteiro entre 1 e 7 inclusive.
- [X] T002 [P] Atualizar `init_db()` em `app.py` para consultar `PRAGMA table_info(habit)` após executar `schema.sql` e executar `ALTER TABLE habit ADD COLUMN weekly_goal INTEGER CHECK (weekly_goal IS NULL OR weekly_goal BETWEEN 1 AND 7)` somente se a coluna não existir; não apagar/recriar tabelas nem alterar hábitos ou marcações existentes.

**Checkpoint**: Bancos novos já contêm a coluna e bancos existentes a recebem uma única vez, com hábitos e marcações preservados.

---

## Fase 3: História de Usuário 1 — Definir uma meta semanal por hábito (Prioridade: P1)

**Objetivo**: Permitir definir, alterar e remover uma meta de 1 a 7 dias para cada hábito, com persistência local.

**Teste independente**: Configurar metas diferentes para dois hábitos, alterar e remover uma delas, rejeitar valores inválidos, reiniciar a aplicação e confirmar que a outra meta e as marcações permanecem inalteradas.

### Testes da História de Usuário 1

- [X] T003 [US1] Adicionar testes em `tests/test_app.py` para definir metas válidas de 1 a 7 por hábito, alterar/remover meta com valor vazio, rejeitar valor inválido com orientação de intervalo, persistir a meta após recriar o app e preservar marcações/sequências ao alterar ou remover.

### Implementação da História de Usuário 1

- [X] T004 [P] [US1] Implementar em `app.py` a rota `POST /habits/<int:habit_id>/weekly-goal`: aceitar `days` vazio para remover a meta ou inteiro de 1 a 7 para definir/alterar, rejeitar demais valores sem salvar, mostrar mensagem sobre o intervalo permitido e retornar 404 para hábito inexistente.
- [X] T005 [P] [US1] Adicionar em `templates/index.html`, para cada hábito, um formulário POST para `/habits/<id>/weekly-goal` com campo `days` limitado a 1–7, valor atual quando houver meta e opção vazia para removê-la.

**Checkpoint**: A pessoa consegue gerenciar metas por hábito; a persistência não altera o histórico de marcações.

---

## Fase 4: História de Usuário 2 — Acompanhar o progresso da semana atual (Prioridade: P1)

**Objetivo**: Exibir, para hábitos com meta, a contagem de dias distintos marcados de segunda a domingo da semana local atual e se a meta foi atingida.

**Teste independente**: Marcar um hábito em dias distintos da semana, consultar a página e conferir contagem e estado da meta; confirmar os limites da semana e a transição de domingo para segunda-feira.

### Testes da História de Usuário 2

- [ ] T006 [US2] Adicionar testes em `tests/test_app.py` para contagens abaixo/na meta, marcações de segunda e domingo, exclusão de datas da semana anterior/próxima, reinício do progresso na segunda-feira seguinte e contagem única após tentativas repetidas na mesma data.

### Implementação da História de Usuário 2

- [ ] T007 [P] [US2] Atualizar a rota `index()` em `app.py` para calcular o início da semana local com `date.today()` e contar com `COUNT(DISTINCT completed_on)` as datas de `habit_checkin` entre segunda e domingo inclusive, somente para hábitos com meta; expor a contagem e o estado `dias_marcados >= weekly_goal` ao template sem alterar `get_habit_sequence()`.
- [ ] T008 [P] [US2] Atualizar `templates/index.html` para exibir contagem e estado de atingimento somente quando o hábito possuir meta semanal, mantendo visíveis a sequência e os controles de marcação já existentes.

**Checkpoint**: O progresso considera somente a semana local atual e não interfere na sequência diária.

---

## Fase 5: História de Usuário 3 — Continuar usando hábitos sem meta (Prioridade: P1)

**Objetivo**: Preservar os fluxos existentes e garantir que hábitos legados e hábitos sem meta continuem sendo cadastrados, marcados e exibidos sem indicador de progresso semanal.

**Teste independente**: Inicializar a aplicação com um banco anterior à coluna `weekly_goal`, confirmar preservação dos hábitos e marcações, consultar a lista e marcar um hábito sem meta; confirmar sequência existente e ausência do estado de meta.

### Testes da História de Usuário 3

- [ ] T009 [US3] Adicionar testes de regressão em `tests/test_app.py` criando um banco legado sem `weekly_goal` com hábito e marcação existentes; após `create_app()`, verificar que ambos foram preservados, que o hábito permanece sem meta e que consulta/marcação continuam exibindo a sequência sem estado semanal.

**Checkpoint**: Bancos legados e hábitos sem meta continuam compatíveis com os fluxos anteriores.

---

## Fase 6: Acabamento e validação integrada

**Objetivo**: Verificar a integração de todas as histórias e o roteiro de validação da feature.

- [ ] T010 Executar `python -m pytest -q` na raiz do repositório e seguir os cenários de `specs/002-meta-semanal/quickstart.md`; corrigir falhas relacionadas à feature em `app.py`, `schema.sql`, `templates/index.html` ou `tests/test_app.py`.

---

## Dependências e ordem de execução

### Dependências entre fases

- **Preparação (Fase 1)**: já atendida pela estrutura e dependências existentes.
- **Fundação (Fase 2)**: concluir antes de qualquer história de usuário.
- **US1 (Fase 3)**: depende da Fundação e estabelece os formulários/rota de metas.
- **US2 (Fase 4)**: depende da Fundação e da US1 para consumir a meta persistida; evitar trabalho simultâneo em `app.py` e `templates/index.html`.
- **US3 (Fase 5)**: depende das fases anteriores para verificar regressão do fluxo completo e compatibilidade de bancos legados.
- **Acabamento (Fase 6)**: depende das histórias que serão entregues.

### Ordem das histórias

```text
Fundação -> US1 (P1) -> US2 (P1) -> US3 (P1) -> Acabamento
```

As histórias têm prioridade P1, mas são executadas em sequência porque a interface e a lógica compartilham `app.py` e `templates/index.html`, e a validação de US3 precisa cobrir a versão integrada sem meta.

### Oportunidades de paralelismo

- **Fundação**: T001 (`schema.sql`) e T002 (`app.py`) podem ser feitas em paralelo; ambas usam o nome de coluna definido no design.
- **US1**: após T003, T004 (`app.py`) e T005 (`templates/index.html`) podem ser implementadas em paralelo conforme o contrato `POST /habits/<habit_id>/weekly-goal`.
- **US2**: após T006, T007 (`app.py`) e T008 (`templates/index.html`) podem ser implementadas em paralelo usando os dados de progresso acordados no modelo.
- Tarefas de teste em `tests/test_app.py` devem ser feitas na fase da respectiva história para evitar alterações simultâneas no mesmo arquivo.

### Exemplo de execução paralela — US1

```text
Primeiro: T003 (testes de configuração, validação, remoção e persistência)
Depois, em paralelo:
  T004 — rota Flask em app.py
  T005 — formulário por hábito em templates/index.html
```

---

## Estratégia de implementação

### MVP primeiro

1. Concluir T001–T002 para preparar a coluna com migração aditiva e preservação do banco.
2. Concluir T003–T005 (US1) para oferecer metas configuráveis e persistentes.
3. Parar e validar independentemente a definição, alteração, remoção, rejeição de valores inválidos e preservação das marcações.

### Entrega incremental

1. Fundação + US1: metas podem ser gerenciadas por hábito.
2. US2: lista apresenta o progresso semanal e o atingimento da meta.
3. US3: regressão confirma compatibilidade com bancos existentes e hábitos sem meta.
4. Acabamento: executar toda a suíte pytest e os cenários de `quickstart.md`.

## Notas

- `[P]` indica tarefas em arquivos diferentes que podem ser executadas sem aguardar uma tarefa incompleta dependente.
- `[US1]`, `[US2]` e `[US3]` rastreiam as histórias correspondentes em `specs/002-meta-semanal/spec.md`.
- Nenhuma dependência ou serviço externo novo deve ser introduzido.
