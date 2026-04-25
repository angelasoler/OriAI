"""
Base de Conhecimento - Trechos chave da Cartilha Parlamentar e PNC
Usados para fornecer contexto e orientação durante o preenchimento do formulário
"""

KNOWLEDGE_BASE = {
    "cartilha_parlamentar": {
        "proponente": """
        O proponente deve ser uma Organização da Sociedade Civil (OSC) qualificada para receber recursos públicos.
        É necessário comprovar capacidade técnica e operacional para executar o projeto.
        """,
        "objeto": """
        O objeto do projeto deve estar alinhado com as políticas públicas do Ministério da Cultura.
        Deve ser claro, específico e mensurável, permitindo avaliação de resultados.
        """,
        "justificativa": """
        A justificativa deve demonstrar a relevância cultural e social do projeto.
        Deve incluir dados sobre a realidade local e a necessidade da intervenção proposta.
        """,
        "publico_beneficiario": """
        O público beneficiário deve ser quantificado e caracterizado por segmentos socioculturais.
        É importante indicar os grupos etários que serão atingidos.
        """
    },
    "pnc": {
        "metas_principais": """
        O Plano Nacional de Cultura (PNC) estabelece metas estratégicas para o desenvolvimento cultural do Brasil.
        Principais eixos: Produção, Difusão, Formação, Intercâmbio, Pesquisa, Preservação.
        """,
        "acessibilidade": """
        Todo projeto cultural deve incluir ações de acessibilidade para pessoas com deficiência.
        Acessibilidade física, comunicacional e atitudinal são obrigatórias (Lei 13.146/2015).
        """
    },
    "objetos_validos": {
        "curso": "Curso de capacitação ou formação em área cultural específica",
        "oficina": "Oficina prática para desenvolvimento de habilidades artísticas ou culturais",
        "seminario": "Seminário para debate e reflexão sobre temas culturais",
        "simposio": "Simpósio para apresentação e discussão de trabalhos culturais",
        "evento": "Evento cultural (festejo, atividade popular tradicional)",
        "digitalizacao": "Digitalização e disponibilização de acervo cultural em meio público"
    },
    "cultura_popular": """
    Manifestações da Cultura Popular Brasileira: Frevo, Maracatu, Fandango, Baião, Jongo, Carimbó, 
    Cordel, Bumba Meu Boi, Samba, Congado, Dança Do Coco, Folia de Reis, Lambada, Xaxado, Catira, 
    Ciranda, Maculelê, Forró, Artesanato, Capoeira, Cavalhada, Quadrilhas Juninas, Indígena, Cigano, etc.
    """,
    "grupos_etarios": {
        "criancas": "0 a 11 anos",
        "adolescentes_jovens": "12 a 29 anos",
        "adultos": "30 a 59 anos",
        "idosos": "Maior de 60 anos"
    }
}

def get_context(section):
    """Retorna contexto relevante para uma seção específica"""
    if section in KNOWLEDGE_BASE["cartilha_parlamentar"]:
        return KNOWLEDGE_BASE["cartilha_parlamentar"][section]
    elif section in KNOWLEDGE_BASE["pnc"]:
        return KNOWLEDGE_BASE["pnc"][section]
    return ""

def get_object_description(obj_type):
    """Retorna descrição de um tipo de objeto válido"""
    return KNOWLEDLEDGE_BASE["objetos_validos"].get(obj_type, "")

def get_cultura_popular_examples():
    """Retorna exemplos de cultura popular brasileira"""
    return KNOWLEDLEDGE_BASE["cultura_popular"]
