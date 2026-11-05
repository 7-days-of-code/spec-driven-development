<!--
Sync Impact Report
- Version change: não definida → 1.0.0 (constituição inicial)
- Princípios adicionados: ferramentas gratuitas; dados locais; critérios de aceitação
  Dado/Quando/Então; data local sem tratamento de fuso horário; implementação guiada
  pelo spec.
- Seções adicionadas: Restrições do Produto; Fluxo de Desenvolvimento e Qualidade.
- Seções removidas: nenhuma.
- Pendências: confirmar a data original de ratificação.
-->

# Hábito Certo — Constituição

## Core Principles

### I. Ferramentas gratuitas
Ferramentas, serviços e dependências do projeto devem ser utilizáveis sem pagamento e sem
exigir cartão de crédito. Nenhuma decisão técnica pode tornar necessária uma assinatura,
licença paga ou plano pago para usar, desenvolver, testar ou distribuir o projeto.

### II. Dados locais e privacidade
Os dados da pessoa devem permanecer no computador dela. O projeto não pode enviar dados
para a internet, armazená-los em serviços remotos ou sincronizá-los com terceiros. Assim,
a pessoa mantém controle direto sobre suas informações.

### III. Comportamento verificável
Todo comportamento definido pelo projeto deve ter critérios de aceitação no formato
“Dado, Quando, Então”. Os critérios devem descrever condições observáveis que permitam
verificar o comportamento esperado.

### IV. Dia baseado na data local
“Dia” deve significar a data local informada pelo computador da pessoa. O projeto não pode
converter datas entre fusos horários nem tratar fusos horários como parte de seu domínio.

### V. Implementação precedida por especificação
Uma funcionalidade ou mudança de comportamento deve estar descrita na especificação
(spec) antes de ser implementada. O spec é a fonte de verdade para o comportamento
esperado; divergências devem ser resolvidas atualizando o spec antes da implementação.

## Restrições do Produto

As decisões de produto e técnicas devem respeitar os princípios acima. Em particular,
nenhum fluxo pode depender de serviços pagos, transferir dados da pessoa para fora do
computador ou introduzir semântica de fuso horário para o conceito de “Dia”.

## Fluxo de Desenvolvimento e Qualidade

Antes de implementar comportamento, a especificação deve documentar os critérios de
aceitação correspondentes em formato “Dado, Quando, Então”. A revisão de mudanças deve
confirmar que a implementação corresponde ao spec e que os princípios desta constituição
continuam atendidos.

## Governance

Esta constituição prevalece sobre práticas e documentos de projeto conflitantes. Uma
emenda deve ser registrada neste arquivo e aprovada pelos responsáveis pelo projeto.
Toda emenda deve avaliar impactos nos specs, na implementação e nos critérios de
aceitação existentes.

A versão segue SemVer: MAJOR para remoção ou redefinição incompatível de princípios ou
regras de governança; MINOR para novos princípios ou requisitos de governança; PATCH para
esclarecimentos editoriais sem alteração de significado.

Revisões de specs e de implementação devem verificar conformidade com esta constituição.
Critérios de aceitação devem permitir verificar os comportamentos definidos, e mudanças
que afetem dados, custos ou o conceito de “Dia” devem receber atenção explícita na revisão.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): data original não informada | **Last Amended**: 2026-11-05
