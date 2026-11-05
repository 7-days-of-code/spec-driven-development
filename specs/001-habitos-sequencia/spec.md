# Feature Specification: Hábitos e Sequências Diárias

**Feature Branch**: `001-habitos-sequencia`

**Created**: 2026-11-05

**Status**: Draft

**Input**: User description: "Escreva em português do Brasil. O Hábito Certo é um app para quem quer criar hábitos. A pessoa cadastra hábitos pelo nome, marca \"fiz hoje\" em cada um e vê há quantos dias seguidos cumpriu cada hábito. Regras: um hábito marcado pela primeira vez tem sequência 1; marcar duas vezes no mesmo dia não muda a sequência; se a pessoa pulou um dia, a sequência volta a ser 1 na próxima marcação. A pessoa também pode ver a lista dos seus hábitos com a sequência de cada um."

## Clarifications

### Session 2026-11-05

- Q: Se a pessoa não marcou um hábito ontem, o que a lista deve mostrar hoje antes de ela marcar “Fiz hoje”? → A: Mostrar 0; ao marcar hoje, a sequência reinicia em 1.
- Q: A pessoa pode cadastrar dois hábitos com o mesmo nome escrito exatamente da mesma forma? → A: Não; nomes exatamente iguais não são permitidos.
- Q: “Leitura” e “leitura” devem ser tratados como o mesmo hábito? → A: Sim; a comparação ignora diferenças entre maiúsculas e minúsculas.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Cadastrar e consultar hábitos (Priority: P1)

A pessoa cria hábitos informando seus nomes e consulta uma lista com todos os hábitos cadastrados e a sequência de cada um.

**Why this priority**: Ter hábitos cadastrados e conseguir consultá-los é a base para acompanhar a rotina.

**Independent Test**: Cadastrar um ou mais hábitos e confirmar que todos aparecem na lista com sua sequência, inclusive com sequência 0 antes da primeira marcação.

**Acceptance Scenarios**:

1. **Given** que a pessoa ainda não cadastrou hábitos, **When** cadastra um hábito com um nome, **Then** o hábito aparece na lista com sequência 0.
2. **Given** que há hábitos cadastrados, **When** a pessoa consulta sua lista, **Then** vê todos eles e a sequência correspondente a cada hábito.
3. **Given** que a pessoa tenta cadastrar um nome vazio ou composto apenas por espaços, **When** confirma o cadastro, **Then** o hábito não é criado e ela recebe uma orientação para informar um nome.
4. **Given** que já existe um hábito com determinado nome, **When** a pessoa tenta cadastrar outro com o mesmo nome, mesmo que use maiúsculas e minúsculas diferentes, **Then** o segundo hábito não é criado e ela é informada de que o nome já está em uso.

---

### User Story 2 - Marcar o hábito de hoje e acompanhar a sequência (Priority: P1)

A pessoa marca que cumpriu um hábito hoje e acompanha quantos dias consecutivos já o cumpriu.

**Why this priority**: A marcação diária é a ação central que permite medir a continuidade do hábito.

**Independent Test**: Marcar um hábito em dias sucessivos e verificar a sequência; repetir a marcação no mesmo dia e verificar que ela não aumenta.

**Acceptance Scenarios**:

1. **Given** um hábito ainda não marcado, **When** a pessoa marca “Fiz hoje”, **Then** a sequência passa a ser 1.
2. **Given** que a pessoa já marcou o hábito hoje, **When** marca “Fiz hoje” novamente no mesmo dia, **Then** a sequência permanece igual e não é criada uma segunda marcação para esse dia.
3. **Given** que o hábito foi marcado no dia anterior e em todos os dias anteriores da sequência, **When** a pessoa o marca hoje, **Then** a sequência aumenta em 1.
4. **Given** que passou ao menos um dia sem marcar o hábito, **When** a pessoa volta a marcá-lo, **Then** uma nova sequência começa em 1.
5. **Given** que a pessoa marcou um hábito hoje, **When** consulta a lista, **Then** vê a sequência atualizada junto ao hábito.
6. **Given** que o computador da pessoa informa a data local de hoje, **When** ela marca “Fiz hoje”, **Then** a marcação é associada a essa data local.
7. **Given** que a última marcação do hábito foi há dois ou mais dias e ele ainda não foi marcado hoje, **When** a pessoa consulta a lista, **Then** vê sequência 0; ao marcar hoje, a sequência passa a 1.

---

### User Story 3 - Acompanhar vários hábitos (Priority: P2)

A pessoa mantém hábitos distintos e acompanha a sequência de cada um sem que as marcações de um alterem as dos demais.

**Why this priority**: A lista deve permitir acompanhar uma rotina composta por mais de um hábito de forma independente.

**Independent Test**: Cadastrar dois hábitos, marcar apenas um e confirmar que a sequência de cada item reflete somente suas próprias marcações.

**Acceptance Scenarios**:

1. **Given** dois hábitos cadastrados com históricos diferentes, **When** a pessoa consulta a lista, **Then** cada hábito apresenta sua própria sequência.
2. **Given** que a pessoa marca um dos hábitos, **When** consulta a lista, **Then** a sequência do outro hábito não é alterada.

### Edge Cases

- Um hábito sem marcações deve aparecer com sequência 0.
- Um nome vazio ou composto apenas por espaços não deve criar um hábito.
- Dois hábitos não podem ter nomes iguais, mesmo que difiram apenas entre maiúsculas e minúsculas.
- Marcações repetidas na mesma data local contam como uma única marcação.
- Um intervalo de um ou mais dias sem marcação reinicia a sequência para 1 na próxima marcação.
- Antes da próxima marcação após um dia sem cumprimento, a lista mostra sequência 0; uma nova marcação após o intervalo inicia a sequência em 1.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A pessoa MUST conseguir cadastrar um hábito informando seu nome.
- **FR-002**: O sistema MUST impedir o cadastro de um nome vazio ou composto apenas por espaços e MUST orientar a pessoa a informar um nome.
- **FR-003**: A pessoa MUST conseguir marcar “Fiz hoje” para cada hábito cadastrado.
- **FR-004**: A primeira marcação de um hábito MUST definir sua sequência como 1.
- **FR-005**: O sistema MUST contar no máximo uma marcação por hábito em cada data local; marcações repetidas no mesmo dia MUST manter a sequência inalterada.
- **FR-006**: Uma marcação em uma data local imediatamente seguinte à última marcação MUST aumentar a sequência em 1.
- **FR-007**: Se houver um ou mais dias sem marcação entre a última marcação e a nova, o sistema MUST iniciar a sequência em 1 na nova marcação.
- **FR-008**: A pessoa MUST conseguir consultar uma lista de todos os hábitos cadastrados e a sequência correspondente a cada um.
- **FR-009**: As marcações e sequências de cada hábito MUST ser independentes das dos demais hábitos.
- **FR-010**: O sistema MUST considerar como data do dia a data local informada pelo computador da pessoa.
- **FR-011**: Se a última marcação de um hábito ocorreu há dois ou mais dias e ele ainda não foi marcado hoje, o sistema MUST exibir sequência 0; após uma nova marcação, MUST exibir sequência 1.
- **FR-012**: O sistema MUST impedir o cadastro de um hábito quando já existir outro cujo nome seja igual sem diferenciar maiúsculas e minúsculas e MUST informar que o nome já está em uso.

### Key Entities *(include if feature involves data)*

- **Hábito**: Uma atividade cadastrada pela pessoa, identificada por um nome que não pode ser igual ao de outro hábito quando ignoradas as diferenças entre maiúsculas e minúsculas, e acompanhada por sua sequência de dias consecutivos.
- **Marcação diária**: O registro de que um hábito foi cumprido em uma data local específica; cada hábito pode ter no máximo uma marcação por data.
- **Sequência**: A quantidade de datas locais consecutivas com uma marcação para o mesmo hábito, iniciada em 1 na primeira marcação ou após um intervalo sem marcações.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Em testes dos cenários de primeira marcação, marcação repetida no mesmo dia, dias consecutivos e retorno após intervalo, 100% dos resultados exibem a sequência definida pelas regras.
- **SC-002**: Em teste de aceitação, pelo menos 90% das pessoas conseguem cadastrar um hábito e localizar sua sequência na lista sem ajuda em até 1 minuto.
- **SC-003**: Em teste com três ou mais hábitos e históricos distintos, 100% dos hábitos aparecem na lista com suas próprias sequências, sem alteração causada por marcações de outros hábitos.

## Assumptions

- O app é usado por uma pessoa no próprio computador; contas, compartilhamento e sincronização entre dispositivos estão fora do escopo desta funcionalidade.
- As informações dos hábitos e suas marcações permanecem no computador da pessoa e não são enviadas a serviços externos.
- “Hoje” e a continuidade entre dias usam a data local informada pelo computador, sem conversão entre fusos horários.
- A lista inclui hábitos ainda não marcados, que começam com sequência 0.
- A sequência mostrada é 0 após um ou mais dias sem cumprimento, até a pessoa marcar novamente; essa marcação inicia a sequência em 1.
- Lembretes, metas, edição e exclusão de hábitos não fazem parte deste escopo.
