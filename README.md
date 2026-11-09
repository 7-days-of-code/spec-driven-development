# #7DaysOfCode — Spec-Driven Development (Python + Spec Kit)

Bem-vindo(a) ao **#7DaysOfCode de Spec-Driven Development** da Alura!

Neste desafio de 7 dias, **o projeto inteiro é o desafio**. A cada dia, você dá um passo no mesmo sistema: em vez de pedir código a um agente de IA com uma frase solta, você escreve o que o software deve fazer, transforma isso em plano e tarefas, deixa o agente implementar e confere se ele cumpriu. No fim, você terá construído o **Hábito Certo**, um app local para registrar hábitos e acompanhar há quantos dias seguidos cada um foi cumprido.

Este repositório é o **gabarito** do desafio: cada branch mostra o projeto como ele fica no fim de um dia.

---

## A Dinâmica do Desafio: 7 Dias, 1 Projeto Evolutivo

Você vai construir o Hábito Certo do jeito Spec-Driven: o spec é a fonte da verdade, e o código vem depois.

```text
Dia 1  Escreva antes de codar        → spec.md à mão + script de terminal
  ↓
Dia 2  Spec Kit e a constituição     → projeto iniciado + princípios do projeto
  ↓
Dia 3  Especifique de verdade        → spec completo, sem ambiguidades
  ↓
Dia 4  Plano técnico e tarefas       → plan.md + tasks.md
  ↓
Dia 5  Mande o agente construir      → app rodando no navegador
  ↓
Dia 6  O código bate com o spec?     → checklist spec ↔ código + divergências corrigidas
  ↓
Dia 7  Mude o spec primeiro          → meta semanal pelo ciclo completo + README
```

---

## Diretriz de Complexidade e Abordagem

- **Nível:** iniciante/intermediário. Você precisa conseguir ler um script Python curto, mas não precisa escrever do zero.
- **Foco pedagógico:** conduzir um agente de IA com especificação, revisar o que ele entrega e mudar o produto alterando o spec primeiro.
- **Como cada dia funciona:**
  1. **Conceito:** a ideia do dia, explicada antes da prática.
  2. **Especificação ou revisão:** você escreve, decide ou confere.
  3. **Execução com o agente:** um comando do Spec Kit ou um pedido ao agente.
  4. **Entrega do dia:** commit do que foi feito, comparável com a branch de solução.

---

## Pré-requisitos e Stack Tecnológica

### Pré-requisitos

- Rodar comandos no terminal (`cd`, executar um script).
- Ler um script Python curto (variáveis, funções, `if`).
- Usar `git add`, `git commit` e `git push`.
- Conta no GitHub, sem cartão, com o [GitHub Copilot Free](https://github.com/features/copilot) ativado.

### Stack Tecnológica

- **Linguagem:** Python 3.11 ou superior.
- **Fluxo de SDD:** [Spec Kit](https://github.com/github/spec-kit) v1.3.0 (`specify-cli`), instalado com o [uv](https://docs.astral.sh/uv/).
- **Agente de IA:** GitHub Copilot Free no VS Code.
- **Aplicação:** Flask, com uma página web local.
- **Dados:** SQLite, guardado no próprio computador.
- **Testes:** pytest.

---

## Como Executar os Desafios Diários

1. Siga o e-mail do dia. Ele traz o conceito, o desafio e como saber que você concluiu.
2. Ao terminar, compare o seu projeto com a branch de solução daquele dia:
   - `solucao-dia-1`: spec escrito à mão e script de terminal
   - `solucao-dia-2`: Spec Kit iniciado e constituição
   - `solucao-dia-3`: spec com as clarificações
   - `solucao-dia-4`: plano técnico e lista de tarefas
   - `solucao-dia-5`: app rodando com as histórias P1 e P2
   - `solucao-dia-6`: checklist spec ↔ código e divergências corrigidas
   - `solucao-dia-7`: meta semanal e projeto completo
3. Em cada branch, o arquivo `PEDIDOS.md` mostra os comandos no terminal e os pedidos ao agente usados naquele dia, na ordem, com o que aconteceu no caminho.
4. Os arquivos que mais importam comparar são os que você escreveu ou decidiu: `.specify/memory/constitution.md`, `specs/*/spec.md`, `specs/*/plan.md` e `specs/*/tasks.md`. Tirando a constituição, os arquivos das pastas `.github/skills` e `.specify` são criados pelo Spec Kit e saem iguais para todo mundo que usa a mesma versão.
5. Para rodar o app da solução, com Python 3.11 ou superior:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1
```

   Abra http://127.0.0.1:5000 no navegador. Para rodar os testes: `python -m pytest`.

6. Compartilhe o seu progresso nas redes com a hashtag **#7DaysOfCode**, e use **#feedback7DoC** se quiser ajuda.
