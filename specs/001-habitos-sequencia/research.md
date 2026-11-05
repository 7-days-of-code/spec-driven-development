# Pesquisa: Hábitos e Sequências Diárias

## Decisões

### Estrutura da aplicação Flask

- **Decision**: Usar uma fábrica `create_app`, um módulo `app.py`, um arquivo `schema.sql`, um template e um módulo de testes. Abrir uma conexão SQLite por contexto de requisição e fechá-la ao final do contexto.
- **Rationale**: O padrão de fábrica e conexão por requisição é documentado pelo tutorial oficial do Flask e facilita criar uma aplicação de teste apontada para um banco temporário, sem adicionar uma arquitetura extensa.
- **Alternatives considered**: Separar rotas, banco e domínio em diversos pacotes; rejeitado para manter o projeto compacto e didático. Usar banco servidor; rejeitado porque SQLite atende o uso individual e não exige um serviço adicional.
- **References**: [Flask tutorial: layout](https://flask.palletsprojects.com/en/stable/tutorial/layout/), [application factory](https://flask.palletsprojects.com/en/stable/tutorial/factory/), [database](https://flask.palletsprojects.com/en/stable/tutorial/database/).

### Rotas e operações

- **Decision**: Expor a página `GET /`, cadastro por `POST /habits` e marcação diária por `POST /habits/<id>/check-ins`; redirecionar após operações POST, validar nomes no servidor e usar consultas SQL parametrizadas.
- **Rationale**: O fluxo é suficiente para a interface HTML proposta, segue o padrão de formulários do Flask e mantém alterações de estado fora de requisições GET. A restrição de unicidade no banco continua sendo a proteção final contra duplicatas.
- **Alternatives considered**: Criar API JSON ou frontend separado; rejeitado, pois a especificação pede uma página simples. Aceitar operações mutáveis por GET; rejeitado para preservar semântica clara das rotas.
- **References**: [Flask tutorial: views](https://flask.palletsprojects.com/en/stable/tutorial/views/), [Python `sqlite3`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute).

### Persistência e unicidade

- **Decision**: Persistir hábitos e marcações como registros distintos; armazenar o nome apresentado e uma chave calculada de `strip()` + normalização Unicode NFC + `casefold()` com restrição `UNIQUE`; impor também unicidade em `(habit_id, completed_on)`. Ativar chaves estrangeiras em cada conexão.
- **Rationale**: A sequência deriva dos registros de marcação, evitando contadores mutáveis que poderiam divergir do histórico. `casefold()` implementa comparação Unicode sem diferenciar caixa; NFC torna equivalentes formas canonicamente compostas/decompostas. A unicidade no SQLite protege contra duplicação mesmo com requisições repetidas.
- **Alternatives considered**: `COLLATE NOCASE`; rejeitado por sua comparação de caixa limitada a ASCII. Guardar somente um contador de sequência; rejeitado porque não preserva os registros necessários às regras de dias consecutivos e duplicação diária.
- **References**: [SQLite `CREATE TABLE` constraints](https://www.sqlite.org/lang_createtable.html), [SQLite collations](https://www.sqlite.org/datatype3.html#collation), [Python `str.casefold`](https://docs.python.org/3/library/stdtypes.html#str.casefold), [Python `unicodedata.normalize`](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize), [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html).

### Data local e cálculo de sequência

- **Decision**: Obter “hoje” em Python com `date.today()` no momento da marcação e armazenar a data ISO (`YYYY-MM-DD`). Calcular a sequência pelo histórico: contar datas consecutivas a partir da última marcação se ela for hoje ou ontem; exibir zero se a última marcação for anterior a ontem.
- **Rationale**: `date.today()` representa a data local do computador conforme a constituição. O cálculo cobre a regra de manter a sequência até o fim do dia atual antes da marcação e a regra de mostrar zero após uma lacuna. A data ISO é ordenável e validável com a biblioteca padrão.
- **Alternatives considered**: Usar `CURRENT_DATE` no SQLite; rejeitado porque a data corrente documentada pelo SQLite é UTC, não necessariamente a data local configurada no computador. Configurar um fuso horário IANA; rejeitado por não fazer parte do domínio definido.
- **References**: [Python `datetime.date.today`](https://docs.python.org/3/library/datetime.html#datetime.date.today), [SQLite date defaults](https://www.sqlite.org/lang_createtable.html).

### Testes

- **Decision**: Usar pytest, cliente de testes do Flask, banco SQLite novo em `tmp_path` por teste e controle do provedor de data para cenários determinísticos.
- **Rationale**: Os testes isolam dados entre execuções e exercitam o comportamento pelo mesmo contrato HTTP usado pela página, cobrindo validação, isolamento de hábitos, datas consecutivas, lacunas e repetições diárias.
- **Alternatives considered**: Depender de um banco compartilhado ou da data real do ambiente; rejeitado por tornar testes dependentes de estado e do dia em que são executados.
- **References**: [Flask tutorial: tests](https://flask.palletsprojects.com/en/stable/tutorial/tests/), [pytest `tmp_path`](https://docs.pytest.org/en/stable/how-to/tmp_path.html).

## Incertezas resolvidas

As escolhas de linguagem, framework, armazenamento, testes, execução local e privacidade foram fixadas pela solicitação do usuário. As regras de negócio restantes são definidas em `spec.md`; não há esclarecimentos pendentes para a fase de design.
