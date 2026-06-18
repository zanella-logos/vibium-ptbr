# Vibium PT-BR

Guia comunitário e não oficial de Vibium em português brasileiro.

O objetivo deste repositório é facilitar os primeiros passos com automação de
navegadores usando Vibium, com foco na API Python, no servidor MCP e na migração
de projetos existentes.

> Este projeto não é mantido nem endossado pela equipe oficial do Vibium.
> Consulte sempre a documentação oficial antes de usar os exemplos em produção.

## Sobre o foco deste projeto

O conteúdo é escrito a partir da experiência prática do autor com **Python**,
que é atualmente a linguagem principal do guia.

A seção de **MCP** acompanha uma jornada de aprendizado em andamento: instalação,
configuração de clientes de IA, estudo das ferramentas e primeiros experimentos.
Ela será ampliada conforme os recursos forem testados na prática.

O Vibium também possui interfaces para JavaScript/TypeScript, Java e linha de
comando. Essas áreas não fazem parte dos estudos atuais do autor. Contribuições
de pessoas que utilizam essas tecnologias são bem-vindas, desde que tragam
exemplos verificados e referências técnicas.

## O que é Vibium?

Vibium é uma ferramenta de automação de navegadores construída sobre o padrão
WebDriver BiDi. Pode ser utilizada por linha de comando, como servidor MCP ou
por bibliotecas para Python, JavaScript/TypeScript e Java.

## Comece por aqui

- [Instalação](docs/instalacao.md)
- [Primeiro script com Python](docs/python/primeiro-script.md)
- [Conceitos da API Python](docs/python/conceitos.md)
- [Comandos Python por tópico](docs/python/comandos-por-topico.md)
- [Referência completa da API Python](docs/python/referencia-completa.md)
- [Primeiros passos com MCP](docs/mcp/primeiros-passos.md)
- [Ferramentas MCP por tópico](docs/mcp/ferramentas-por-topico.md)
- [Python ou MCP: qual escolher?](docs/python-ou-mcp.md)
- [Migração de Selenium](docs/comparativos/selenium.md)
- [Boas práticas](docs/boas-praticas.md)

## Exemplo rápido com Python

```python
from vibium import browser

bro = browser.start()

try:
    page = bro.page()
    page.go("https://example.com")

    titulo = page.find("h1")
    print(titulo.text())
finally:
    bro.stop()
```

## Fluxo mental

Uma automação confiável normalmente segue este ciclo:

```text
iniciar → navegar → localizar → interagir → verificar → evidenciar → encerrar
```

A verificação é parte da ação. Um clique sem erro não garante que o resultado
esperado ocorreu.

## Escopo atual

- fundamentos da API síncrona de Python;
- introdução à API assíncrona;
- instalação e fluxo básico de MCP;
- comparação conceitual com Selenium;
- exemplos públicos e reproduzíveis;
- práticas de segurança e manutenção.

## Compatibilidade

O Vibium evolui rapidamente. Os exemplos deste guia foram elaborados com base
na documentação disponível em junho de 2026. Os comandos Python principais
foram conferidos localmente com o Vibium `26.5.31`. Confira a versão instalada:

```bash
pip show vibium
```

## Fontes principais

- [Repositório oficial do Vibium](https://github.com/VibiumDev/vibium)
- [Tutorial oficial de Python](https://github.com/VibiumDev/vibium/blob/main/docs/tutorials/getting-started-python.md)
- [Tutorial oficial de MCP](https://github.com/VibiumDev/vibium/blob/main/docs/tutorials/getting-started-mcp.md)
- [Referência Python da Daisy Ladybug](https://www.daisyladybug.com/vibium/python/)
- [Referência MCP da Daisy Ladybug](https://www.daisyladybug.com/vibium/mcp/)

## Contribuições

Sim: a proposta de um projeto público é permitir que outras pessoas usem,
corrijam e ampliem o material. Correções, exemplos e novos capítulos são
bem-vindos, inclusive sobre JavaScript/TypeScript, Java e CLI.

Toda contribuição passa por revisão antes de entrar no projeto. Antes de
contribuir, consulte [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença e marcas

O conteúdo autoral deste guia é distribuído sob a licença MIT.

O projeto Vibium oficial utiliza a licença Apache 2.0. Vibium e nomes
relacionados pertencem aos seus respectivos titulares. Consulte o
[repositório oficial](https://github.com/VibiumDev/vibium) para código,
documentação e licença oficiais.
