# Pedidos do Dia 5 — Mande o agente construir

Tudo o que foi digitado para chegar a esta solução. As 14 tarefas foram implementadas **por fase**, em quatro pedidos, com revisão e commit depois de cada um. Cada pedido foi feito num chat novo, no modo agente.

## Pedido 1: Fases 1 e 2 (T001 a T004)

```
/speckit-implement Responda em português do Brasil. Execute somente as Fases 1 e 2 (T001 a T004) e pare. Marque as tarefas concluídas no tasks.md.
```

**A revisão encontrou um problema grave:** o `schema.sql` começava com `DROP TABLE IF EXISTS`, e o app rodava esse arquivo toda vez que abria. Ou seja, **apagava todos os dados a cada vez que era aberto**. O teste do próprio agente só conferia se o app abria.

A causa estava no spec: ele nunca dizia que os dados continuam salvos depois de fechar o app. A correção seguiu a ordem do SDD. Primeiro, esta linha foi acrescentada ao `spec.md`, à mão, abaixo do FR-012:

```
- **FR-013**: Os hábitos e as marcações MUST continuar salvos depois que o app é fechado e aberto de novo.
```

Depois, num chat novo:

```
Responda em português do Brasil. O spec ganhou o FR-013: os dados devem continuar salvos depois que o app é fechado e aberto de novo. Hoje o schema.sql começa com DROP TABLE e o create_app roda o init_db toda vez que o app inicia, o que apaga tudo. Corrija para criar as tabelas só se ainda não existirem, sem apagar dados. Não mude mais nada.
```

## Pedido 2: Fase 3 (T005 a T007)

```
/speckit-implement Responda em português do Brasil. Execute somente a Fase 3 (T005 a T007) e pare. Marque as tarefas concluídas no tasks.md.
```

## Pedido 3: Fase 4 (T008 a T011)

```
/speckit-implement Responda em português do Brasil. Execute somente a Fase 4 (T008 a T011) e pare. Marque as tarefas concluídas no tasks.md.
```

O agente parou antes de começar e perguntou se devia fazer um commit das mudanças pendentes. Como tudo já estava commitado, a resposta foi:

```
Não precisa, já está tudo commitado. Pode seguir com a Fase 4 (T008 a T011) e parar no fim.
```

## Pedido 4: Fases 5 e 6 (T012 a T014)

A frase sobre o commit entrou no pedido para o agente não parar de novo:

```
/speckit-implement Responda em português do Brasil. Já está tudo commitado, não precisa fazer commit antes. Execute as Fases 5 e 6 (T012 a T014) e pare. Marque as tarefas concluídas no tasks.md.
```

## Commits

Um depois de cada pedido, pelo terminal:

```
git add .
git commit -m "feat: prepara projeto e fundação (T001-T004) e garante dados salvos (FR-013)"
git commit -m "feat: cadastra e lista hábitos (US1, T005-T007)"
git commit -m "feat: marca hábito do dia e calcula a sequência (US2, T008-T011)"
git commit -m "feat: isola sequências entre hábitos e valida a entrega (US3, T012-T014)"
```

## Rodar o app

O agente criou o ambiente virtual `.venv` na Fase 1. No Windows:

```
.\.venv\Scripts\Activate.ps1
python -m flask --app app run --host 127.0.0.1
```

Abrir http://127.0.0.1:5000 no navegador. Para os testes: `python -m pytest`.
