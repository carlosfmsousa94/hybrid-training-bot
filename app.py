import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🏋️ Hybrid Training AI Bot")

cycles = st.number_input("How many 3-week cycles do you want?", min_value=1, max_value=6, value=1)
experience = st.selectbox("Your training experience:", ["Beginner", "Intermediate", "Advanced"])
goals = st.text_area("Your training goals:", "Build muscle and run a half marathon")

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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role":"user","content":prompt}],
            temperature=0.7,
            max_tokens=3200
        )
        st.markdown(response.choices[0].message.content)
        st.markdown("---")
        st.markdown("_Written by Carlos Sousa, AI_")
