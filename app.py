import streamlit as st

# 1. Page Configuration (Icons Removed)
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
    st.markdown("**Analyst:** [Your Name]") # Update this!
    st.markdown("**Institution:** Warwick Business School")
    st.markdown("**Focus:** Equity Research & M&A")
    st.markdown("---")
    
    # Macro Navigation: Switch between companies here
    page = st.radio("Coverage Universe", ["Home", "Constellation Energy (CEG)", "Macro Terminal"])

# 4. Page Routing & Micro Navigation (Tabs)

if page == "Home":
    st.title("Welcome to Nexus Alpha Research")
    st.markdown("### Institutional-Grade Analysis at the Intersection of Tech, Energy, and Macro.")
    st.markdown("---")
    st.markdown("""
    Welcome to my proprietary research portal. I built this platform from scratch in Python to host my financial models, equity research, and macro analytics. 
    
    **Coverage Universe:**
    * **Constellation Energy (US: CEG):** Initiation of Coverage focusing on the AI-Energy Nexus.
    * *(More coverage initiating soon...)*
    
    *Use the sidebar to select a company and view the interactive reports and financial models.*
    """)

elif page == "Constellation Energy (CEG)":
    st.title("Constellation Energy (US: CEG)")
    st.markdown("### Initiation of Coverage: The AI-Energy Nexus")
    st.markdown("---")
    
    # Micro Navigation: 4 Horizontal Tabs for the Company (Icons Removed)
    tab1, tab2, tab3, tab4 = st.tabs([
        "Investment Report", 
        "Financial Models", 
        "Valuation Scenarios", 
        "Risks & Catalysts"
    ])
    
    with tab1:
        st.subheader("Executive Summary")
        st.write("This tab will host the text and narrative of your 15-page initiation report. We can break it down into Investment Thesis, Industry Overview, etc.")
        
    with tab2:
        st.subheader("3-Statement Model & DCF")
        st.write("This tab will host your interactive data tables. We will use Pandas to display your historicals, projections, and terminal value calculations cleanly.")
        
    with tab3:
        st.subheader("Margin Expansion & BTM Economics")
        st.write("This tab will host interactive charts. We can plot the margin expansion scenarios driven by the Calpine natural gas acquisition here.")
        
    with tab4:
        st.subheader("FERC Transmission & Regulatory Risks")
        st.write("This tab will cover stress-testing of BTM data center economics and regulatory hurdles.")

elif page == "Macro Terminal":
    st.title("Macro & Markets Terminal")
    st.markdown("---")
    st.write("Global liquidity and API-driven dashboards will go here.")
