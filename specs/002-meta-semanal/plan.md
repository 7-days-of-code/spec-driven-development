# Plano de Implementação: Meta Semanal

**Branch**: `002-meta-semanal` | **Data**: 2026-11-06 | **Spec**: [spec.md](./spec.md)

## Resumo

Adicionar metas semanais opcionais de 1 a 7 dias por hábito, permitindo configurar,
alterar e remover a meta e mostrando o progresso de segunda a domingo na lista. A
implementação preservará os hábitos e as marcações já armazenados: a inicialização do
SQLite fará uma migração aditiva e idempotente para acrescentar a coluna da meta somente
quando ela ainda não existir. O cálculo usará a data local já empregada pelo aplicativo
e as marcações existentes, sem alterar a sequência diária.

## Contexto Técnico

**Linguagem/Versão**: Python 3 (o repositório não fixa uma versão mínima).

**Dependências principais**: Flask 3.x e biblioteca padrão `sqlite3`; sem novas
dependências.

**Armazenamento**: SQLite local, arquivo configurado em `DATABASE` (por padrão
`instance/habitos.sqlite3`).

**Testes**: pytest 8.x.

**Plataforma-alvo**: Aplicação web local executada no ambiente da pessoa.

**Tipo de projeto**: Aplicação web Flask de projeto único.

**Metas de desempenho**: Não há requisito de desempenho específico; listar os hábitos e
calcular seu progresso com as consultas SQLite existentes é suficiente para o escopo
local do projeto.

**Restrições**: Preservar dados e compatibilidade com bancos existentes; não apagar nem
recriar tabelas; não adicionar serviços externos; usar a data local; manter hábitos sem
meta e a sequência diária inalterados.

**Escala/escopo**: Uso local, para os hábitos cadastrados no banco da pessoa.

## Verificação da Constituição

| Princípio/regra | Verificação | Estado |
|---|---|---|
| Ferramentas gratuitas | Flask, SQLite e pytest existentes; nenhuma dependência ou serviço pago será adicionado. | PASSA |
| Dados locais e privacidade | Metas e progresso permanecem no SQLite local; nenhuma sincronização ou envio externo. | PASSA |
| Comportamento verificável | Os cenários e resultados observáveis estão descritos no spec em formato Dado/Quando/Então. | PASSA |
| Dia baseado na data local | O período será calculado usando `date.today()` e datas ISO locais, sem conversão de fuso. | PASSA |
| Especificação antes da implementação | `spec.md` foi elaborado antes deste plano e permanece a fonte de comportamento. | PASSA |
| Integridade dos dados existentes | A migração será aditiva e condicional à ausência da coluna; nenhuma marcação ou hábito será descartado. | PASSA |

**Gate pré-pesquisa**: PASSA. Não há conflito com a constituição nem questão de
produto não especificada que impeça o desenho.

## Estrutura do Projeto

### Documentação desta feature

```text
specs/002-meta-semanal/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── web.md
└── spec.md
```

### Código existente a evoluir

```text
app.py                  # rotas, cálculo de sequência e inicialização do SQLite
schema.sql              # esquema inicial do banco
templates/
└── index.html          # lista, formulário de hábito e marcação diária
tests/
└── test_app.py         # testes Flask com banco temporário
requirements.txt        # Flask e pytest
```

**Decisão de estrutura**: Manter o projeto de arquivo único e seus diretórios atuais.
As alterações funcionais ficarão em `app.py`, `schema.sql` e `templates/index.html`;
os testes serão adicionados a `tests/test_app.py`. Não criar camadas, banco novo ou
framework de migração para esta funcionalidade.

## Decisões de Projeto

- Armazenar a meta como `habit.weekly_goal`, anulável, para que a meta pertença
  diretamente ao hábito e hábitos existentes continuem sem meta.
- Na inicialização, comparar as colunas de `habit` com `PRAGMA table_info`; executar
  `ALTER TABLE ... ADD COLUMN` somente se `weekly_goal` não existir. A criação de banco
  novo também incluirá a coluna no `schema.sql`. A operação será idempotente e não
  reescreverá hábitos nem marcações.
- Receber configuração, alteração e remoção em um formulário por hábito; um valor vazio
  remove a meta. O servidor validará rigorosamente os valores de 1 a 7 e comunicará
  valores inválidos.
- Calcular o início da semana local como segunda-feira e contar as marcações no
  intervalo inclusivo de segunda a domingo. O progresso será derivado das marcações,
  sem armazenamento duplicado.
- Exibir progresso somente para hábitos com meta. A contagem não modificará o cálculo
  nem os registros usados pela sequência diária.

## Gate após o desenho

**Gate pós-design**: PASSA. O modelo opcional mantém os dados legados válidos; a
migração apenas adiciona uma coluna, e o contrato preserva os fluxos existentes. As
decisões respeitam os princípios de dados locais, data local e comportamento verificável.

## Rastreamento de Complexidade

Não há violações da constituição nem complexidade adicional a justificar.
