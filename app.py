import streamlit as st
from openai import OpenAI
from openai.error import OpenAIError

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🏋️ Hybrid Training AI Bot")

cycles = st.number_input("How many 3-week cycles do you want?", min_value=1, max_value=6, value=1)
experience = st.selectbox("Your training experience:", ["Beginner", "Intermediate", "Advanced"])
goals = st.text_area("Your training goals:", "Build muscle and run a half marathon")

def generate_plan(prompt, model_name):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        st.warning(f"Model '{model_name}' failed with error: {e}")
        return None

if st.button("Generate Program"):
    with st.spinner("Generating your plan..."):
        prompt = f"""
You are a hybrid coach blending Max El-Hag, Nick DiMarco, and an elite running coach.
Create {cycles} training cycles (3 weeks each) based on experience '{experience}' and goals: {goals}.
Each week:
- Monday: Upper Strength + Gymnastics
- Tuesday: Lower Body Bodybuilding + Heavy Olympic Lifting
- Wednesday: VO2Max + Threshold Running
- Thursday: Zone 2 Cardio or Mobility
- Friday: Light Olympic Lifting + Gymnastics + Accessories
- Saturday: Easy Z2 Run or Rest
- Sunday: Z2 Run

Include progression using volume, intensity, density, and complexity for strength and gymnastics.
Return a clear, easy-to-follow weekly plan.
"""

        # Try models in order until one works
        for model in ["gpt-4o-16k", "gpt-4o", "gpt-3.5-turbo"]:
            result = generate_plan(prompt, model)
            if result:
                st.markdown(result)
                st.markdown("---")
                st.markdown("_Writ_
