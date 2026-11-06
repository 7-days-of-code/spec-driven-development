# Pedidos do Dia 7 — Mude o spec primeiro

Tudo o que foi digitado para chegar a esta solução. A meta semanal entrou pelo ciclo completo: spec, plano, tarefas e código. Cada pedido foi feito num chat novo, no modo agente.

## 1. Spec da funcionalidade nova

```
/speckit-specify Escreva em português do Brasil. Nova funcionalidade do Hábito Certo: meta semanal. A pessoa pode definir, para cada hábito, quantos dias por semana quer cumpri-lo, de 1 a 7. A lista mostra, para cada hábito com meta, quantos dias ele foi marcado na semana atual e se a meta da semana foi atingida. A semana vai de segunda a domingo, pela data local do computador. Hábitos sem meta continuam funcionando como antes.
```

A descrição já diz quando a semana começa: sem isso, o agente escolheria sozinho. O comando criou a branch `002-meta-semanal` e a pasta `specs/002-meta-semanal`.

## 2. Plano

```
/speckit-plan Escreva em português do Brasil. Já está tudo commitado, não precisa fazer commit antes. Use a mesma stack e a mesma estrutura do projeto atual (Flask, SQLite, pytest, app.py, schema.sql, templates/index.html). A meta precisa funcionar com o banco que já existe, sem apagar dados.
```

A última frase é de propósito: acrescentar uma coluna ao banco é o tipo de mudança em que o erro do `DROP TABLE` do Dia 5 poderia voltar. O plano escolheu acrescentar a coluna só se ela não existir, sem apagar nada.

## 3. Tarefas

```
/speckit-tasks Escreva em português do Brasil. Já está tudo commitado, não precisa fazer commit antes. Organize as tarefas por história de usuário.
```

## 4. Implementação, em dois pedidos

```
/speckit-implement Responda em português do Brasil. Já está tudo commitado, não precisa fazer commit antes. Execute as Fases 1, 2 e 3 (até a T005) e pare. Marque as tarefas concluídas no tasks.md.
```

```
/speckit-implement Responda em português do Brasil. Já está tudo commitado, não precisa fazer commit antes. Execute as Fases 4, 5 e 6 (T006 a T010) e pare. Marque as tarefas concluídas no tasks.md.
```

## 5. README

Escrito à mão, sem o agente.

## Commits

```
git add .
git commit -m "docs: especifica a meta semanal (002)"
git commit -m "docs: planeja e quebra em tarefas a meta semanal (002)"
git commit -m "feat: define meta semanal por hábito com migração do banco (002, T001-T005)"
git commit -m "feat: mostra progresso da meta na semana atual (002, T006-T010)"
git commit -m "docs: acrescenta README do projeto"
```
