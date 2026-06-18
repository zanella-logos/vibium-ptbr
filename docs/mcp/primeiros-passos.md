# Primeiros passos com Vibium MCP

MCP significa Model Context Protocol. No Vibium, o servidor MCP disponibiliza
ações de navegador como ferramentas estruturadas para clientes de IA.

```text
cliente de IA → ferramentas MCP → Vibium → Chrome
```

## Pré-requisitos

- Node.js com `npx`;
- um cliente compatível com MCP;
- permissão para iniciar o Chrome e baixar componentes na primeira execução.

## Chave de API e autenticação

O servidor MCP do Vibium não exige uma chave de API própria para controlar o
navegador localmente.

Entretanto, o **cliente de IA** usado com ele precisa estar autenticado. Conforme
o cliente e o plano escolhido, isso pode ocorrer por:

- login em uma conta;
- assinatura do produto;
- chave de API do provedor do modelo;
- credenciais fornecidas por uma organização.

Por exemplo, Claude Code e Gemini CLI possuem processos próprios de
autenticação. Consulte a documentação do cliente escolhido antes da
configuração.

Nunca coloque uma chave diretamente no arquivo de configuração MCP, em exemplos
públicos ou no Git. Use o mecanismo recomendado pelo cliente, variáveis de
ambiente ou um gerenciador de segredos.

## Exemplos de configuração

Claude Code:

```bash
claude mcp add vibium -- npx -y vibium mcp
```

Gemini CLI:

```bash
gemini mcp add vibium npx -y vibium mcp
```

Após configurar, reinicie a sessão do cliente para que as ferramentas sejam
descobertas.

## Testar o servidor

```bash
npx -y vibium mcp
```

O processo deve iniciar e aguardar mensagens. Use `Ctrl+C` para encerrá-lo.

## Fluxo básico

A referência atual resume o ciclo como:

```text
navegar → mapear → agir → capturar
```

Exemplo conceitual de ferramentas:

```text
browser_navigate
browser_map
browser_click
browser_screenshot
```

Os nomes, parâmetros e a quantidade de ferramentas podem mudar. Consulte:

- [tutorial oficial de MCP](https://github.com/VibiumDev/vibium/blob/main/docs/tutorials/getting-started-mcp.md);
- [referência de ferramentas MCP](https://www.daisyladybug.com/vibium/mcp/).

Veja também [Ferramentas MCP por tópico](ferramentas-por-topico.md).

## Segurança

Não conceda liberdade irrestrita a um agente em sistemas sensíveis. Defina:

- quais sites podem ser acessados;
- quais ações exigem confirmação;
- quais dados podem ser enviados;
- como downloads e screenshots serão armazenados;
- como os passos serão auditados;
- quando uma pessoa deve assumir o controle.

Autenticação, pagamentos, exclusões e envio de dados merecem controles
adicionais.
