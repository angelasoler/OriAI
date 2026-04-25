"""
Definição das perguntas e fluxo do questionário
"""

QUESTIONS = [
    # Seção 1 - Identificação do Projeto
    {
        "id": "numero_proposta",
        "section": "1.1",
        "question": "Qual o número da proposta na Plataforma Transferegov.br?",
        "type": "text",
        "required": True,
        "placeholder": "Ex: 2024-12345",
        "context": ""
    },
    {
        "id": "titulo_projeto",
        "section": "1.1",
        "question": "Qual o título do projeto?",
        "type": "text",
        "required": True,
        "placeholder": "Ex: Oficina de Maracatu para Jovens",
        "context": ""
    },
    {
        "id": "nome_proponente",
        "section": "1.2",
        "question": "Nome da entidade proponente:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: Associação Cultural XYZ",
        "context": ""
    },
    {
        "id": "cnpj_proponente",
        "section": "1.2",
        "question": "CNPJ da entidade:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: 00.000.000/0001-00",
        "context": ""
    },
    {
        "id": "endereco_proponente",
        "section": "1.2",
        "question": "Endereço completo / CEP / Município - UF:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: Rua das Flores, 123 - Centro - CEP 12345-678 - São Paulo - SP",
        "context": ""
    },
    {
        "id": "telefone_proponente",
        "section": "1.2",
        "question": "Contato telefônico:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: (11) 1234-5678",
        "context": ""
    },
    {
        "id": "email_proponente",
        "section": "1.2",
        "question": "E-mail:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: contato@organizacao.org.br",
        "context": ""
    },
    {
        "id": "site_proponente",
        "section": "1.2",
        "question": "Site (opcional):",
        "type": "text",
        "required": False,
        "placeholder": "Ex: www.organizacao.org.br",
        "context": ""
    },
    {
        "id": "nome_dirigente",
        "section": "1.3",
        "question": "Nome do dirigente responsável:",
        "type": "text",
        "required": True,
        "placeholder": "Nome completo do dirigente",
        "context": ""
    },
    {
        "id": "cargo_dirigente",
        "section": "1.3",
        "question": "Cargo/Função do dirigente:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: Presidente",
        "context": ""
    },
    {
        "id": "cpf_dirigente",
        "section": "1.3",
        "question": "CPF do dirigente:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: 000.000.000-00",
        "context": ""
    },
    {
        "id": "rg_dirigente",
        "section": "1.3",
        "question": "RG do dirigente:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: 12.345.678-9",
        "context": ""
    },
    {
        "id": "endereco_dirigente",
        "section": "1.3",
        "question": "Endereço residencial / CEP / Município - UF do dirigente:",
        "type": "text",
        "required": True,
        "placeholder": "Endereço completo",
        "context": ""
    },
    {
        "id": "telefone_dirigente",
        "section": "1.3",
        "question": "Contato telefônico do dirigente:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: (11) 9876-5432",
        "context": ""
    },
    {
        "id": "email_dirigente",
        "section": "1.3",
        "question": "E-mail do dirigente:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: dirigente@organizacao.org.br",
        "context": ""
    },
    {
        "id": "assinatura_dirigente",
        "section": "1.4",
        "question": "O dirigente da entidade é o responsável por assinar o Termo de Fomento?",
        "type": "select",
        "required": True,
        "options": ["Sim", "Não"],
        "context": ""
    },
    {
        "id": "nome_responsavel_tecnico",
        "section": "1.5",
        "question": "Nome do responsável técnico pelo projeto:",
        "type": "text",
        "required": True,
        "placeholder": "Nome completo do responsável técnico",
        "context": ""
    },
    {
        "id": "cargo_responsavel_tecnico",
        "section": "1.5",
        "question": "Cargo/Função do responsável técnico:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: Coordenador de Projetos",
        "context": ""
    },
    {
        "id": "telefone_responsavel_tecnico",
        "section": "1.5",
        "question": "Contato telefônico do responsável técnico:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: (11) 1111-2222",
        "context": ""
    },
    {
        "id": "email_responsavel_tecnico",
        "section": "1.5",
        "question": "E-mail do responsável técnico:",
        "type": "text",
        "required": True,
        "placeholder": "Ex: tecnico@organizacao.org.br",
        "context": ""
    },
    # Seção 2 - Objeto
    {
        "id": "tipo_atividade",
        "section": "2.1",
        "question": "Qual tipo de atividade será realizada?",
        "type": "select",
        "required": True,
        "options": ["Curso", "Oficina", "Seminário", "Simpósio", "Evento", "Digitalização de acervo"],
        "context": "Selecione o tipo que melhor descreve seu projeto cultural"
    },
    {
        "id": "tema_atividade",
        "section": "2.1",
        "question": "Qual o tema da atividade?",
        "type": "text",
        "required": True,
        "placeholder": "Ex: Maracatu, Cultura Popular, Artesanato, etc.",
        "context": ""
    },
    {
        "id": "cidade_execucao",
        "section": "2.1",
        "question": "Qual a cidade de execução?",
        "type": "text",
        "required": True,
        "placeholder": "Ex: São Paulo - SP",
        "context": ""
    },
    # Seção 3 - Justificativa
    {
        "id": "motivos_origem",
        "section": "3.1",
        "question": "Descreva os motivos que originaram o projeto:",
        "type": "textarea",
        "required": True,
        "placeholder": "Descreva de forma objetiva os motivos, com dados históricos se possível",
        "context": "Explique a necessidade e relevância do projeto"
    },
    {
        "id": "realidade_regional",
        "section": "3.2",
        "question": "Descreva a realidade regional onde será executado o projeto:",
        "type": "textarea",
        "required": True,
        "placeholder": "Contexto cultural, social e econômico da região",
        "context": "Demonstre a relação entre a realidade local e as ações propostas"
    },
    {
        "id": "local_execucao",
        "section": "3.3",
        "question": "Descreva o local onde será executado o projeto:",
        "type": "textarea",
        "required": True,
        "placeholder": "Descrição física, capacidade, tipo de local (praça, auditório, sala, etc.)",
        "context": "Inclua informações sobre capacidade, localização e infraestrutura"
    },
    {
        "id": "aderencia_pnc",
        "section": "3.4",
        "question": "Quais metas do Plano Nacional de Cultura (PNC) o projeto atinge?",
        "type": "textarea",
        "required": True,
        "placeholder": "Liste as metas do PNC que o projeto visa atingir",
        "context": "Consulte o PNC para identificar as metas relevantes ao seu projeto"
    },
    {
        "id": "relacao_pronac",
        "section": "3.5",
        "question": "Qual a relação entre a proposta e os objetivos do PRONAC (Lei 8.313/91)?",
        "type": "textarea",
        "required": True,
        "placeholder": "Descreva como o projeto se relaciona com os objetivos do PRONAC",
        "context": "O PRONAC visa apoiar iniciativas que valorizem e difundam a cultura brasileira"
    },
    {
        "id": "efeitos_sociais",
        "section": "3.6",
        "question": "Quais os efeitos sociais do projeto na comunidade?",
        "type": "textarea",
        "required": True,
        "placeholder": "Impactos sociais esperados",
        "context": ""
    },
    {
        "id": "efeitos_culturais",
        "section": "3.6",
        "question": "Quais os efeitos culturais do projeto na comunidade?",
        "type": "textarea",
        "required": True,
        "placeholder": "Impactos culturais esperados",
        "context": ""
    },
    {
        "id": "efeitos_economicos",
        "section": "3.6",
        "question": "Quais os efeitos econômicos do projeto na comunidade?",
        "type": "textarea",
        "required": True,
        "placeholder": "Impactos econômicos esperados",
        "context": ""
    },
    {
        "id": "efeitos_ambientais",
        "section": "3.6",
        "question": "Quais os efeitos ambientais do projeto na comunidade?",
        "type": "textarea",
        "required": True,
        "placeholder": "Impactos ambientais esperados (se aplicável)",
        "context": ""
    },
    # Seção 4 - Público Beneficiário
    {
        "id": "grupos_beneficiarios",
        "section": "4.1",
        "question": "Quais grupos/segmentos socioculturais serão beneficiados? (Selecione todos que aplicam)",
        "type": "multiselect",
        "required": True,
        "options": [
            "Artistas e grupos artísticos",
            "Povos e comunidades indígenas",
            "Comunidades quilombolas",
            "Povos e comunidades tradicionais de matriz africana",
            "Povos e comunidades ciganos",
            "População rural",
            "Estudantes de instituições públicas de ensino",
            "Mulheres",
            "Pessoas com deficiência",
            "Pessoas em situação de rua",
            "LGBT",
            "Outros"
        ],
        "context": "Selecione todos os grupos que serão beneficiados pelo projeto"
    },
    {
        "id": "quantidade_beneficiarios",
        "section": "4.1",
        "question": "Qual a quantidade estimada de pessoas beneficiadas por cada grupo selecionado?",
        "type": "textarea",
        "required": True,
        "placeholder": "Ex: Artistas: 50, Estudantes: 100, Mulheres: 80",
        "context": "Informe a quantidade para cada grupo selecionado anteriormente"
    },
    {
        "id": "grupos_etarios",
        "section": "4.1",
        "question": "Quais grupos etários serão beneficiados?",
        "type": "multiselect",
        "required": True,
        "options": [
            "Crianças (0 a 11 anos)",
            "Adolescentes e Jovens (12 a 29 anos)",
            "Adultos (30 a 59 anos)",
            "Idosos (maior de 60 anos)"
        ],
        "context": "Selecione todas as faixas etárias que serão beneficiadas"
    }
]


def get_question_by_id(question_id):
    """Retorna uma pergunta pelo seu ID"""
    for q in QUESTIONS:
        if q["id"] == question_id:
            return q
    return None


def get_questions_by_section(section):
    """Retorna todas as perguntas de uma seção"""
    return [q for q in QUESTIONS if q["section"] == section]


def get_total_questions():
    """Retorna o número total de perguntas"""
    return len(QUESTIONS)


def get_section_from_index(index):
    """Retorna a seção baseada no índice da pergunta"""
    if index < len(QUESTIONS):
        return QUESTIONS[index]["section"]
    return ""
