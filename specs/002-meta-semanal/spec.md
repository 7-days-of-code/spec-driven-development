# Feature Specification: Meta Semanal

**Feature Branch**: `002-meta-semanal`

**Created**: 2026-11-06

**Status**: Draft

**Input**: User description: "Escreva em português do Brasil. Nova funcionalidade do Hábito Certo: meta semanal. A pessoa pode definir, para cada hábito, quantos dias por semana quer cumpri-lo, de 1 a 7. A lista mostra, para cada hábito com meta, quantos dias ele foi marcado na semana atual e se a meta da semana foi atingida. A semana vai de segunda a domingo, pela data local do computador. Hábitos sem meta continuam funcionando como antes."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Definir uma meta semanal por hábito (Priority: P1)

A pessoa define para um hábito uma meta de cumprimento semanal entre 1 e 7 dias, podendo alterar ou remover essa meta posteriormente.

**Why this priority**: A meta personalizada expressa a frequência que a pessoa deseja alcançar em cada hábito.

**Independent Test**: Definir metas diferentes para dois hábitos e confirmar que cada uma fica associada somente ao hábito escolhido; alterar e remover uma delas.

**Acceptance Scenarios**:

1. **Dado** um hábito sem meta semanal, **Quando** a pessoa define uma meta de 3 dias, **Então** o hábito passa a ter uma meta de 3 dias por semana.
2. **Dado** um hábito com uma meta semanal, **Quando** a pessoa escolhe outra quantidade entre 1 e 7, **Então** a nova quantidade substitui a anterior.
3. **Dado** um hábito, **Quando** a pessoa tenta definir uma meta menor que 1 ou maior que 7, **Então** a meta inválida não é salva e a pessoa recebe uma orientação sobre o intervalo permitido.
4. **Dado** um hábito com meta semanal, **Quando** a pessoa remove a meta, **Então** o hábito volta a funcionar sem meta semanal.
5. **Dado** um hábito com meta semanal, **Quando** a pessoa fecha e abre novamente o aplicativo, **Então** a meta continua definida para esse hábito.
6. **Dado** um hábito com marcações e meta semanal, **Quando** a pessoa altera ou remove a meta, **Então** as marcações e a sequência diária permanecem inalteradas.

---

### User Story 2 - Acompanhar o progresso da meta na semana atual (Priority: P1)

A pessoa consulta a lista de hábitos e vê, em cada hábito com meta, quantos dias foi marcado na semana atual e se atingiu a meta.

**Why this priority**: A comparação entre o progresso e a meta permite à pessoa entender rapidamente se está no ritmo desejado.

**Independent Test**: Definir uma meta, marcar o hábito em dias distintos da semana e confirmar a contagem e o estado de atingimento exibidos.

**Acceptance Scenarios**:

1. **Dado** um hábito com meta de 3 dias e duas marcações em dias distintos de segunda a domingo da semana atual, **Quando** a pessoa consulta a lista, **Então** vê 2 dias marcados e a meta ainda não atingida.
2. **Dado** um hábito com meta de 3 dias e pelo menos três marcações em dias distintos da semana atual, **Quando** a pessoa consulta a lista, **Então** vê a contagem semanal e que a meta foi atingida.
3. **Dado** que um hábito foi marcado mais de uma vez na mesma data local, **Quando** a pessoa consulta seu progresso semanal, **Então** essa data conta uma única vez.
4. **Dado** um hábito com marcações em datas anteriores à segunda-feira da semana atual, **Quando** a pessoa consulta a lista nesta semana, **Então** essas marcações não entram na contagem semanal atual.
5. **Dado** que a data local do computador passa de domingo para segunda-feira, **Quando** a pessoa consulta a lista na nova semana, **Então** o progresso exibido considera somente as marcações da nova semana.

---

### User Story 3 - Continuar usando hábitos sem meta (Priority: P1)

A pessoa continua cadastrando, marcando e consultando hábitos sem meta semanal sem mudança no comportamento existente.

**Why this priority**: A meta semanal é opcional e não deve interromper o acompanhamento atual de quem não deseja definir uma meta.

**Independent Test**: Consultar e marcar um hábito sem meta e confirmar que o fluxo e as informações existentes continuam disponíveis, sem indicador de progresso semanal de meta.

**Acceptance Scenarios**:

1. **Dado** um hábito sem meta semanal, **Quando** a pessoa consulta a lista, **Então** o hábito continua sendo exibido com as informações existentes e sem estado de meta semanal.
2. **Dado** um hábito sem meta semanal, **Quando** a pessoa o marca como cumprido, **Então** a marcação e a sequência diária continuam funcionando como antes.
3. **Dado** que a pessoa usa o aplicativo com metas e marcações, **Quando** consulta ou atualiza seus hábitos, **Então** esses dados permanecem no computador e não são enviados nem sincronizados com serviços externos.

### Edge Cases

- Uma meta de 1 dia é atingida após uma marcação em qualquer dia da semana atual.
- Uma meta de 7 dias só é atingida quando cada um dos sete dias da semana atual tiver ao menos uma marcação.
- Marcações repetidas do mesmo hábito na mesma data local contam como um único dia.
- Marcações de domingo pertencem à semana que termina nesse domingo; marcações de segunda-feira pertencem à semana que começa nesse dia.
- Uma alteração ou remoção de meta não altera as marcações nem a sequência diária do hábito.
- Hábitos existentes que ainda não tenham uma meta permanecem sem meta até que a pessoa escolha defini-la.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A pessoa MUST conseguir definir separadamente para cada hábito uma meta de 1 a 7 dias por semana.
- **FR-002**: O sistema MUST rejeitar uma meta inferior a 1 ou superior a 7 e MUST informar à pessoa o intervalo permitido.
- **FR-003**: A pessoa MUST conseguir alterar ou remover a meta semanal de um hábito.
- **FR-004**: Para cada hábito com meta, o sistema MUST exibir na lista a quantidade de datas distintas em que o hábito foi marcado na semana atual e indicar se a meta foi atingida.
- **FR-005**: O sistema MUST considerar uma meta atingida quando a quantidade de dias distintos marcados na semana atual for igual ou superior à meta definida.
- **FR-006**: O sistema MUST considerar a semana atual como o período de segunda-feira a domingo, inclusive, determinado pela data local informada pelo computador da pessoa.
- **FR-007**: O sistema MUST contar no máximo uma marcação por hábito em cada data local ao calcular o progresso semanal.
- **FR-008**: O progresso semanal MUST incluir apenas marcações cujas datas locais estejam na semana atual, sem incluir marcações da semana anterior ou da próxima.
- **FR-009**: Hábitos sem meta semanal MUST continuar funcionando e sendo exibidos conforme o comportamento existente, sem exigir definição de meta.
- **FR-010**: Alterar ou remover uma meta semanal MUST NOT alterar as marcações ou a sequência diária do hábito.
- **FR-011**: As metas semanais MUST permanecer salvas depois que o aplicativo for fechado e aberto novamente.
- **FR-012**: As metas e marcações MUST permanecer armazenadas no computador da pessoa, sem envio ou sincronização com serviços externos.

### Key Entities *(include if feature involves data)*

- **Hábito**: Atividade cadastrada pela pessoa, com uma meta semanal opcional de 1 a 7 dias.
- **Marcação diária**: Registro de cumprimento de um hábito associado a uma data local; no máximo uma marcação por hábito e data conta para o progresso semanal.
- **Progresso semanal**: Quantidade de datas distintas da semana atual em que o hábito foi marcado e indicação de meta atingida ou ainda não atingida.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Em testes de aceitação, 100% das metas válidas de 1 a 7 dias podem ser definidas para um hábito, e valores fora do intervalo são rejeitados com orientação clara.
- **SC-002**: Em testes com marcações conhecidas de segunda a domingo, a contagem semanal exibida corresponde corretamente ao número de dias distintos marcados em 100% dos casos.
- **SC-003**: Em todos os testes de aceitação, a lista identifica corretamente se cada hábito com meta atingiu ou não a meta semanal.
- **SC-004**: Em testes de regressão, 100% dos fluxos existentes de hábitos sem meta continuam disponíveis sem exigir uma meta semanal.

## Assumptions

- Hábitos existentes começam sem meta semanal, preservando o comportamento anterior.
- A pessoa pode remover uma meta depois de defini-la; remover a meta não apaga o hábito nem seu histórico.
- As marcações são associadas à data local do computador, e a semana atual é calculada a partir dessa data, sem conversão de fuso horário.
- O progresso exibido é derivado das marcações existentes da semana atual; atingir a meta não impede marcações adicionais.
- Metas semanais e marcações ficam somente no computador da pessoa, conforme as regras de privacidade do projeto.
