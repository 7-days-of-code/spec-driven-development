# Hábito Certo — marcar e ver sequência

**Para quê:** quem quer criar um hábito precisa ver há quantos dias seguidos o cumpriu.

**Como usar:**
- `python habito.py feito <hábito>` marca o hábito como feito hoje.
- `python habito.py sequencia <hábito>` mostra a sequência do hábito, sem marcar.

**Critérios de aceitação:**
1. Dado um hábito novo, quando eu marco "feito", então a sequência é 1.
2. Dado um hábito já marcado hoje, quando eu marco de novo, então a sequência não muda.
3. Dado um hábito com sequência de 3 dias que não foi marcado ontem, quando eu marco "feito" hoje, então a sequência volta a ser 1.