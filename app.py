import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Nexus Alpha Research",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Institutional Dark Mode CSS with Typography Hierarchy
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    [data-testid="stSidebar"] { background-color: #1E2127; }
    
    /* Global Typography: Muted grey for paragraphs to reduce eye strain */
    p, li, span { font-family: 'Helvetica Neue', sans-serif; color: #D1D5DB !important; font-size: 15px; line-height: 1.6; }
    
    /* Main Title (H1): Restored original Streamlit size, kept subtle underline */
    h1 { font-family: 'Helvetica Neue', sans-serif; font-weight: 600; border-bottom: 1px solid #333; padding-bottom: 0.5rem; margin-bottom: 1rem; color: #FAFAFA !important;}
    
    /* Sub-title (H2): Muted, no underline */
    h2 { font-family: 'Helvetica Neue', sans-serif; font-weight: 400; color: #A0AEC0 !important; margin-bottom: 2rem;}
    
    /* Section Headers (H3): Uppercase, wide spacing, terminal-green underline pulled tighter to text */
    h3 { 
        font-family: 'Helvetica Neue', sans-serif; 
        font-weight: 600; 
        font-size: 1.05rem; 
        text-transform: uppercase; 
        letter-spacing: 1.5px; 
        border-bottom: 2px solid #00E676; 
        padding-bottom: 2px; /* Tightened from 5px to 2px */
        color: #FAFAFA !important; 
        display: inline-block; 
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    hr { border-top: 1px solid #333; }
    
    /* Sidebar Text Spacing */
    [data-testid="stSidebar"] p { font-size: 14px; margin-bottom: 0.5rem; }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: transparent; border-radius: 4px; color: #FAFAFA; font-size: 16px; font-weight: 400;}
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #00E676; color: #00E676 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration & Macro Navigation
with st.sidebar:
    st.title("Nexus Alpha")
    st.markdown("### Proprietary Research")
    st.markdown("---")
    
    st.markdown("**Analysts**<br>Aditya Pandey<br>Ved Krishnagiri", unsafe_allow_html=True)
    st.markdown("<br>**Institution**<br>Warwick Business School", unsafe_allow_html=True)
    st.markdown("<br>**Focus**<br>Equity Research & M&A", unsafe_allow_html=True)
    st.markdown("---")
    
    page = st.radio("Coverage Universe", ["Home", "Constellation Energy (CEG)"])

# 4. Page Routing & Micro Navigation (Tabs)

if page == "Home":
    st.title("Welcome to Nexus Alpha Research")
    st.header("Institutional-Grade Analysis on Energy and AI Infrastructure Markets.")
    
    st.markdown("""
    Nexus Alpha Research is an independent equity research terminal developed by Aditya Pandey and Ved Krishnagiri. 
    
    As Finance undergraduates at Warwick Business School, we recognized that static reports are no longer sufficient for modern market analysis. We engineered this platform from the ground up in Python to host our live financial models, dynamic valuation frameworks, and proprietary investment theses.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### Platform Architecture")
        st.markdown("""
        This portal serves as a transparent, continuously updated ledger of our research. It bridges the gap between traditional fundamental analysis and programmatic data visualization. 
        
        By utilizing a Python-backed infrastructure, we bypass the limitations of traditional PDFs to build a verifiable, interactive track record in public markets.
        """)
        
    with col2:
        st.markdown("### Our Sector Mandate")
        st.markdown("""
        We deliberately concentrate our coverage on Energy and AI Infrastructure, viewing them as the twin pillars driving the next decade of capital allocation:
        * **Energy & Macroeconomics:** Energy markets serve as the ultimate barometer for global macroeconomic cycles and geopolitical friction. 
        * **AI Infrastructure:** The physical build-out of artificial intelligence represents the most consequential secular growth trend of our generation. 
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("### Coverage Universe")
        st.markdown("""
        * **Constellation Energy (US: CEG):** Initiation of Coverage focusing on the AI-Energy Nexus, BTM data center economics, and margin expansion.
        * *(Further coverage initiating soon...)*
        """)

elif page == "Constellation Energy (CEG)":
    st.title("Constellation Energy (US: CEG)")
    st.header("Initiation of Coverage: The AI-Energy Nexus")
    
    tab1, tab2, tab3 = st.tabs([
        "Investment Reports", 
        "Financial Models", 
        "Two-Pager"
    ])
    
    with tab1:
        st.markdown("### Investment Reports")
        st.write("This section will host your comprehensive 15-page initiation report, covering the investment thesis, industry overview, and margin expansion scenarios.")
        
    with tab2:
        st.markdown("### Financial Models")
        st.write("This section will host your 3-statement model and DCF valuation. We will use Pandas to render institutional-grade data tables.")
        
    with tab3:
        st.markdown("### Two-Pager")
        st.write("This section will host the condensed tear sheet summarizing the core thesis, valuation matrix, and critical catalysts.")
