# Ferramentas MCP por tópico

O servidor MCP expõe ferramentas para que um cliente de IA observe e controle o
navegador. Os nomes e parâmetros podem mudar entre versões.

## Fluxo essencial

```text
browser_navigate → browser_map → agir → verificar → browser_screenshot
```

## Navegação

Exemplo conceitual:

```json
{
  "tool": "browser_navigate",
  "arguments": {
    "url": "https://example.com"
  }
}
```

Use ferramentas dessa categoria para abrir URLs e controlar a navegação.

## Mapear e localizar

```json
{
  "tool": "browser_map",
  "arguments": {}
}
```

Mapear a página permite que o agente compreenda elementos e construa a próxima
ação com base no estado atual, em vez de adivinhar.

## Ler conteúdo e estado

Ferramentas de leitura podem recuperar texto, atributos, valores e outras
informações sem alterar a página. Prefira leituras específicas a extrações
indiscriminadas de todo o conteúdo.

## Interação

Exemplo conceitual:

```json
{
  "tool": "browser_click",
  "arguments": {
    "role": "button",
    "text": "Entrar"
  }
}
```

A categoria de interação inclui ações como clicar, preencher campos, selecionar
opções e usar teclado ou mouse.

## Páginas e frames

Sites podem abrir novas abas ou usar `iframe`. O agente precisa identificar o
contexto correto antes de localizar ou interagir com um elemento.

## Capturas

```json
{
  "tool": "browser_screenshot",
  "arguments": {
    "fullPage": true
  }
}
```

Screenshots ajudam na verificação visual. Revise o conteúdo antes de compartilhar
ou publicar a imagem.

## Navegador e sessão

Ferramentas dessa categoria administram sessão, páginas e estado geral do
navegador. Encerrar recursos continua sendo uma responsabilidade importante.

## Tempo

Controles de tempo podem auxiliar em páginas com transições ou conteúdo
assíncrono. Uma condição verificável continua sendo preferível a uma pausa
arbitrária.

## Confirmação para ações sensíveis

O agente deve solicitar confirmação antes de ações como:

- enviar dados pessoais;
- concluir autenticação sensível;
- apagar informações;
- realizar compras;
- publicar ou enviar mensagens;
- alterar permissões.

## Referência completa

A referência complementar da Daisy Ladybug organiza atualmente as ferramentas
em Navigate, Find & Read, Interact, Pages & Frames, Capture, State, Browser e
Clock:

- [Referência MCP](https://www.daisyladybug.com/vibium/mcp/)
- [Tutorial oficial de MCP](https://github.com/VibiumDev/vibium/blob/main/docs/tutorials/getting-started-mcp.md)

