# Implementation Plan: Hábitos e Sequências Diárias

**Branch**: `solucao-dia-4` | **Feature**: `001-habitos-sequencia` | **Date**: 2026-11-05 | **Spec**: [spec.md](./spec.md)

**Input**: Especificação para cadastrar hábitos, registrar cumprimento diário e exibir sequências locais.

## Summary

Aplicação web simples, em português do Brasil, para uma pessoa cadastrar hábitos, registrar “Fiz hoje” e consultar a sequência de dias cumpridos. Será executada no próprio computador com Flask e Python 3.11+, persistirá hábitos e marcações em SQLite local, e calculará sequências a partir das datas registradas. A data do cumprimento virá da data local do computador; nenhuma conta, sincronização ou serviço externo será necessário.

## Technical Context

**Language/Version**: Python 3.11 ou superior  
**Primary Dependencies**: Flask; bibliotecas padrão do Python para SQLite, datas e normalização de texto  
**Storage**: SQLite no diretório local `instance/` da aplicação  
**Testing**: pytest e cliente de teste do Flask, com banco temporário por teste  
**Target Platform**: Computador pessoal com Python 3.11+ e navegador; execução local multiplataforma  
**Project Type**: Aplicação web local de página única  
**Performance Goals**: Uso individual e conjunto pequeno de hábitos; resposta imediata para as operações da página  
**Constraints**: Sem serviços externos, contas, sincronização ou dependências pagas; preservar os dados no computador; usar a data local do sistema; manter a estrutura e a implementação simples para iniciantes  
**Scale/Scope**: Uma pessoa, uma lista de hábitos, uma marcação por hábito por data; sem edição, exclusão, lembretes ou metas

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Princípio | Verificação no plano | Resultado |
|---|---|---|
| I. Ferramentas gratuitas | Python, Flask, SQLite e pytest são utilizáveis sem serviços ou licenças pagos. | PASS |
| II. Dados locais e privacidade | Banco SQLite e execução permanecem no computador; a aplicação não requer tráfego externo nem sincronização. | PASS |
| III. Comportamento verificável | Os cenários e critérios de aceitação da especificação usam Dado/Quando/Então e serão exercitados por testes. | PASS |
| IV. Dia baseado na data local | O dia será obtido da data local do sistema, sem conversão ou domínio de fuso horário. | PASS |
| V. Implementação precedida por especificação | Esta solução implementa apenas comportamentos já descritos em `spec.md`. | PASS |

**Gate pré-pesquisa**: PASS — não há violações nem decisões pendentes de produto que impeçam o desenho.

## Project Structure

### Documentation (this feature)

```text
specs/001-habitos-sequencia/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── web.md
└── tasks.md             # Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
app.py
schema.sql
requirements.txt
templates/
└── index.html
tests/
└── test_app.py
instance/
└── habitos.sqlite3      # Criado localmente em tempo de execução; não versionado
```

**Structure Decision**: Um único módulo Flask, um template, um esquema SQL e testes focados. A fábrica `create_app` permitirá apontar testes para bancos temporários sem exigir camadas ou serviços adicionais. O diretório `instance/` conterá os dados locais e será excluído do controle de versão.

## Phase 0: Research

As decisões e alternativas pesquisadas estão registradas em [research.md](./research.md). Não restam itens `NEEDS CLARIFICATION`.

## Phase 1: Design

- Entidades e regras de persistência: [data-model.md](./data-model.md).
- Contrato da interface HTTP e formulários: [contracts/web.md](./contracts/web.md).
- Execução e validação manual/automatizada: [quickstart.md](./quickstart.md).

**Gate pós-design**: PASS — a estrutura mantém a aplicação e os dados locais, usa somente as tecnologias especificadas e preserva os critérios da especificação. Não há violações a justificar nem complexidade adicional.

## Complexity Tracking

Não há violações da constituição ou complexidade adicional que exija justificativa.
