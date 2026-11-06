# Pedidos do Dia 1 — Escreva antes de codar

Tudo o que foi digitado para chegar a esta solução. No Dia 1 não há Spec Kit: o spec é escrito à mão e entregue ao agente num chat comum.

## O spec entregue ao agente

O arquivo [`spec.md`](spec.md) desta branch, inteiro, colado no chat do Copilot (modo agente).

## Pedido ao agente

Logo abaixo do conteúdo do `spec.md`:

```
Implemente exatamente este spec como um script Python de terminal. Não adicione nada que não esteja escrito.
```

## Comandos no terminal

```
python habito.py feito leitura
python habito.py feito leitura
python habito.py sequencia leitura
```

## O que aconteceu no caminho

- **Na primeira tentativa, o spec não tinha a seção "Como usar".** O agente gerou um programa que cumpria os três critérios, mas sem os comandos `feito` e `sequencia`: cada execução marcava o hábito, e `sequencia leitura` marcava de novo em vez de só mostrar.
- **A correção foi no spec, não no código:** a seção "Como usar" foi acrescentada e o mesmo pedido foi feito de novo, num chat novo. O segundo programa passou no teste.
- **Antes de testar a segunda versão, o `habito.json` foi apagado**, porque guardava dados no formato da versão anterior.
