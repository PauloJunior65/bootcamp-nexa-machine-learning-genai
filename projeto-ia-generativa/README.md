# 🤖 Gerador de Conteúdo com IA Generativa

## 📒 Descrição
Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida em Python que utiliza IAs Generativas para criar conteúdos automaticamente. A aplicação demonstra como desenvolvedores podem integrar APIs de IA em seus projetos para gerar textos, ideias e conteúdos criativos.

## 🤖 Tecnologias Utilizadas
- **Python 3.10+** - Linguagem de programação principal
- **OpenAI API** - Para geração de texto com GPT
- **Rich** - Para interface CLI bonita e colorida
- **Python-dotenv** - Para gerenciamento de variáveis de ambiente
- **Requests** - Para chamadas HTTP às APIs

## 🧐 Processo de Criação
1. **Arquitetura**: Desenvolvi uma estrutura modular separando a lógica de IA dos componentes de interface
2. **Integração com APIs**: Implementei conectores para a API da OpenAI, com possibilidade de expansão para outras APIs
3. **Interface CLI**: Utilizei a biblioteca Rich para criar uma experiência de usuário agradável no terminal
4. **Configuração**: Usei dotenv para manter as chaves de API seguras e fora do código

## 🚀 Resultados
A ferramenta permite:
- ✅ Gerar textos criativos sobre qualquer tema
- ✅ Criar ideias para projetos
- ✅ Gerar descrições de produtos
- ✅ Sugerir títulos e headlines
- ✅ Modo offline com respostas simuladas para demonstração

### Exemplo de Uso
```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar API Key (opcional)
cp .env.example .env
# Editar .env com sua chave da OpenAI

# Executar o gerador
python main.py

# Ou executar em modo demo (sem API key)
python main.py --demo
```

### Screenshot
```
╭──────────────────────────────────────────────────────────────╮
│           🤖 Gerador de Conteúdo com IA Generativa           │
╰──────────────────────────────────────────────────────────────╯

? Escolha uma opção:
  1. 📝 Gerar texto criativo
  2. 💡 Gerar ideias para projeto
  3. 📦 Gerar descrição de produto
  4. 🎯 Gerar título/headline
  5. ❌ Sair

> Sua escolha: 1
> Tema do texto: Inteligência Artificial no futuro

╭──────────────────────────────────────────────────────────────╮
│                      📝 Texto Gerado                         │
╰──────────────────────────────────────────────────────────────╯

A Inteligência Artificial está transformando rapidamente nossa 
sociedade. No futuro, veremos IAs cada vez mais integradas em 
nosso cotidiano, desde assistentes pessoais até sistemas de 
saúde preditivos...
```

## 💭 Reflexão
Criar este projeto foi uma experiência enriquecedora que demonstrou como é simples integrar IAs Generativas em aplicações de software. O maior desafio foi criar uma interface amigável que funcionasse tanto com a API real quanto em modo demonstração, permitindo que qualquer pessoa possa testar a ferramenta mesmo sem uma chave de API.

## 📁 Estrutura do Projeto
```
projeto-ia-generativa/
├── README.md           # Este arquivo
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências Python
├── .env.example        # Exemplo de configuração
└── src/
    ├── __init__.py
    ├── generator.py    # Lógica de geração com IA
    ├── cli.py          # Interface de linha de comando
    └── config.py       # Configurações da aplicação
```

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Conta na OpenAI (opcional, para usar a API real)

### Passos
1. Clone o repositório
2. Navegue até a pasta do projeto: `cd projeto-ia-generativa`
3. Crie um ambiente virtual: `python -m venv venv`
4. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Instale as dependências: `pip install -r requirements.txt`
6. (Opcional) Configure sua API key no arquivo `.env`
7. Execute: `python main.py`

## 📄 Licença
Este projeto é parte do bootcamp Nexa de Machine Learning e IA Generativa da DIO.
