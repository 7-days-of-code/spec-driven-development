# Hábito Certo

App local para cadastrar hábitos, marcar "Fiz hoje" e acompanhar há quantos dias seguidos cada hábito foi cumprido, com meta semanal opcional.

Projeto feito no **7 Days of Code de Spec-Driven Development**: cada funcionalidade começou por uma especificação escrita, passou por plano e tarefas e só então virou código, implementado por um agente de IA e revisado contra o spec.

## O que ele faz

- Cadastra hábitos pelo nome. Nomes repetidos não são aceitos, mesmo com maiúsculas diferentes.
- Marca "Fiz hoje" uma vez por dia em cada hábito.
- Mostra a sequência de dias seguidos. Se um dia for pulado, a sequência volta a 0 até a próxima marcação.
- Permite definir uma meta de 1 a 7 dias por semana e mostra o progresso da semana atual (segunda a domingo).
- Guarda tudo no próprio computador, em SQLite. Nada vai para a internet.

## Como rodar

Precisa de **Python 3.11 ou superior**.

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1
```

Abra http://127.0.0.1:5000 no navegador. Para parar, use `Ctrl+C` no terminal.

Para rodar os testes, com o ambiente virtual ativado:

```powershell
python -m pytest
```

## Como foi construído

| Etapa | Arquivo |
| :--- | :--- |
| Princípios do projeto | [`.specify/memory/constitution.md`](.specify/memory/constitution.md) |
| Spec de hábitos e sequências | [`specs/001-habitos-sequencia/spec.md`](specs/001-habitos-sequencia/spec.md) |
| Plano e tarefas | [`plan.md`](specs/001-habitos-sequencia/plan.md) e [`tasks.md`](specs/001-habitos-sequencia/tasks.md) |
| Conferência spec ↔ código | [`checklists/spec-codigo.md`](specs/001-habitos-sequencia/checklists/spec-codigo.md) |
| Spec da meta semanal | [`specs/002-meta-semanal/spec.md`](specs/002-meta-semanal/spec.md) |

Ferramentas: [Spec Kit](https://github.com/github/spec-kit) para o fluxo spec → plano → tarefas e GitHub Copilot Free como agente de IA.

## Uma decisão que o spec resolveu

Se a pessoa não marcou um hábito ontem, o que a lista mostra hoje, antes de ela marcar? A sequência antiga ou 0?

O agente recomendou manter a sequência antiga. A decisão foi **mostrar 0**: é mais honesto, porque a sequência já foi quebrada, e evita que a pessoa só descubra isso ao marcar de novo. A resposta ficou registrada no spec (FR-011) e virou teste.
