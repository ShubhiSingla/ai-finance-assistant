# Goal Planner Page - lets users define financial goals and generate a personalized investment plan

import streamlit as st

from src.tools.goal_planner_tools import calculate_goal_plan


def render():

    st.header("🎯 Financial Goal Planner")

    with st.form("goal_form"):

        goal_type = st.selectbox(
            "Goal Type",
            [
                "Buy a House",
                "Retirement",
                "Child Education",
                "Emergency Fund",
                "Dream Car",
                "Wealth Creation",
                "Vacation",
                "Other"
            ]
        )

        if goal_type == "Other":
            goal_name = st.text_input("Goal Name")
        else:
            goal_name = goal_type

        target_corpus = st.number_input(
            "Target Corpus (₹)",
            min_value=10000,
            value=5000000,
            step=100000
        )

        timeline_years = st.number_input(
            "Investment Duration (Years)",
            min_value=1,
            max_value=40,
            value=10
        )

        expected_return = st.number_input(
            "Expected Annual Return (%)",
            min_value=1.0,
            max_value=25.0,
            value=12.0,
            step=0.5
        )

        current_sip = st.number_input(
            "Current Monthly SIP (Optional)",
            min_value=0,
            value=0,
            step=1000
        )

        submitted = st.form_submit_button("Generate Financial Plan")

    if submitted:

        result = calculate_goal_plan.invoke(
            {
                "goal_amount": target_corpus,
                "years": timeline_years,
                "annual_return": expected_return
            }
        )

        if result["status"] == "error":
            st.error(result["message"])
            return

        required_sip = result["monthly_sip"]

        st.success("🎉 Financial Plan Generated")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🎯 Goal",
                goal_name
            )

            st.metric(
                "💰 Target Corpus",
                f"₹{target_corpus:,.0f}"
            )

        with col2:
            st.metric(
                "📅 Investment Duration",
                f"{timeline_years} Years"
            )

            st.metric(
                "💵 Required Monthly SIP",
                f"₹{required_sip:,.2f}"
            )

        st.metric(
            "📈 Expected Annual Return",
            f"{expected_return}%"
        )

        if current_sip > 0:

            st.divider()

            st.subheader("Current Investment Analysis")

            st.metric(
                "Your Current Monthly SIP",
                f"₹{current_sip:,.2f}"
            )

            sip_gap = required_sip - current_sip

            if sip_gap > 0:

                st.warning(
                    f"You need to increase your monthly SIP by ₹{sip_gap:,.2f} to achieve your financial goal."
                )

            else:

                st.success(
                    f"Great! You are investing ₹{abs(sip_gap):,.2f} more than the required SIP. You are on track to achieve your goal."
                )

        st.divider()

        st.subheader("💡 AI Recommendation")

        if current_sip == 0:

            st.info(
                f"""
To achieve your goal of **₹{target_corpus:,.0f}** for **{goal_name}**
within **{timeline_years} years**, you should invest approximately
**₹{required_sip:,.2f} every month** assuming an expected annual return
of **{expected_return}%**.

Market returns are not guaranteed, so review your investment plan periodically.
"""
            )

        elif current_sip >= required_sip:

            st.success(
                f"""
Excellent! Based on your current SIP of **₹{current_sip:,.2f}**, you are on track to achieve your goal of **₹{target_corpus:,.0f}**.

Continue investing consistently and review your portfolio periodically.
"""
            )

        else:

            additional = required_sip - current_sip

            st.warning(
                f"""
You are currently investing **₹{current_sip:,.2f}** per month.

To achieve your target corpus of **₹{target_corpus:,.0f}**, you should increase your SIP by approximately **₹{additional:,.2f} per month**, or consider extending your investment duration.
"""
            )


render()