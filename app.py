import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Nexus Alpha Research",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Institutional Dark Mode CSS
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    [data-testid="stSidebar"] { background-color: #1E2127; }
    h1, h2, h3, p, li, span { font-family: 'Helvetica Neue', sans-serif; color: #FAFAFA !important; }
    h1, h2, h3 { font-weight: 300; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    hr { border-top: 1px solid #333; }
    /* Style the horizontal tabs to look sleek */
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
    st.markdown("**Analysts:** Aditya Pandey; Ved Krishnagiri") 
    st.markdown("**Institution:** Warwick Business School")
    st.markdown("**Focus:** Equity Research")
    st.markdown("---")
    
    # Macro Navigation: Macro Terminal removed
    page = st.radio("Coverage Universe", ["Home", "Constellation Energy (CEG)"])

# 4. Page Routing & Micro Navigation (Tabs)

if page == "Home":
    st.title("Welcome to Nexus Alpha Research")
    st.markdown("### Institutional-Grade Analysis on Energy and AI Infrastructure Markets.")
    st.markdown("---")
    
    st.markdown("""
    Nexus Alpha Research is an independent equity research terminal developed by Aditya Pandey and Ved Krishnagiri. 
    
    As Finance undergraduates at Warwick Business School, we recognized that static reports are no longer sufficient for modern market analysis. We engineered this platform from the ground up in Python to host our live financial models, dynamic valuation frameworks, and proprietary investment theses.
    
    This portal serves as a transparent, continuously updated ledger of our research. It bridges the gap between traditional fundamental analysis and programmatic data visualization, allowing us to build a verifiable, long-term track record in public markets.
    
    **Coverage Universe:**
    * **Constellation Energy (US: CEG):** Initiation of Coverage focusing on the AI-Energy Nexus, BTM data center economics, and margin expansion.
    * *(Further coverage initiating soon...)*
    
    *Use the sidebar to navigate the platform and view our interactive reports and financial models.*
    """)

elif page == "Constellation Energy (CEG)":
    st.title("Constellation Energy (US: CEG)")
    st.markdown("### Initiation of Coverage: The AI-Energy Nexus")
    st.markdown("---")
    
    # Micro Navigation: 3 Horizontal Tabs
    tab1, tab2, tab3 = st.tabs([
        "Investment Reports", 
        "Financial Models", 
        "Two-Pager"
    ])
    
    with tab1:
        st.subheader("Investment Reports")
        st.write("This section will host your comprehensive 15-page initiation report, covering the investment thesis, industry overview, and margin expansion scenarios.")
        
    with tab2:
        st.subheader("Financial Models")
        st.write("This section will host your 3-statement model and DCF valuation. We will use Pandas to render institutional-grade data tables.")
        
    with tab3:
        st.subheader("Two-Pager")
        st.write("This section will host the condensed tear sheet summarizing the core thesis, valuation matrix, and critical catalysts.")
