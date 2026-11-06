# Pedidos do Dia 6 — O código bate com o spec?

Tudo o que foi digitado ou escrito para chegar a esta solução.

## 1. Convergência

Num chat novo, no modo agente:

```
/speckit-converge Responda em português do Brasil. Já está tudo commitado, não precisa fazer commit antes. Compare o código com o spec.md, incluindo a constituição, e liste as divergências encontradas antes de acrescentar qualquer tarefa.
```

**Resultado:** o comando encontrou **uma** lacuna. O critério SC-003 pede três hábitos, e o teste usava dois. Ele criou a tarefa T015 numa nova "Fase 7: Convergência" do `tasks.md`.

## 2. Checklist spec ↔ código (escrito à mão)

O arquivo [`checklists/spec-codigo.md`](specs/001-habitos-sequencia/checklists/spec-codigo.md) foi montado lendo o spec e o código, requisito por requisito. Ele encontrou cinco divergências, das quais o `converge` só tinha apontado uma.

## 3. Correções feitas à mão

No `spec.md`, abaixo do FR-013, porque o código fazia algo que o spec não dizia:

```
- **FR-014**: O sistema MUST remover os espaços do começo e do fim do nome antes de salvar e de comparar, e MUST tratar como iguais nomes que só diferem na forma de escrever os acentos.
```

No `tasks.md`, abaixo da T015, porque o FR-013 não tinha nenhum teste:

```
- [ ] T016 Acrescentar teste que cadastra e marca um hábito, recria o app com o mesmo banco e confirma que o hábito e a sequência continuam lá, conforme FR-013
```

## 4. Implementar os testes que faltavam

Num chat novo:

```
/speckit-implement Responda em português do Brasil. Já está tudo commitado, não precisa fazer commit antes. Execute somente a Fase 7 (T015 e T016) e pare. Marque as tarefas concluídas no tasks.md.
```

O agente parou e perguntou: "Some checklists have unchecked items. Do you want to proceed with implementation anyway?". O motivo eram as caixinhas `[ ]` do checklist da etapa 2. A resposta foi:

```
yes
```

## 5. Teste do teste

Para conferir que o teste novo do FR-013 funciona, o `DROP TABLE` foi recolocado de propósito no `schema.sql`. O teste falhou, como devia. Com o `DROP TABLE` removido de novo, os 7 testes passaram.

## Commit

```
git add .
git commit -m "test: confere spec contra código e fecha divergências (FR-014, T015, T016)"
```
