# Quickstart: Hábitos e Sequências Diárias

## Pré-requisitos

- Python 3.11 ou superior instalado.
- Navegador web.
- Nenhum serviço externo ou conta é necessário.

## Instalação e execução (PowerShell)

Na raiz do projeto:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1
```

Abra `http://127.0.0.1:5000` no navegador. O banco SQLite local será criado em `instance/`. Para encerrar, use `Ctrl+C` no terminal.

## Validação automatizada

Com o ambiente virtual ativado:

```powershell
python -m pytest
```

**Resultado esperado**: todos os testes passam sem acessar a internet; cada teste usa seu próprio banco temporário.

## Cenários de verificação manual

1. Cadastre `Leitura`. A página deve mostrar o hábito com sequência `0`.
2. Tente cadastrar `leitura`. O segundo cadastro deve ser recusado com mensagem de nome já em uso.
3. Marque “Fiz hoje”. A sequência deve mostrar `1`. Marque novamente no mesmo dia; deve continuar `1`.
4. Teste os limites de dias consecutivos e de intervalo usando os testes com data controlada. Uma marcação em dia seguido aumenta a sequência; após um dia ou mais sem marcação, a lista mostra `0` e a próxima marcação reinicia em `1`.
5. Cadastre outro hábito e marque apenas um deles. A sequência do outro deve permanecer independente.

Consulte [contracts/web.md](./contracts/web.md) para o contrato da interface e [data-model.md](./data-model.md) para as regras de persistência e sequência.
