# Pedidos do Dia 3 — Especifique de verdade

Tudo o que foi digitado para chegar a esta solução.

## 1. Criar o spec

Num chat novo, no modo agente:

```
/speckit-specify Escreva em português do Brasil. O Hábito Certo é um app para quem quer criar hábitos. A pessoa cadastra hábitos pelo nome, marca "fiz hoje" em cada um e vê há quantos dias seguidos cumpriu cada hábito. Regras: um hábito marcado pela primeira vez tem sequência 1; marcar duas vezes no mesmo dia não muda a sequência; se a pessoa pulou um dia, a sequência volta a ser 1 na próxima marcação. A pessoa também pode ver a lista dos seus hábitos com a sequência de cada um.
```

A descrição não cita linguagem, banco de dados nem tela: isso fica para o plano. O comando criou sozinho a branch `001-habitos-sequencia` e um checklist de qualidade.

## 2. Esclarecer, primeira tentativa (sem foco)

```
/speckit-clarify Responda e escreva em português do Brasil.
```

**Resultado:** "No critical ambiguities detected". Nenhuma pergunta, nenhuma mudança no spec. O agente não encontrou nem a dúvida do dia pulado.

## 3. Esclarecer, segunda tentativa (com as dúvidas)

Antes de rodar de novo, as dúvidas foram listadas lendo o spec. Depois, num chat novo:

```
/speckit-clarify Responda e escreva em português do Brasil. Foque nestas dúvidas: 1) se a pessoa não marcou um hábito ontem, o que a lista mostra hoje antes de ela marcar: a sequência antiga ou 0? 2) dá para cadastrar dois hábitos com o mesmo nome? 3) "Leitura" e "leitura" são o mesmo hábito?
```

O agente fez três perguntas, uma por vez, cada uma com opções e uma recomendação:

| Pergunta | Recomendação do agente | Resposta dada | Por quê |
| :--- | :--- | :--- | :--- |
| O que a lista mostra depois de um dia pulado? | A: a sequência antiga | **B: mostrar 0** | A sequência já foi quebrada; mostrar a antiga esconde isso da pessoa |
| Dois hábitos com o mesmo nome? | A: não permitir | **A** | Com dois nomes iguais, não dá para saber em qual marcar |
| "Leitura" e "leitura" são o mesmo hábito? | A: sim | **A** | Senão, a regra anterior é contornada trocando uma letra |

As respostas foram dadas digitando só a letra no chat. O agente registrou as decisões na seção "Clarifications" do spec e criou os requisitos FR-011 e FR-012.

## Commit

```
git add .
git commit -m "docs: especifica hábitos e sequências com clarificações"
```
