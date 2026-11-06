---
description: "Tarefas para implementar hábitos e sequências diárias"
---

# Tasks: Hábitos e Sequências Diárias

**Entrada**: Documentos de design em `/specs/001-habitos-sequencia/`

**Pré-requisitos**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/web.md`, `quickstart.md`

**Testes**: Incluídos porque os critérios da especificação e o plano definem validação automatizada dos cenários.

**Organização**: Tarefas agrupadas por história de usuário em prioridade: P1, P1 e P2.

## Fase 1: Preparação

**Objetivo**: Configurar as dependências e os arquivos-base previstos no plano.

- [x] T001 [P] Declarar Flask e pytest como dependências em `requirements.txt`, mantendo compatibilidade com Python 3.11 ou superior
- [x] T002 [P] Ignorar `.venv/`, `__pycache__/`, `.pytest_cache/` e `instance/` em `.gitignore` para não versionar ambientes, caches e dados locais

## Fase 2: Fundação

**Objetivo**: Disponibilizar persistência local e infraestrutura Flask antes das histórias.

- [x] T003 [P] Criar `schema.sql` com as tabelas de hábitos e marcações: para `name`, aplicar a regra “Obrigatório; texto apresentado na interface, removendo espaços no início e no fim. Não pode ser vazio após `strip()`.”; para `name_key`, aplicar “Obrigatório e único; forma NFC de `name.strip()` convertida por `casefold()`. ”; para `habit_id`, aplicar “Obrigatório; chave estrangeira para `habit.id`. ”; para `completed_on`, aplicar “Obrigatório; data local em ISO 8601 (`YYYY-MM-DD`).”; impor unicidade em `(habit_id, completed_on)`
- [x] T004 [P] Criar a fábrica `create_app`, conexão SQLite por contexto de requisição, fechamento da conexão e inicialização do esquema em `app.py`; usar banco em `instance/` por padrão, permitir banco temporário pela configuração de testes e ativar chaves estrangeiras em cada conexão

**Ponto de verificação**: Aplicação e banco local podem ser inicializados; histórias podem começar.

## Fase 3: História de Usuário 1 — Cadastrar e consultar hábitos (Prioridade: P1)

**Objetivo**: Cadastrar hábitos com nomes válidos e consultar a lista, mostrando sequência 0 antes de qualquer marcação.

**Teste independente**: Com o cliente de teste do Flask, cadastrar um ou mais hábitos, consultar `GET /` e confirmar que a lista mostra cada nome com sequência 0; tentativas de nome vazio ou duplicado não criam registros e exibem orientação adequada.

### Testes da História de Usuário 1

- [ ] T005 [US1] Escrever em `tests/test_app.py` testes HTTP para lista vazia e lista de hábitos, cadastro com aparagem de espaços, rejeição de nome vazio/só espaços e rejeição de duplicatas ignorando caixa e equivalência Unicode NFC; usar banco temporário

### Implementação da História de Usuário 1

- [ ] T006 [US1] Implementar `POST /habits` em `app.py`: aparar o nome, calcular `name_key` com NFC e `casefold()`, usar consulta parametrizada, recusar chave duplicada e apresentar mensagens compreensíveis sem inserir dados inválidos
- [ ] T007 [US1] Implementar `GET /` em `app.py` e a página correspondente em `templates/index.html`, exibindo o formulário, mensagens, estado vazio e todos os hábitos com sequência inicial 0

**Ponto de verificação**: Fluxo de cadastro e consulta funciona isoladamente e seus testes passam.

## Fase 4: História de Usuário 2 — Marcar o hábito de hoje e acompanhar a sequência (Prioridade: P1)

**Objetivo**: Registrar no máximo uma marcação por hábito e data local, e apresentar a sequência consecutiva atual.

**Teste independente**: Preparar um hábito em banco temporário e controlar a data nos testes; verificar primeira marcação, repetição no mesmo dia, dias consecutivos, intervalo sem marcação, exibição de 0 após intervalo, reinício em 1 e data local armazenada em ISO 8601.

### Testes da História de Usuário 2

- [ ] T008 [US2] Acrescentar testes em `tests/test_app.py` para `POST /habits/<id>/check-ins`, controlando a data usada pela aplicação e cobrindo primeira marcação, repetição idempotente, dias consecutivos, lacuna, sequência 0 antes de remarcar e resposta 404 para hábito inexistente

### Implementação da História de Usuário 2

- [ ] T009 [US2] Implementar em `app.py` o cálculo da sequência a partir das datas registradas para o hábito: retornar 0 sem marcações ou se a última for anterior a ontem; nos demais casos, contar datas consecutivas para trás a partir da última marcação
- [ ] T010 [US2] Implementar `POST /habits/<habit_id>/check-ins` em `app.py`, associando `date.today()` ao hábito, usando inserção idempotente para não duplicar `(habit_id, completed_on)`, retornando 404 para hábito inexistente e redirecionando à lista
- [ ] T011 [US2] Atualizar `templates/index.html` para exibir a sequência atualizada e um formulário “Fiz hoje” por hábito, enviando POST ao endpoint correspondente sem aceitar data do navegador

**Ponto de verificação**: Marcações e sequências obedecem às regras de data local e repetição diária.

## Fase 5: História de Usuário 3 — Acompanhar vários hábitos (Prioridade: P2)

**Objetivo**: Manter históricos e sequências independentes para cada hábito da lista.

**Teste independente**: Cadastrar dois ou mais hábitos com históricos diferentes, marcar apenas um e confirmar em `GET /` que cada sequência corresponde exclusivamente às marcações daquele hábito.

### Testes da História de Usuário 3

- [ ] T012 [US3] Acrescentar a `tests/test_app.py` um cenário HTTP com pelo menos dois hábitos e históricos distintos; marcar um deles e afirmar que a sequência do outro permanece inalterada e que ambos continuam na lista

### Implementação da História de Usuário 3

- [ ] T013 [US3] Isolar em `app.py` a consulta do histórico e o cálculo da sequência por `habit_id`, garantindo que a montagem da lista não compartilhe marcações nem contadores entre hábitos

**Ponto de verificação**: Históricos independentes são demonstrados por testes com múltiplos hábitos.

## Fase 6: Acabamento e validação transversal

**Objetivo**: Validar a entrega integrada e manter as instruções de execução alinhadas ao projeto.

- [ ] T014 Executar `python -m pytest` e seguir a instalação e execução descritas em `specs/001-habitos-sequencia/quickstart.md`; corrigir divergências entre as instruções, `requirements.txt` e os caminhos locais de execução

## Dependências e ordem de execução

### Dependências entre fases

- Preparação (Fase 1) não depende de outras fases.
- Fundação (Fase 2) depende da Preparação e bloqueia todas as histórias.
- US1 (Fase 3) e US2 (Fase 4) são P1; US2 integra o formulário e a lista criados em US1, portanto a entrega completa segue US1 → US2.
- US3 (Fase 5, P2) verifica o isolamento dos dados já persistidos e apresentados pelas histórias anteriores; segue US1 → US2 → US3.
- Acabamento (Fase 6) depende das histórias incluídas na entrega.

### Oportunidades de paralelismo

- Fase 1: T001 e T002 podem ser executadas em paralelo, pois alteram arquivos diferentes.
- Fase 2: T003 e T004 podem ser preparadas em paralelo, pois alteram `schema.sql` e `app.py`; ambas devem estar concluídas antes das histórias.
- Dentro das histórias não há paralelismo seguro: os testes precedem a implementação e as tarefas de aplicação integram arquivos ou operações compartilhados.

### Exemplo de execução por história

- **US1**: após a Fundação, executar T005 primeiro; então T006 e T007 em sequência, verificando o ponto de verificação da fase.
- **US2**: após US1, executar T008 primeiro; então T009, T010 e T011 em sequência, verificando os limites de data e idempotência.
- **US3**: após US2, executar T012 primeiro; então T013 e confirmar o isolamento dos históricos.

## Estratégia de implementação

### MVP incremental

1. Concluir Preparação e Fundação.
2. Entregar US1 (P1) para cadastrar e consultar hábitos; validar o incremento de forma independente.
3. Entregar US2 (P1) para completar o fluxo central de marcação e sequências; validar os limites de data e repetição.
4. Entregar US3 (P2) e confirmar o isolamento de hábitos múltiplos.
5. Executar a validação integrada descrita no quickstart.

**Escopo MVP sugerido**: US1 como primeiro incremento demonstrável. Para atender ao objetivo principal do produto de acompanhar cumprimento diário, incluir US2 logo em seguida.
