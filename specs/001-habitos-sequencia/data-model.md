# Modelo de Dados: Hábitos e Sequências Diárias

O SQLite é a fonte persistente. A sequência é um valor derivado do histórico de marcações, não um campo salvo que possa ficar desatualizado.

## Hábito

| Campo | Tipo | Regras |
|---|---|---|
| `id` | INTEGER | Chave primária. |
| `name` | TEXT | Obrigatório; texto apresentado na interface, removendo espaços no início e no fim. Não pode ser vazio após `strip()`. |
| `name_key` | TEXT | Obrigatório e único; forma NFC de `name.strip()` convertida por `casefold()`. Usada para impedir duplicatas sem distinção de maiúsculas/minúsculas. |

Cada hábito pode ter zero ou várias marcações. Não há edição nem exclusão no escopo atual.

## Marcação diária

| Campo | Tipo | Regras |
|---|---|---|
| `id` | INTEGER | Chave primária. |
| `habit_id` | INTEGER | Obrigatório; chave estrangeira para `habit.id`. |
| `completed_on` | TEXT | Obrigatório; data local em ISO 8601 (`YYYY-MM-DD`). |

Uma restrição única em `(habit_id, completed_on)` permite no máximo uma marcação por hábito por data. As chaves estrangeiras devem ser ativadas em cada conexão SQLite. Uma repetição da marcação do mesmo dia deve ser idempotente.

## Sequência exibida

Não é persistida. Para cada hábito:

1. Sem marcações, exibir `0`.
2. Se a última data marcada for anterior a ontem, exibir `0` até que haja uma nova marcação.
3. Caso contrário, contar do dia da última marcação para trás enquanto houver uma marcação em cada data consecutiva.
4. Ao registrar hoje, a sequência resultante é 1 se a data anterior não for ontem; caso contrário, é a sequência anterior acrescida de 1. Se hoje já estiver registrado, o histórico e a sequência não mudam.

As datas usam a data local do computador fornecida por `date.today()`. Não são convertidas entre fusos.
