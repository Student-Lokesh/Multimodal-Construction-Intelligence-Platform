import streamlit as st
import google.generativeai as genai
from PIL import Image
import requests
import json

# Page Config
st.set_page_config(page_title="Multimodal Construction Intelligence", layout="wide")
st.title("🏗️ Multimodal Construction Intelligence Platform")

# Sidebar - Configuration
st.sidebar.header("⚙️ Configuration")
api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("API Key Loaded Successfully!")
else:
    st.sidebar.warning("Running in Demo Mode. Please enter your Gemini API Key to enable AI features.")

# Create Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🛡️ Site Safety & PPE Audit", 
    "🔍 Crack Diagnostics", 
    "💰 Planning & Valuation", 
    "🌦️ Daily Site Assistant"
])

# --- TAB 1: Site Safety & PPE Audit (Epic 2) ---
with tab1:
    st.header("Site Safety & PPE Compliance Audit")
    ppe_image = st.file_uploader("Upload Construction Site Photo (JPG/PNG)", type=['jpg', 'jpeg', 'png'], key="ppe")
    
    if ppe_image is not None:
        img = Image.open(ppe_image)
        st.image(img, caption="Uploaded Site Photo", use_container_width=True)
        
        if st.button("Analyze PPE Compliance"):
            if api_key:
                with st.spinner("Analyzing site safety..."):
                    prompt = """Analyze this construction site photo for PPE compliance (helmets, high-vis vests, steel-toe boots, safety harnesses) under OSHA and IS 456 standards. 
                    Return ONLY a structured JSON containing: 
                    {"safety_score": 0-100, "overall_status": "Status", "ppe_detection": ["items"], "hazards": [{"hazard": "name", "severity": "Low/Medium/High/Critical", "remedy": "action"}]}"""
                    response = model.generate_content([prompt, img])
                    st.write(response.text)
            else:
                st.info("DEMO OUTPUT: Please enter API key for real analysis.")
                st.json({
                    "safety_score": 65,
                    "overall_status": "Needs Improvement",
                    "ppe_detection": ["Yellow Helmet", "High-Vis Vest"],
                    "hazards": [
                        {"hazard": "Missing Safety Harness on scaffold", "severity": "Critical", "remedy": "Stop work and provide harness immediately."}
                    ]
                })

# --- TAB 2: Crack Diagnostics (Epic 2) ---
with tab2:
    st.header("Crack Diagnostics & Structural Integrity")
    crack_image = st.file_uploader("Upload Concrete/Wall Surface Photo", type=['jpg', 'jpeg', 'png'], key="crack")
    
    if crack_image is not None:
        img2 = Image.open(crack_image)
        st.image(img2, caption="Uploaded Surface Photo", use_container_width=True)
        
        if st.button("Run Diagnostics"):
            if api_key:
                with st.spinner("Diagnosing structural integrity..."):
                    prompt = "Classify this concrete defect type (Hairline, Settlement, Structural Shear, Thermal Expansion, Spalling). Estimate crack width (mm), root causes, recommended engineering repairs, and urgency."
                    response = model.generate_content([prompt, img2])
                    st.write(response.text)
            else:
                st.info("DEMO OUTPUT: Please enter API key for real analysis.")
                st.write("**Defect Type:** Structural Shear Crack\n\n**Estimated Width:** ~4mm\n\n**Urgency:** High\n\n**Recommended Repair:** Structural re-grouting and epoxy injection.")

# --- TAB 3: Planning & Valuation (Epic 3) ---
with tab3:
    st.header("Planning & Real Estate Valuation")
    
    col1, col2 = st.columns(2)
    with col1:
        structure_type = st.selectbox("Structure Type", ["Residential", "Commercial", "Industrial"])
        sqft = st.number_input("Built-up Area (Sq.Ft)", min_value=500, value=1500)
    with col2:
        tier = st.selectbox("Location Tier", ["Tier 1 (Metro)", "Tier 2", "Tier 3"])
        completion = st.slider("Project Completion %", 0, 100, 45)
        
    if st.button("Calculate Valuation"):
        # Cost Calculation Logic
        base_rate = 2500 if tier == "Tier 1 (Metro)" else (2000 if tier == "Tier 2" else 1500)
        total_budget = sqft * base_rate
        capex = total_budget * (completion / 100)
        
        st.subheader("Financial Dashboard")
        st.metric(label="Total Estimated Budget", value=f"₹ {total_budget:,.2f}")
        st.metric(label="Capital Expenditure (CAPEX) Incurred", value=f"₹ {capex:,.2f}")
        
        st.subheader("Architectural Conceptualization")
        # Pollinations AI integration for 3D Render
        image_url = f"https://image.pollinations.ai/prompt/3D%20architectural%20render%20of%20modern%20{structure_type}%20building%20in%20India?width=800&height=400"
        st.image(image_url, caption=f"AI Generated 3D Concept: {structure_type}")

# --- TAB 4: Daily Site Assistant & Weather Advisory (Epic 5) ---
with tab4:
    st.header("Daily Site Assistant & Weather Advisory")
    weather = st.selectbox("Current Weather Condition", ["Normal", "High Wind", "Heavy Rain", "Extreme Heat"])
    
    if weather == "High Wind":
        st.error("🚨 ALERT: Suspend crane operations immediately. Secure loose materials.")
    elif weather == "Heavy Rain":
        st.warning("⚠️ ALERT: Cover fresh concrete. Check drainage systems for waterlogging.")
    elif weather == "Extreme Heat":
        st.warning("☀️ ALERT: Implement concrete curing protocols. Mandate water breaks for workers.")
    else:
        st.success("✅ Weather normal. Proceed with standard operations.")
        
    st.subheader("Construction Engineering Assistant")
    user_q = st.text_input("Ask a technical question regarding the site:")
    if user_q:
        if api_key:
            with st.spinner("Assistant is typing..."):
                response = model.generate_content(f"You are a construction engineering assistant. Answer this query: {user_q}")
                st.write(response.text)
        else:
            st.write("🤖 **Assistant (Demo):** Please connect your API key to get real-time engineering advice.")