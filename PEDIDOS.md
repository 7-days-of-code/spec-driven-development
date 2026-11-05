# Pedidos do Dia 2 — Spec Kit e a constituição

Tudo o que foi digitado para chegar a esta solução.

## Comandos no terminal

Instalação do uv (Windows, PowerShell):

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

No Mac ou no Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`.

Depois, **num terminal novo** (no terminal em que o uv foi instalado, o comando `uv` ainda não é reconhecido):

```
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v1.3.0
specify version
```

Criação do projeto. O `init` pergunta o tipo de script: no Windows, `ps` já vem marcado e basta apertar Enter.

```
specify init habito-certo --integration copilot --extension git
cd habito-certo
git init -b main
```

O Spec Kit cria os arquivos, mas não inicia o Git: por isso o `git init`. O `-b main` faz a branch principal nascer com o nome que o GitHub usa.

## Pedido ao agente

Com a pasta `habito-certo` aberta no VS Code, num chat novo, no modo agente:

```
/speckit-constitution Escreva em português do Brasil. Os princípios do projeto Hábito Certo são:
1. Só ferramentas gratuitas: nada que exija pagamento ou cartão.
2. Os dados ficam no computador da pessoa: nada vai para a internet.
3. Todo comportamento tem critério de aceitação no formato Dado, Quando, Então.
4. "Dia" é a data local do computador; o projeto não trata fuso horário.
5. Nada é implementado sem estar no spec.
```

O agente pediu permissão algumas vezes para rodar os scripts do Spec Kit. Todas foram aprovadas.

## Commit

```
git add .
git commit -m "docs: cria constituição do Hábito Certo v1.0.0"
```

O `/speckit-git-commit`, sugerido pelo agente no fim, não foi usado: o commit pelo terminal não gasta crédito.

## O que aconteceu no caminho

- O agente manteve os cinco princípios e acrescentou seções do modelo do Spec Kit: restrições do produto, fluxo de desenvolvimento e governança.
- Alguns títulos ficaram em inglês, herdados do modelo, e a data de ratificação ficou como `TODO`.
