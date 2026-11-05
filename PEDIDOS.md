# Pedidos do Dia 4 — Plano técnico e tarefas

Tudo o que foi digitado para chegar a esta solução.

## 1. Plano técnico

Num chat novo, no modo agente:

```
/speckit-plan Escreva em português do Brasil. Use Python 3.11 ou superior, Flask para uma página web simples que roda no próprio computador, SQLite para guardar os dados e pytest para os testes. Nada de serviços externos, contas ou bibliotecas pagas. Mantenha o projeto pequeno: é para uma pessoa iniciante entender o código.
```

A tecnologia que ficou fora do spec entra aqui. O comando gerou cinco arquivos: `plan.md`, `research.md`, `data-model.md`, `contracts/web.md` e `quickstart.md`.

## 2. Tarefas

Num chat novo:

```
/speckit-tasks Escreva em português do Brasil. Organize as tarefas por história de usuário, com as histórias P1 primeiro.
```

O resultado foram 14 tarefas em 6 fases, com os testes antes da implementação em cada história e o marcador `[P]` nas tarefas que podem rodar em paralelo.

## Commit

```
git add .
git commit -m "docs: cria plano técnico e lista de tarefas"
```

## O que aconteceu no caminho

- O plano decidiu sozinho tirar os espaços do começo e do fim do nome do hábito e padronizar os acentos. É uma decisão de produto, que deveria estar no spec: ela foi levada para o spec no Dia 6 (FR-014).
- Na verificação da constituição, o plano marcou como aprovado o princípio "critérios em Dado, Quando, Então", mas o spec usava "Given, When, Then". O agente não conferiu de verdade.
