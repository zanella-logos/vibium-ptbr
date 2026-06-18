# Python ou MCP?

As duas opções controlam um navegador, mas servem a arquiteturas diferentes.

| Critério | Python | MCP |
|---|---|---|
| Quem define a sequência | Código escrito previamente | Cliente de IA escolhe ferramentas |
| Previsibilidade | Maior | Depende do agente e das instruções |
| Uso típico | Robôs, testes e integrações | Exploração e automação assistida por IA |
| Repetibilidade | Natural em código versionado | Exige prompts, limites e verificação |
| Segurança | Controlada pela implementação | Também depende das permissões do agente |
| Depuração | Logs, testes e debugger Python | Histórico de ferramentas e logs do cliente |

## Escolha Python quando

- o fluxo é conhecido e repetitivo;
- a regra de negócio precisa ser determinística;
- há execução agendada ou em lote;
- erros precisam ser classificados de forma previsível;
- o sistema exige testes automatizados.

## Escolha MCP quando

- a tarefa exige exploração;
- o caminho varia conforme o estado da página;
- uma pessoa está acompanhando a execução;
- o cliente de IA precisa verificar uma interface;
- velocidade de experimentação é mais importante que determinismo total.

## Combinação

Uma estratégia comum é usar MCP para explorar e compreender um fluxo e depois
implementar a versão estável em Python. O sentido inverso também existe: um
agente pode usar ferramentas para investigar falhas de uma automação existente.

