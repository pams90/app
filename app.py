import streamlit as st
import random
from datetime import datetime

# Configure page with enhanced constraints
st.set_page_config(
    page_title="Garage Startup Generator",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS for low-resource mindset
st.markdown("""
<style>
.lean-card {
    padding: 15px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    margin: 10px 0;
    background: #f8f9fa;
}
.constraint-badge {
    color: #28a745;
    font-size: 0.8em;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# Curated list of 100% implementable ideas with free tech stack
IDEAS = {
    "Privacy Tools": [
        ("Local AI Email Assistant", "Python, Transformers.js, IndexedDB",
         "Browser-based email composer with GPT-2 quality suggestions that never leaves your device",
         "Freemium: $5/mo for advanced templates"),
        
        ("Decentralized File Sharing", "WebRTC, WebTorrent, React",
         "Peer-to-peer file transfer without central servers using browser-to-browser connections",
         "Pay-What-You-Want model")
    ],
    
    "Productivity Boosters": [
        ("Contextual Clipboard Manager", "Rust, Tauri, SQLite",
         "Lightweight clipboard history with semantic search (runs locally)",
         "Donation-based with sponsorware features"),
        
        ("Auto-Documentation Generator", "Tree-sitter, Markdown, Go",
         "CLI tool that creates docs from code comments and git history",
         "OSS with enterprise support")
    ],
    
    "Niche Utilities": [
        ("Accessibility Stream Deck", "ESP32, WebSerial, WASM",
         "DIY hardware controller for common accessibility shortcuts",
         "Hardware kits + free firmware"),
        
        ("Bandwidth Optimizer", "PWA, Service Workers, Cloudflare Workers",
         "Automatic network throttling for background tabs",
         "Browser extension with premium rulesets")
    ]
}

def generate_lean_startup():
    """Generate validated ideas with implementation blueprint"""
    category = random.choice(list(IDEAS.keys()))
    idea = random.choice(IDEAS[category])
    
    return {
        "name": idea[0],
        "stack": idea[1],
        "description": idea[2],
        "monetization": idea[3],
        "validation": {
            "existing_alternatives": random.choice(["None", "1-2 partial solutions"]),
            "dev_time": f"{random.randint(1,6)} weekends",
            "hosting": random.choice(["GitHub Pages", "Cloudflare Workers", "Local First"]),
            "differentiator": random.choice([
                "Zero runtime costs",
                "No account required",
                "Offline functionality",
                "Privacy by design"
            ])
        }
    }

def display_idea(idea):
    """Show idea with implementation constraints"""
    with st.container():
        st.markdown(f"""
        <div class="lean-card">
            <div class="constraint-badge">🛠️ {idea['validation']['dev_time']} | 🖥️ {idea['validation']['hosting']}</div>
            <h4>{idea['name']}</h4>
            <p><strong>{idea['description']}</strong></p>
            <div style="font-size:0.9em">
            📦 Stack: {idea['stack']}<br>
            💰 Model: {idea['monetization']}<br>
            🚫 Competition: {idea['validation']['existing_alternatives']}<br>
            🔑 Key: {idea['validation']['differentiator']}
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.title("🚀 Garage Startup Generator")
    st.markdown("""
    **Generates bootstrappable app ideas with:**
    - $0 development/hosting costs
    - 100% solo-developer implementable
    - Built with open-source tools
    - Clear monetization path
    """)
    
    if st.button("Generate Implementable Idea"):
        idea = generate_lean_startup()
        display_idea(idea)
        st.caption(f"Generated at {datetime.now().strftime('%H:%M:%S')} · Refresh for new ideas")

if __name__ == "__main__":
    main()
