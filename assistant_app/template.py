"""
Template Markdown para geração do documento PLANEJAMENTO DO PROJETO
"""

def generate_markdown(responses):
    """Gera o documento Markdown completo baseado nas respostas do usuário"""
    
    md = """**PLANEJAMENTO DO PROJETO**  
*Documento gerado pelo Assistente de Planejamento de Projetos Culturais*

---

## 1 - Identificação do projeto e do proponente

### 1.1 Informações sobre o Projeto

**Nº da Proposta na Plataforma Transferegov.br:** {numero_proposta}

**Título do projeto:** {titulo_projeto}

### 1.2 Informações sobre o Proponente

**Nome:** {nome_proponente}

**CNPJ:** {cnpj_proponente}

**Endereço completo / CEP / Município - UF:** {endereco_proponente}

**Contato telefônico:** {telefone_proponente}

**E-mail:** {email_proponente}

**Site:** {site_proponente}

### 1.3 Informações sobre o Dirigente Responsável

**Nome:** {nome_dirigente}

**Cargo/Função:** {cargo_dirigente}

**CPF:** {cpf_dirigente}

**RG:** {rg_dirigente}

**Endereço residencial / CEP / Município - UF:** {endereco_dirigente}

**Contato telefônico:** {telefone_dirigente}

**E-mail:** {email_dirigente}

### 1.4 Assinatura do Termo de Fomento

**O dirigente da entidade é o responsável por assinar o Termo de Fomento?** {assinatura_dirigente}

{responsavel_assinatura}

### 1.5 Responsável Técnico pelo Projeto

**Nome:** {nome_responsavel_tecnico}

**Cargo/Função:** {cargo_responsavel_tecnico}

**Contato telefônico:** {telefone_responsavel_tecnico}

**E-mail:** {email_responsavel_tecnico}

---

## 2 - Definição do objeto

### 2.1 Objeto do Projeto

{objeto_projeto}

---

## 3 - Complementação da Justificativa

### 3.1 Motivos de origem do projeto

{motivos_origem}

### 3.2 Realidade regional

{realidade_regional}

### 3.3 Local de execução

{local_execucao}

### 3.4 Aderência ao Plano Nacional de Cultura (PNC)

{aderencia_pnc}

### 3.5 Relação com o PRONAC (Lei nº 8.313/91)

{relacao_pronac}

### 3.6 Efeitos na comunidade local/regional

**Sociais:** {efeitos_sociais}

**Culturais:** {efeitos_culturais}

**Econômicos:** {efeitos_economicos}

**Ambientais:** {efeitos_ambientais}

---

## 4 - Detalhamento do Público beneficiário

### 4.1 Grupos/Segmentos socioculturais beneficiados

{publico_beneficiario_tabela}

---

*Documento gerado em {data_geracao}*
"""
    
    # Substituir as variáveis no template
    return md.format(**responses)


def get_empty_responses():
    """Retorna um dicionário com todas as chaves vazias"""
    return {
        "numero_proposta": "",
        "titulo_projeto": "",
        "nome_proponente": "",
        "cnpj_proponente": "",
        "endereco_proponente": "",
        "telefone_proponente": "",
        "email_proponente": "",
        "site_proponente": "",
        "nome_dirigente": "",
        "cargo_dirigente": "",
        "cpf_dirigente": "",
        "rg_dirigente": "",
        "endereco_dirigente": "",
        "telefone_dirigente": "",
        "email_dirigente": "",
        "assinatura_dirigente": "",
        "responsavel_assinatura": "",
        "nome_responsavel_tecnico": "",
        "cargo_responsavel_tecnico": "",
        "telefone_responsavel_tecnico": "",
        "email_responsavel_tecnico": "",
        "objeto_projeto": "",
        "motivos_origem": "",
        "realidade_regional": "",
        "local_execucao": "",
        "aderencia_pnc": "",
        "relacao_pronac": "",
        "efeitos_sociais": "",
        "efeitos_culturais": "",
        "efeitos_economicos": "",
        "efeitos_ambientais": "",
        "publico_beneficiario_tabela": "",
        "data_geracao": ""
    }
