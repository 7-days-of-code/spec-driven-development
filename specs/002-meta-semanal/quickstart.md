# Validação Rápida: Meta Semanal

## Pré-requisitos

- Python 3 instalado.
- Dependências do projeto instaladas.
- Para validação manual, uma cópia de segurança usual do banco pode ser feita antes de
  iniciar a versão atualizada. A inicialização da aplicação deve preservar o banco e
  seus dados; não apague nem recrie `instance/habitos.sqlite3`.

## Testes automatizados

Na raiz do repositório, execute:

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```

Resultado esperado: testes existentes continuam passando e os testes da feature
verificam, usando bancos temporários, definição/alteração/remoção e validação de metas,
limites de semana, persistência e compatibilidade com um banco legado contendo hábitos e
marcações antes da migração.

## Verificação manual com a aplicação

1. Inicie o servidor local:

   ```powershell
   python -m flask --app app run
   ```

2. Abra a página local e confirme que os hábitos e as sequências anteriores continuam
   visíveis; hábitos existentes começam sem meta.
3. Defina uma meta de 1 a 7 dias para um hábito. Confirme que a lista mostra os dias
   distintos marcados desde segunda-feira local e se a meta foi atingida.
4. Altere a meta e depois remova-a. Confirme que o estado de meta desaparece, enquanto
   as marcações e a sequência diária permanecem.
5. Tente submeter um valor menor que 1, maior que 7 ou não numérico. Confirme que a
   alteração é rejeitada e a orientação sobre o intervalo é exibida.
6. Reinicie o aplicativo e confirme que a meta válida continua salva.

O formato detalhado da página e da submissão está em [contracts/web.md](./contracts/web.md);
campos, validações e cálculo estão em [data-model.md](./data-model.md).
