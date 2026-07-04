# Goal Planner Page - lets users define financial goals and generate a personalized investment plan

import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


from src.tools.goal_planner_tools import calculate_goal_plan

# --- Custom CSS ---
st.markdown("""
<style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Form container */
    section[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    
    /* Metrics */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    div[data-testid="stMetric"] label {
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 3rem;
        font-size: 1.1rem;
        font-weight: 700;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
    }
    
    /* Success/Warning/Info boxes */
    .stSuccess, .stWarning, .stInfo {
        border-radius: 15px;
        padding: 1.5rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)


def render():
    # --- Header with icon ---
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='font-size: 3.5rem; margin-bottom: 0.5rem;'>🎯 Financial Goal Planner</h1>
        <p style='color: rgba(255,255,255,0.9); font-size: 1.3rem;'>Plan your financial future with AI-powered SIP calculations</p>
    </div>
    """, unsafe_allow_html=True)

    # --- Info cards ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📊 **Set Your Goal**\nDefine what you want to achieve")
    with col2:
        st.info("💰 **Calculate SIP**\nGet personalized monthly investment")
    with col3:
        st.info("🚀 **Track Progress**\nMonitor your journey to success")
    
    st.markdown("<br>", unsafe_allow_html=True)

    with st.form("goal_form"):
        st.markdown("### 📝 Goal Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            goal_type = st.selectbox(
                "🎯 Goal Type",
                [
                    "🏠 Buy a House",
                    "🌴 Retirement",
                    "🎓 Child Education",
                    "🚨 Emergency Fund",
                    "🚗 Dream Car",
                    "💎 Wealth Creation",
                    "✈️ Vacation",
                    "📌 Other"
                ]
            )

        with col2:
            if "Other" in goal_type:
                goal_name = st.text_input("Goal Name", placeholder="Enter custom goal name")
            else:
                goal_name = goal_type

        st.markdown("### 💵 Financial Parameters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            target_corpus = st.number_input(
                "💰 Target Corpus (₹)",
                min_value=10000,
                value=5000000,
                step=100000,
                help="Total amount you want to accumulate"
            )
            
            expected_return = st.number_input(
                "📈 Expected Annual Return (%)",
                min_value=1.0,
                max_value=25.0,
                value=12.0,
                step=0.5,
                help="Expected return from your investments"
            )

        with col2:
            timeline_years = st.number_input(
                "📅 Investment Duration (Years)",
                min_value=1,
                max_value=40,
                value=10,
                help="How many years until you need the money"
            )
            
            current_sip = st.number_input(
                "💳 Current Monthly SIP (Optional, ₹)",
                min_value=0,
                value=0,
                step=1000,
                help="Your existing monthly SIP amount, if any"
            )

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🚀 Generate Financial Plan")

    if submitted:
        with st.spinner("🧮 Calculating your personalized plan..."):
            result = calculate_goal_plan.invoke(
                {
                    "goal_amount": target_corpus,
                    "years": timeline_years,
                    "annual_return": expected_return
                }
            )

        if result["status"] == "error":
            st.error(f"❌ {result['message']}")
            return

        required_sip = result["monthly_sip"]

        # --- Success banner ---
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;'>
            <h2 style='color: white; margin: 0;'>🎉 Your Financial Plan is Ready!</h2>
        </div>
        """, unsafe_allow_html=True)

        # --- Key metrics ---
        st.markdown("### 📊 Goal Summary")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🎯 Goal",
                goal_name.replace("🏠 ", "").replace("🌴 ", "").replace("🎓 ", "").replace("🚨 ", "").replace("🚗 ", "").replace("💎 ", "").replace("✈️ ", "").replace("📌 ", "")
            )

        with col2:
            st.metric(
                "💰 Target Corpus",
                f"₹{target_corpus:,.0f}"
            )
            
        with col3:
            st.metric(
                "📅 Duration",
                f"{timeline_years} Years"
            )

        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- Required SIP (highlighted) ---
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
                    padding: 2rem; border-radius: 20px; text-align: center; border: 3px solid #667eea;'>
            <h3 style='color: #667eea; margin-bottom: 0.5rem;'>💵 Required Monthly SIP</h3>
            <h1 style='color: #764ba2; font-size: 3.5rem; margin: 0;'>₹{:,.2f}</h1>
            <p style='color: #667eea; margin-top: 0.5rem;'>📈 @ {}% annual return</p>
        </div>
        """.format(required_sip, expected_return), unsafe_allow_html=True)

        # --- Current SIP analysis ---
        if current_sip > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📊 Current Investment Analysis")

            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "Your Current SIP",
                    f"₹{current_sip:,.2f}"
                )
            
            with col2:
                sip_gap = required_sip - current_sip
                st.metric(
                    "Gap / Surplus",
                    f"₹{abs(sip_gap):,.2f}",
                    delta=f"{sip_gap:,.2f}",
                    delta_color="inverse"
                )

            if sip_gap > 0:
                st.warning(
                    f"⚠️ **Action Required:** Increase your monthly SIP by **₹{sip_gap:,.2f}** to achieve your goal on time."
                )
            else:
                st.success(
                    f"🎉 **Excellent Progress!** You're investing **₹{abs(sip_gap):,.2f}** more than required. You're on track!"
                )

        # --- AI Recommendation ---
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 💡 AI-Powered Recommendation")

        if current_sip == 0:
            st.info(
                f"""
**Investment Strategy for {goal_name}**

✅ **Target:** ₹{target_corpus:,.0f}  
✅ **Timeline:** {timeline_years} years  
✅ **Required Monthly SIP:** ₹{required_sip:,.2f}  
✅ **Expected Return:** {expected_return}% annually  

**Next Steps:**
1. Start a monthly SIP of ₹{required_sip:,.2f}
2. Choose diversified equity mutual funds for long-term goals
3. Review your portfolio every 6 months
4. Stay invested through market volatility

⚠️ *Disclaimer: Market returns are not guaranteed. Adjust your plan as needed.*
"""
            )

        elif current_sip >= required_sip:
            st.success(
                f"""
**🎉 You're on the Right Track!**

Your current SIP of **₹{current_sip:,.2f}** is sufficient to reach your goal of **₹{target_corpus:,.0f}**.

**Keep it up by:**
- Continuing your SIP consistently
- Reviewing your portfolio quarterly
- Rebalancing when necessary
- Staying disciplined during market downturns
"""
            )

        else:
            additional = required_sip - current_sip
            st.warning(
                f"""
**⚠️ Investment Gap Detected**

Current SIP: **₹{current_sip:,.2f}**  
Required SIP: **₹{required_sip:,.2f}**  
Shortfall: **₹{additional:,.2f}/month**

**Options to bridge the gap:**
1. ✅ Increase monthly SIP by ₹{additional:,.2f}
2. 📅 Extend investment duration by a few years
3. 📈 Opt for higher-return asset classes (higher risk)
4. 💰 Make a lump-sum investment to reduce monthly burden
"""
            )

        # --- Disclaimer ---
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style='background-color: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; text-align: center;'>
            <small style='color: rgba(255,255,255,0.8);'>
            ⚠️ This is an educational tool. Consult a licensed financial advisor before making investment decisions.
            </small>
        </div>
        """, unsafe_allow_html=True)


render()