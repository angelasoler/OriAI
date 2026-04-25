# Assistente de Planejamento de Projetos Culturais

Aplicação Streamlit para preenchimento assistido do documento "PLANEJAMENTO DO PROJETO" do Ministério da Cultura.

## Funcionalidades

- Interface de chat com perguntas sequenciais
- Foco nas seções críticas (1-4): Identificação, Objeto, Justificativa e Público Beneficiário
- Preview em tempo real do documento Markdown
- Design corporativo gov.br
- 30 perguntas estruturadas para preenchimento completo

## Instalação

```bash
cd assistant_app
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Execução

```bash
streamlit run app.py
```

A aplicação estará disponível em http://localhost:8501

## Estrutura do Projeto

```
assistant_app/
├── app.py                 # Aplicação Streamlit principal
├── questions.py           # Definição das 30 perguntas
├── template.py           # Template Markdown do documento
├── knowledge_base.py     # Base de conhecimento (trechos da Cartilha e PNC)
├── requirements.txt       # Dependências
└── README.md             # Este arquivo
```

## Seções Cobertas

1. **Identificação do projeto e do proponente**
   - Informações do projeto
   - Dados do proponente
   - Dirigente responsável
   - Responsável técnico

2. **Definição do objeto**
   - Tipo de atividade (curso, oficina, seminário, etc.)
   - Tema e localização

3. **Complementação da Justificativa**
   - Motivos de origem
   - Realidade regional
   - Local de execução
   - Aderência ao PNC
   - Relação com PRONAC
   - Efeitos na comunidade

4. **Detalhamento do Público beneficiário**
   - Grupos/segmentos socioculturais
   - Quantidade e grupos etários

## Stack Tecnológico

- Python 3.x
- Streamlit
- python-markdown

## Design

- Cores gov.br: verde (#009c3b), azul (#0055a4), amarelo (#ffbd00)
- Layout com barra lateral para preview
- Interface intuitiva com navegação por botões
