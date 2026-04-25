"""
Aplicação Streamlit - Assistente de Planejamento de Projetos Culturais
"""

import streamlit as st
from datetime import datetime
from questions import QUESTIONS, get_section_from_index
from template import generate_markdown, get_empty_responses


# Configuração da página
st.set_page_config(
    page_title="Assistente de Planejamento de Projetos",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para estilo gov.br
st.markdown("""
<style>
    .stApp {
        background-color: #f5f5f5;
        color: #333333;
    }
    .header {
        background: linear-gradient(135deg, #009c3b 0%, #0055a4 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    .header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    .question-box {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        color: #333333;
    }
    .section-title {
        color: #0055a4;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .progress-bar {
        background-color: #e0e0e0;
        border-radius: 10px;
        padding: 0.5rem;
        margin-bottom: 2rem;
        color: #333333;
    }
    .stButton>button {
        background-color: #009c3b;
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #007a2e;
    }
    .preview-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        max-height: 80vh;
        overflow-y: auto;
        color: #333333;
    }
    .preview-title {
        color: #0055a4;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #ffbd00;
    }
    /* Fix for markdown content visibility */
    .stMarkdown {
        color: #333333;
    }
    .stMarkdown strong {
        color: #333333;
    }
    /* Ensure all text is readable */
    p, label, div, span {
        color: #333333;
    }
    /* Input fields */
    input[type="text"], textarea {
        color: #333333;
    }
    /* Sidebar content - white text on dark background */
    [data-testid="stSidebar"] {
        color: white !important;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: white !important;
    }
    /* Sidebar markdown content */
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] .stMarkdown strong {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Inicializa o estado da sessão"""
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'responses' not in st.session_state:
        st.session_state.responses = get_empty_responses()
    if 'completed' not in st.session_state:
        st.session_state.completed = False


def render_header():
    """Renderiza o cabeçalho"""
    st.markdown("""
    <div class="header">
        <h1>📋 Assistente de Planejamento de Projetos</h1>
        <p>Preenchimento assistido do documento PLANEJAMENTO DO PROJETO - MinC</p>
    </div>
    """, unsafe_allow_html=True)


def render_progress():
    """Renderiza a barra de progresso"""
    total = len(QUESTIONS)
    current = st.session_state.current_question
    progress = (current / total) * 100
    
    st.markdown(f"""
    <div class="progress-bar">
        <strong>Progresso:</strong> {current}/{total} perguntas ({progress:.1f}%)
    </div>
    """, unsafe_allow_html=True)
    
    st.progress(progress / 100)


def render_question(question):
    """Renderiza uma pergunta"""
    section = question["section"]
    question_text = question["question"]
    question_type = question["type"]
    required = question["required"]
    context = question.get("context", "")
    
    st.markdown(f"<div class='section-title'>Seção {section}</div>", unsafe_allow_html=True)
    
    if context:
        st.info(context)
    
    if required:
        question_text += " *"
    
    current_value = st.session_state.responses.get(question["id"], "")
    
    if question_type == "text":
        answer = st.text_input(
            question_text,
            value=current_value,
            placeholder=question.get("placeholder", ""),
            key=f"q_{question['id']}"
        )
    elif question_type == "textarea":
        answer = st.text_area(
            question_text,
            value=current_value,
            placeholder=question.get("placeholder", ""),
            key=f"q_{question['id']}",
            height=150
        )
    elif question_type == "select":
        options = question["options"]
        current_index = options.index(current_value) if current_value in options else 0
        answer = st.selectbox(
            question_text,
            options,
            index=current_index,
            key=f"q_{question['id']}"
        )
    elif question_type == "multiselect":
        options = question["options"]
        current_values = current_value.split(", ") if current_value else []
        selected = st.multiselect(
            question_text,
            options,
            default=current_values if all(v in options for v in current_values) else [],
            key=f"q_{question['id']}"
        )
        answer = ", ".join(selected)
    else:
        answer = st.text_input(question_text, value=current_value, key=f"q_{question['id']}")
    
    return answer


def render_navigation():
    """Renderiza botões de navegação"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("⬅️ Anterior"):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        st.write("")  # Espaçador
    
    with col3:
        if st.session_state.current_question < len(QUESTIONS) - 1:
            if st.button("Próxima ➡️"):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("✅ Finalizar"):
                st.session_state.completed = True
                st.session_state.responses["data_geracao"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                st.rerun()


def render_preview():
    """Renderiza o preview do documento na sidebar"""
    with st.sidebar:
        st.markdown("<div class='preview-title'>📄 Preview do Documento</div>", unsafe_allow_html=True)
        
        # Atualizar objeto do projeto com base nas respostas
        responses = st.session_state.responses.copy()
        
        # Construir objeto do projeto dinamicamente
        tipo_atividade = responses.get("tipo_atividade", "")
        tema_atividade = responses.get("tema_atividade", "")
        cidade_execucao = responses.get("cidade_execucao", "")
        
        if tipo_atividade and tema_atividade and cidade_execucao:
            responses["objeto_projeto"] = f"Realizar {tipo_atividade.lower()} de {tema_atividade} na cidade de {cidade_execucao}"
        
        # Construir tabela de público beneficiário
        grupos = responses.get("grupos_beneficiarios", "")
        quantidade = responses.get("quantidade_beneficiarios", "")
        etarios = responses.get("grupos_etarios", "")
        
        if grupos:
            table_rows = []
            for grupo in grupos.split(", "):
                table_rows.append(f"| {grupo} | {quantidade} | {etarios} |")
            
            if table_rows:
                responses["publico_beneficiario_tabela"] = (
                    "\n| Grupo / Segmento | Quantidade | Grupos Etários |\n"
                    "|-------------------|-------------|----------------|\n" +
                    "\n".join(table_rows)
                )
        
        # Tratar campo de assinatura
        assinatura = responses.get("assinatura_dirigente", "")
        if assinatura == "Não":
            responses["responsavel_assinatura"] = """
*Nota: Caso o dirigente não seja o responsável pela assinatura, preencher os dados do responsável conforme item 1.4 do documento original.*
"""
        else:
            responses["responsavel_assinatura"] = ""
        
        # Gerar markdown
        try:
            markdown_content = generate_markdown(responses)
            st.markdown(markdown_content)
        except:
            st.warning("Preencha mais campos para visualizar o documento completo")
        
        st.divider()
        
        if st.session_state.completed:
            st.success("🎉 Documento completo!")
            if st.button("📋 Copiar Markdown"):
                st.code(markdown_content, language="markdown")
        else:
            st.info("Continue respondendo as perguntas para completar o documento")


def render_completed():
    """Renderiza a tela de conclusão"""
    st.success("🎉 Parabéns! Você completou o preenchimento do PLANEJAMENTO DO PROJETO")
    
    st.markdown("---")
    
    responses = st.session_state.responses.copy()
    
    # Reconstruir objeto e tabela
    tipo_atividade = responses.get("tipo_atividade", "")
    tema_atividade = responses.get("tema_atividade", "")
    cidade_execucao = responses.get("cidade_execucao", "")
    
    if tipo_atividade and tema_atividade and cidade_execucao:
        responses["objeto_projeto"] = f"Realizar {tipo_atividade.lower()} de {tema_atividade} na cidade de {cidade_execucao}"
    
    grupos = responses.get("grupos_beneficiarios", "")
    quantidade = responses.get("quantidade_beneficiarios", "")
    etarios = responses.get("grupos_etarios", "")
    
    if grupos:
        table_rows = []
        for grupo in grupos.split(", "):
            table_rows.append(f"| {grupo} | {quantidade} | {etarios} |")
        
        if table_rows:
            responses["publico_beneficiario_tabela"] = (
                "\n| Grupo / Segmento | Quantidade | Grupos Etários |\n"
                "|-------------------|-------------|----------------|\n" +
                "\n".join(table_rows)
            )
    
    assinatura = responses.get("assinatura_dirigente", "")
    if assinatura == "Não":
        responses["responsavel_assinatura"] = """
*Nota: Caso o dirigente não seja o responsável pela assinatura, preencher os dados do responsável conforme item 1.4 do documento original.*
"""
    else:
        responses["responsavel_assinatura"] = ""
    
    markdown_content = generate_markdown(responses)
    
    st.markdown(markdown_content)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Reiniciar"):
            st.session_state.current_question = 0
            st.session_state.responses = get_empty_responses()
            st.session_state.completed = False
            st.rerun()
    
    with col2:
        if st.button("📋 Copiar Markdown"):
            st.code(markdown_content, language="markdown")


def main():
    """Função principal"""
    initialize_session_state()
    render_header()
    
    if st.session_state.completed:
        render_completed()
    else:
        render_progress()
        
        current_index = st.session_state.current_question
        question = QUESTIONS[current_index]
        
        st.markdown("<div class='question-box'>", unsafe_allow_html=True)
        answer = render_question(question)
        st.session_state.responses[question["id"]] = answer
        st.markdown("</div>", unsafe_allow_html=True)
        
        render_navigation()
        
        # Atualizar preview
        render_preview()


if __name__ == "__main__":
    main()
