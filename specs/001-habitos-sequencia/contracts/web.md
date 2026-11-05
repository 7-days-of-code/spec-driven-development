# Contrato HTTP da interface web

A aplicação atende somente no computador local. A interface é HTML renderizada no servidor, em português do Brasil. Formulários usam métodos POST para alterações e redirecionam à página principal após a operação.

## `GET /`

- **Resposta**: `200 text/html`.
- **Conteúdo**: formulário de cadastro e lista de todos os hábitos com nome, sequência atual e controle “Fiz hoje”.
- **Estado vazio**: orientar a pessoa a cadastrar o primeiro hábito.
- **Sequência**: `0` para hábito sem marcação ou com última marcação há dois ou mais dias; nos outros casos, quantidade de datas locais consecutivas conforme [data-model.md](../data-model.md).

## `POST /habits`

- **Entrada de formulário**: `name` (texto).
- **Sucesso**: cria hábito com nome aparado, exibe na lista com sequência `0` e redireciona para `/`.
- **Nome vazio ou só espaços**: não cria registro; exibe orientação para informar um nome e redireciona para `/`.
- **Nome duplicado sem distinção de caixa**: não cria registro; informa que o nome já está em uso e redireciona para `/`.
- A unicidade também considera equivalência Unicode após normalização NFC e `casefold()`.

## `POST /habits/<habit_id>/check-ins`

- **Entrada**: identificador inteiro do hábito na URL; sem entrada de data fornecida pelo navegador.
- **Sucesso**: associa a data local atual (`date.today()`) ao hábito; redireciona para `/` e mostra a sequência atualizada.
- **Repetição no mesmo dia**: mantém apenas uma marcação nessa data e não aumenta a sequência.
- **Hábito inexistente**: retorna `404`.
- **Persistência**: uma marcação de um hábito não altera qualquer outro hábito.

## Comportamento comum

- Consultas SQL recebem parâmetros, não concatenação de valores fornecidos pela pessoa.
- Nomes ou estados inválidos são apresentados como mensagens compreensíveis na página; operações inválidas não criam nem alteram dados.
- A aplicação e seu arquivo SQLite permanecem locais; não há endpoints de conta, sincronização ou dependência de rede.
