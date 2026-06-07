# Goal Planner Page - lets users define financial goals and get an AI-driven plan
import streamlit as st


def render():
    st.header("🎯 Financial Goal Planner")

    with st.form("goal_form"):
        goal = st.text_input("What is your financial goal?", "Save $50,000 for a house")
        timeline_years = st.number_input("Timeline (years)", min_value=1, max_value=40, value=5)
        monthly_savings = st.number_input("Monthly savings capacity ($)", min_value=0, value=500)
        submitted = st.form_submit_button("Generate Plan")

    if submitted:
        # TODO: invoke GoalPlannerAgent with form inputs
        st.info("Goal plan coming soon.")


render()
