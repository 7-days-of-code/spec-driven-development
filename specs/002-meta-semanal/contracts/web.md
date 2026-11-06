# Contrato Web: Meta Semanal

## Página de hábitos

`GET /`

- Mantém a lista e os dados atuais de cada hábito, incluindo a sequência diária.
- Para cada hábito com meta, apresenta a quantidade de dias marcados na semana local
  atual e se a meta foi atingida.
- Para cada hábito sem meta, não apresenta estado de progresso semanal.
- Apresenta controles para definir, alterar ou remover a meta semanal do hábito.

## Definir, alterar ou remover meta

`POST /habits/<habit_id>/weekly-goal`

Formulário:

| Campo | Valores | Efeito |
|---|---|---|
| `days` | Inteiro de `1` a `7` | Define ou atualiza a meta daquele hábito. |
| `days` | Vazio | Remove a meta daquele hábito, sem remover o hábito nem seu histórico. |

- Uma submissão válida redireciona à página de hábitos após persistir a mudança.
- Valor malformado ou fora do intervalo é rejeitado, não altera a meta e mostra uma
  mensagem informando que o intervalo permitido é de 1 a 7 dias por semana.
- Um identificador de hábito inexistente responde com HTTP 404.
- O formulário não altera marcações ou sequências.
- Dados do formulário são validados no servidor; nenhuma API externa é introduzida.
