import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Nexus Alpha Research",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Brute-Force Institutional Dark Mode (All in one file)
st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background-color: #0E1117;
    }
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #1E2127;
    }
    /* Text formatting and colors */
    h1, h2, h3, p, li, span { 
        font-family: 'Helvetica Neue', sans-serif; 
        color: #FAFAFA !important;
    }
    /* Make headers look sleek */
    h1, h2, h3 { 
        font-weight: 300; 
    }
    /* Clean up the top padding */
    .block-container { 
        padding-top: 2rem; 
        padding-bottom: 2rem; 
    }
    /* Subtle divider line */
    hr { 
        border-top: 1px solid #333; 
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.title("Nexus Alpha")
    st.markdown("### Proprietary Research")
    st.markdown("---")
    st.markdown("**Analyst:** [Your Name]")
    st.markdown("**Institution:** Warwick Business School")
    st.markdown("**Focus:** Equity Research & M&A")

# 4. Main Landing Page Content
st.title("Welcome to Nexus Alpha Research")
st.markdown("### Institutional-Grade Analysis at the Intersection of Tech, Energy, and Macro.")
st.markdown("---")

st.markdown("""
Welcome to my proprietary research portal. I built this platform from scratch in Python to host my financial models, equity research, and macro analytics. 

**Featured Research:**
* **Constellation Energy (US: CEG):** An Initiation of Coverage focusing on the AI-Energy Nexus, BTM data center economics, and margin expansion.
* **Macro & Markets Terminal:** A fault-tolerant, API-driven dashboard tracking global liquidity.

*Use the sidebar to navigate the platform once reports are published.*
""")
