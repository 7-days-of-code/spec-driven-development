# Pesquisa: Meta Semanal

## Persistência e compatibilidade com o banco existente

**Decisão**: Guardar a meta opcional em uma coluna anulável `weekly_goal` da tabela
`habit`. Atualizar o esquema de criação e fazer a inicialização verificar as colunas com
`PRAGMA table_info(habit)`, adicionando a coluna com `ALTER TABLE` apenas quando ausente.

**Racional**: A relação é de um para um com o hábito, e `NULL` representa naturalmente a
ausência de meta. O projeto já inicializa o esquema em `init_db()` e usa `sqlite3`, então
uma migração aditiva nesse ponto funciona com o banco local já configurado sem introduzir
dependências. Em banco legado, a coluna nova começa nula; os valores e relações
existentes permanecem intactos. Verificar a coluna torna a inicialização repetível.

**Alternativas consideradas**:
- Apagar e recriar a tabela ou o banco: rejeitada por perda de dados e incompatibilidade
  com o requisito de preservação.
- Guardar metas em arquivo ou serviço separado: rejeitada por duplicar persistência e
  contrariar o uso exclusivo do banco local existente.
- Criar uma tabela de metas: possível, mas desnecessária para um único valor opcional
  por hábito e exige uma relação adicional.
- Adotar um pacote de migrações: rejeitado por ser desproporcional a uma migração
  aditiva única e não existir no projeto.

## Contagem da semana

**Decisão**: Derivar a segunda-feira da semana atual a partir de `date.today()` e contar
as datas em `habit_checkin.completed_on` entre essa segunda-feira e o domingo inclusivo.

**Racional**: O aplicativo já usa `date.today()` para registrar marcações e datas ISO
para persistência. A restrição `UNIQUE(habit_id, completed_on)` garante no máximo uma
marcação por hábito/data. Um intervalo inclusivo seleciona exatamente os sete dias da
semana local e não inclui marcações de semanas adjacentes.

**Alternativas consideradas**:
- Agrupar pela semana no banco: rejeitada por misturar cálculo temporal específico do
  produto com a persistência e tornar menos explícito o uso da data local.
- Armazenar um contador semanal: rejeitada porque duplica dados derivados e exige
  atualizações e reinicializações a cada semana.
- Alterar ou reaproveitar a sequência diária como meta: rejeitada porque sequência e
  progresso semanal têm períodos e semânticas diferentes.

## Interface e validação

**Decisão**: Manter o padrão de formulários HTML e rotas Flask com POST já usado pelo
projeto. Usar um campo por hábito em que valor vazio remove a meta e valores numéricos
de 1 a 7 definem ou atualizam; validar no servidor antes de persistir.

**Racional**: Isso conserva o padrão simples de interface, fluxo de redirecionamento e
mensagens flash da aplicação, enquanto a validação do servidor cobre submissões que
não vêm do formulário esperado.

**Alternativas consideradas**:
- API JSON ou chamadas externas: rejeitadas, pois a interface atual é renderizada pelo
  Flask e não requer cliente externo.
- Permitir edição direta do banco ou depender somente de validação HTML: rejeitada
  porque não oferece a experiência de configuração pedida nem proteção de validação no
  servidor.
