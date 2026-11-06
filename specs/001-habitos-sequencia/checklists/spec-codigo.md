# Checklist spec ↔ código — Hábitos e Sequências Diárias

**Data**: 2026-11-06 · **Branch**: `solucao-dia-6`

Para cada requisito do `spec.md`: onde ele está no código, qual teste confere e se passa.

## Requisitos funcionais

| Req. | O que diz | Onde no código | Teste que confere | Situação |
| :--- | :--- | :--- | :--- | :---: |
| FR-001 | Cadastrar hábito pelo nome | `app.py`, `create_habit` | `test_list_habits_and_duplicate_validation` | ✅ |
| FR-002 | Barrar nome vazio ou só espaços, com orientação | `app.py`, `create_habit` | `test_list_habits_and_duplicate_validation` | ✅ |
| FR-003 | Marcar "Fiz hoje" | `app.py`, `check_in_habit` + botão em `index.html` | `test_check_in_sequence_and_missing_habit` | ✅ |
| FR-004 | Primeira marcação = 1 | `get_habit_sequence` | `test_check_in_sequence_and_missing_habit` | ✅ |
| FR-005 | No máximo uma marcação por dia | `UNIQUE(habit_id, completed_on)` em `schema.sql` | `test_check_in_sequence_and_missing_habit` | ✅ |
| FR-006 | Dia seguinte soma 1 | `get_habit_sequence` | `test_check_in_sequence_and_missing_habit` | ✅ |
| FR-007 | Depois de pular, nova marcação = 1 | `get_habit_sequence` | `test_check_in_sequence_and_missing_habit` | ✅ |
| FR-008 | Lista com todos os hábitos e sequências | `app.py`, `index` | `test_check_ins_keep_habit_sequences_independent` | ✅ |
| FR-009 | Hábitos independentes | `get_habit_sequence` por `habit_id` | `test_check_ins_keep_habit_sequences_independent` | ✅ |
| FR-010 | Data local do computador | `date.today()` | Testes congelam `date.today()` | ✅ |
| FR-011 | Pulou um dia e não marcou hoje = 0 | `get_habit_sequence` | `test_check_in_sequence_and_missing_habit` | ✅ |
| FR-012 | Nome repetido sem diferenciar maiúsculas | `name_key` com `casefold()` + `UNIQUE` | `test_duplicate_name_ignores_casefold_and_unicode` | ✅ |
| FR-013 | Dados continuam salvos depois de fechar o app | `CREATE TABLE IF NOT EXISTS` em `schema.sql` | `test_habits_and_sequences_persist_after_app_recreation` (acrescentado no Dia 6) | ✅ |
| FR-014 | Remover espaços das pontas e tratar acentos de forma padronizada | `normalize_habit_name` e `name_key` em `app.py` | `test_list_habits_and_duplicate_validation` | ✅ (requisito acrescentado no Dia 6) |

## Critérios de sucesso

| Critério | Situação |
| :--- | :--- |
| SC-001: cenários de marcação passam 100% | ✅ coberto pelos testes de US2 |
| SC-002: 90% das pessoas cadastram em 1 minuto | ⚠️ Não dá para verificar com teste automático. Exige teste com pessoas. |
| SC-003: três ou mais hábitos independentes | ✅ Teste com três hábitos acrescentado no Dia 6 (tarefa T015, achada pelo `/speckit-converge`). |

## Divergências encontradas

| # | Divergência | Quem achou | Onde corrigir | Por quê |
| :---: | :--- | :--- | :--- | :--- |
| 1 | O código **remove espaços do começo e do fim** do nome e trata "café" com acento composto e decomposto como iguais. O spec não diz nada disso. | Revisão humana | **Spec** | O código tomou uma decisão de produto que não estava escrita. O comportamento é bom; o spec é que ficou para trás. |
| 2 | **FR-013 sem teste automático.** Se alguém voltar o `DROP TABLE`, nenhum teste falha. | Revisão humana | **Testes** | O requisito existe, mas nada garante que continue valendo. |
| 3 | **SC-003 pede três hábitos**, o teste usa dois. | `/speckit-converge` | **Testes** | Lacuna pequena entre o critério e o teste. |
| 4 | **A constituição pede "Dado, Quando, Então"** e o spec usa "Given, When, Then". | Revisão humana | **Spec** (ou constituição) | O template do Spec Kit é em inglês. Baixo impacto; fica registrado. |
| 5 | **SC-002 não é verificável** neste projeto. | Revisão humana | **Spec** | Critério de sucesso que nenhum teste consegue medir. |

## Corrigido no Dia 6

- **Divergência 1:** feito. Requisito FR-014 acrescentado ao spec, à mão.
- **Divergências 2 e 3:** feito. Testes acrescentados pelo agente (T015 e T016). O teste do FR-013 foi conferido: com o `DROP TABLE` recolocado de propósito, ele falha.
- **Divergências 4 e 5:** registradas, sem correção. Baixo impacto.

Resultado: **7 testes passando.**
