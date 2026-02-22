import streamlit as st
from src.models import Team, TeamMember
from src.graph import build_graph
from src.visualization import visualize_results

st.title("AI Project Manager Agent")
st.subheader("Configure your project below and run the agent.")

# --- Project Description ---
project_description = st.text_area(
    "Project Description",
    value="Create a secure, multi-user AI dashboard using LangGraph and React."
)

# --- Settings ---
st.subheader("Settings")
max_iteration = st.slider("Max Iterations", min_value=1, max_value=5, value=2)
risk_threshold = st.slider("Risk Threshold", min_value=5, max_value=50, value=15)

# --- Team Members ---
SENIORITY_OPTIONS = ["Junior", "Mid", "Senior"]
SKILL_OPTIONS = ["Python", "React", "UI/UX", "Testing", "Architecture", "LangGraph", "Database", "DevOps"]

num_members = st.slider("Number of Team Members", min_value=1, max_value=8, value=3)
team_members = []

for i in range(num_members):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        name = st.text_input(f"Name {i+1}", key=f"name_{i}")
    with col2:
        role = st.selectbox(f"Role {i+1}", ["Developer", "Designer", "QA", "Lead", "DevOps"], key=f"role_{i}")
    with col3:
        skills = st.multiselect(f"Skills {i+1}", SKILL_OPTIONS, key=f"skills_{i}")
    with col4:
        seniority = st.selectbox(f"Seniority {i+1}", SENIORITY_OPTIONS, key=f"seniority_{i}")

    if name:
        team_members.append(TeamMember(name=name, role=role, skills=skills, seniority=seniority))

# --- Run Agent ---
if st.button("Run AI Project Manager"):
    team = Team(team_members=team_members)
    graph = build_graph()
    results = graph.invoke(
        {
            "project_description": project_description,
            "team": team,
            "max_iteration": max_iteration,
            "risk_threshold": risk_threshold,
            "iteration_number": 0,
            "insights": [],
            "project_risk_score_iterations": []
        },
        {"configurable": {"thread_id": "streamlit_session"}}
    )
    visualize_results(results)
