# 🏗️ Multimodal Construction Intelligence Platform

## 📖 Overview
The **Multimodal Construction Intelligence Platform** is an AI-powered decision-support system designed for the construction and real estate industry. It leverages Generative AI (Google Gemini) to analyze site photos for PPE safety compliance, classify concrete cracks, estimate project costs, and provide weather-aware engineering advisories. 

This project is developed as **Capstone Project 1** for the NASSCOM FutureSkills Prime and SmartBridge Skill Wallet certification.

## ✨ Core Features
This platform is divided into four main intelligent modules:
1. **🛡️ Site Safety & PPE Audit:** Upload site photos to detect PPE compliance (helmets, vests) and identify critical hazards based on safety standards.
2. **🔍 Crack Diagnostics:** Analyze concrete/wall surface images to classify structural defects, estimate crack width, and recommend engineering repairs.
3. **💰 Planning & Valuation:** Calculate estimated project budgets and Capital Expenditure (CAPEX) based on structure type, location tier, and completion percentage. Includes an AI-generated 3D architectural concept.
4. **🌦️ Daily Site Assistant:** Get dynamic safety alerts based on weather conditions (High Wind, Heavy Rain, Extreme Heat) and interact with an AI-powered construction engineering chatbot.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Frontend/Framework:** Streamlit
* **AI Engine:** Google Gemini (1.5 Flash) via `google-generativeai`
* **Image Processing:** Pillow (PIL)
* **External APIs:** Pollinations AI (for 3D conceptual renders)

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/YourUsername/Your-Repository-Name.git](https://github.com/YourUsername/Your-Repository-Name.git)
cd Your-Repository-Name