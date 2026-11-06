# Modelo de Dados: Meta Semanal

## Hábito (`habit`)

Um hábito cadastrado localmente, com uma meta semanal opcional.

| Campo | Tipo/forma | Regras |
|---|---|---|
| `id` | `INTEGER`, chave primária | Identificador atual, preservado. |
| `name` | `TEXT NOT NULL` | Nome atual, sem alteração. |
| `name_key` | `TEXT NOT NULL UNIQUE` | Chave atual, sem alteração. |
| `weekly_goal` | `INTEGER NULL` | Nova meta opcional; quando presente, deve estar entre 1 e 7, inclusive. |

**Migração**: Em banco existente, acrescentar `weekly_goal` somente se a coluna não
estiver presente. A coluna começa como `NULL`; não atualizar nem remover hábitos,
marcações, chaves ou sequências. Em banco novo, criar a coluna junto com a tabela
existente.

**Transições da meta**:

- `NULL` → inteiro de 1 a 7: definir a meta.
- Inteiro de 1 a 7 → outro inteiro de 1 a 7: atualizar a meta.
- Inteiro de 1 a 7 → `NULL`: remover a meta.
- Valores abaixo de 1, acima de 7 ou que não sejam inteiros válidos: rejeitar sem
  persistir a mudança e orientar sobre o intervalo permitido.

## Marcação diária (`habit_checkin`)

Registro atual de um hábito concluído em uma data local. Os campos e a chave única
`(habit_id, completed_on)` permanecem inalterados. A contagem semanal considera cada
data distinta uma vez; nenhuma alteração de meta modifica esse registro ou a sequência
diária.

## Progresso semanal (derivado)

Não é persistido. Para cada hábito com meta, é calculado a partir da data local de hoje
e de suas marcações:

- **Período**: segunda-feira a domingo da semana da data local atual, ambas inclusivas.
- **Dias marcados**: número de datas do hábito dentro do período.
- **Meta atingida**: `dias_marcados >= weekly_goal`.
- O cálculo é atualizado ao consultar a lista e não afeta outros hábitos.
- Hábitos sem meta não apresentam progresso semanal, mas continuam exibindo e usando a
  sequência existente.
