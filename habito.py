import argparse
import json
from datetime import date, timedelta
from pathlib import Path
from typing import TypedDict


ARQUIVO_ESTADO = Path(__file__).with_name("habito.json")


class RegistroHabito(TypedDict):
    ultima_data: str
    sequencia: int


def carregar_estado() -> dict[str, RegistroHabito]:
    if not ARQUIVO_ESTADO.exists():
        return {}
    return json.loads(ARQUIVO_ESTADO.read_text(encoding="utf-8"))


def marcar_feito(habito: str, hoje: date | None = None) -> int:
    hoje = hoje or date.today()
    estado = carregar_estado()
    registro = estado.get(habito)

    if registro is None:
        sequencia = 1
    else:
        ultima_data = date.fromisoformat(registro["ultima_data"])
        sequencia = registro["sequencia"]
        if ultima_data == hoje:
            return sequencia
        if ultima_data == hoje - timedelta(days=1):
            sequencia += 1
        else:
            sequencia = 1

    estado[habito] = {"ultima_data": hoje.isoformat(), "sequencia": sequencia}
    ARQUIVO_ESTADO.write_text(
        json.dumps(estado, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return sequencia


def obter_sequencia(habito: str, hoje: date | None = None) -> int:
    hoje = hoje or date.today()
    registro = carregar_estado().get(habito)
    if registro is None:
        return 0

    ultima_data = date.fromisoformat(registro["ultima_data"])
    if ultima_data not in (hoje, hoje - timedelta(days=1)):
        return 0
    return registro["sequencia"]


def main() -> None:
    parser = argparse.ArgumentParser()
    comandos = parser.add_subparsers(dest="comando", required=True)

    for comando in ("feito", "sequencia"):
        subparser = comandos.add_parser(comando)
        subparser.add_argument("habito", nargs="+")

    argumentos = parser.parse_args()
    habito = " ".join(argumentos.habito)

    if argumentos.comando == "feito":
        sequencia = marcar_feito(habito)
    else:
        sequencia = obter_sequencia(habito)
    print(f"Sequência: {sequencia}")


if __name__ == "__main__":
    main()
