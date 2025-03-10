# Import necessary libraries
import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="App Idea Generator",
    page_icon="💡",
    layout="centered"
)

# Define application components (same as before)
CATEGORIES = [
    "Health & Fitness",
    "Education",
    "Finance",
    "Social Media",
    "Productivity",
    "Travel",
    "Food & Cooking",
    "Gaming",
    "E-commerce",
    "Sustainability"
]

TARGET_AUDIENCE = [
    "Students",
    "Professionals",
    "Parents",
    "Seniors",
    "Teachers",
    "Entrepreneurs",
    "Fitness Enthusiasts",
    "Travelers",
    "Gamers",
    "Local Communities"
]

FEATURES = [
    "AI-powered recommendations",
    "Social sharing",
    "Augmented Reality",
    "Real-time collaboration",
    "Gamification elements",
    "Personalized dashboard",
    "Location-based services",
    "Voice commands",
    "Offline functionality",
    "Blockchain integration"
]

def generate_idea():
    """Generate a random app idea (same as before)"""
    category = random.choice(CATEGORIES)
    audience = random.choice(TARGET_AUDIENCE)
    feature = random.choice(FEATURES)
    return f"Create a {category} app for {audience} with {feature}"

# Streamlit UI Components
def main():
    # Add header and description
    st.title("💡 App Idea Generator")
    st.markdown("""
    Generate custom application ideas for your next project!
    Simply choose how many ideas you want and click the button.
    """)
    
    # Create input controls
    num_ideas = st.number_input(
        "Number of ideas to generate",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )
    
    # Generate button
    if st.button("Generate Ideas 💡"):
        st.subheader("Generated Ideas:")
        for i in range(num_ideas):
            st.success(f"{i+1}. {generate_idea()}")

if __name__ == "__main__":
    main()