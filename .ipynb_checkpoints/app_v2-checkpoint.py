# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:59:14 2025

@author: Utilisateur
"""

import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from scipy import stats

def astronaut_simulation(num_applicants=18300, num_selected=200, luck_weight=0.05, num_simulations=1000, distribution='uniform', loc=85, scale=10):
    impact_of_luck_measures = []
    avg_luck_scores = []
    avg_top_skill_selected = []
    skill_weight = 1-luck_weight
    for _ in range(num_simulations):
        if distribution == 'uniform':
            skill_scores = np.random.randint(0, 101, num_applicants)
            luck_scores = np.random.randint(0, 101, num_applicants)
        elif distribution == 'normal':
            skill_scores = np.clip(np.random.normal(loc, scale, num_applicants), 0, 100).astype(int)
            luck_scores = np.clip(np.random.normal(loc, scale, num_applicants), 0, 100).astype(int)
        else:
            raise ValueError("Distribution must be either 'normal' or 'uniform'")
        overall_scores = (skill_weight * skill_scores) + (luck_weight * luck_scores)

        selected_indices = np.argsort(overall_scores)[::-1][:num_selected]
        top_skill_indices = np.argsort(skill_scores)[::-1][:num_selected]
        avg_luck_scores.append(np.mean(luck_scores[selected_indices]))
        top_skill_selected_count = len(set(selected_indices) & set(top_skill_indices))
        avg_top_skill_selected.append(top_skill_selected_count)
        impact_of_luck_measures.append(1 - top_skill_selected_count / num_selected)

    return avg_luck_scores, avg_top_skill_selected, impact_of_luck_measures

st.set_page_config(layout="wide")
st.title("The Luck Factor: How Much Does Chance Impact Success?")

# Sidebar for user inputs with tooltips
with st.sidebar:
    st.header("Simulation Parameters")
    num_applicants = st.number_input("Number of Applicants", min_value=100, max_value=10000, step=100, value=3000, help="Total number of applicants.")
    num_selected = st.number_input("Number Selected", min_value=1, max_value=num_applicants, step=1, value=10, help="Number of applicants selected.")
    luck_weight = st.slider("Luck Weight", min_value=0.0, max_value=1.0, step=0.01, value=0.05, help="Weight given to luck in the selection process.")
    num_simulations = st.number_input("Number of Simulations", min_value=100, max_value=10000, step=100, value=500, help="Number of simulation runs.")
    distribution = st.selectbox("Distribution", options=['uniform', 'normal'], help="Distribution of skill and luck scores.")
    if distribution == "normal":
        loc = st.number_input("Mean (loc)", min_value=0, max_value=100, value=85, help="Mean of the normal distribution.")
        scale = st.number_input("Standard Deviation (scale)", min_value=1, max_value=50, value=10, help="Standard deviation of the normal distribution.")
    else:
        loc = None
        scale = None
    col1, col2 = st.columns(2)
    with col1:
        run_simulation = st.button("Run Simulation")
    with col2:
        reset_simulation = st.button("Reset Parameters")


if reset_simulation:
    st.experimental_rerun()

if run_simulation:
    avg_luck_scores, avg_top_skill_selected, impact_of_luck = astronaut_simulation(
        num_applicants, num_selected, luck_weight, num_simulations, distribution, loc, scale
    )

    st.write("## Simulation Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Luck Score (Selected)", f"{np.mean(avg_luck_scores):.1f}", help="Average luck score of the selected applicants.")
    col2.metric("Average Top-Skilled Selected", f"{np.mean(avg_top_skill_selected):.1f} / {num_selected} ({np.mean(avg_top_skill_selected)/num_selected:.1%})", help="Average number of selected applicants who were also in the top based on skill alone (as a percentage of the total selected).")
    col3.metric("Average Impact of Luck", f"{np.mean(impact_of_luck):.2%}", help="Average percentage of selected applicants who were selected due to luck.")

    # Plotly Histograms
    fig1 = px.histogram(avg_luck_scores, title='Distribution of Average Luck Scores', labels={'value':'Average Luck Score'})
    fig2 = px.histogram(avg_top_skill_selected, title='Distribution of Top Skilled Selected', labels={'value':'Number of Top Skilled'})
    fig3 = px.histogram(impact_of_luck, title='Distribution of Impact of Luck', labels={'value':'Impact of Luck'})
    fig3.update_layout(yaxis_tickformat='.0%')

    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)

    luck_weights = np.linspace(0.0, 1.0, 21)
    results = []
    for weight in luck_weights:
        _, _, impact = astronaut_simulation(
            num_applicants, num_selected, weight, num_simulations, distribution, loc, scale
        )
        mean_impact = np.mean(impact)
        std_err = stats.sem(impact)
        confidence_interval = stats.t.interval(0.95, len(impact)-1, loc=mean_impact, scale=std_err)
        results.append({'Luck Weight': weight,
                        'Luck Impact': mean_impact,
                        'Lower bound': confidence_interval[0],
                        'Upper bound': confidence_interval[1]})

    df_results = pd.DataFrame(results)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_results['Luck Weight'], y=df_results['Luck Impact'], mode='lines+markers', name='Average Impact of Luck')) # Corrected name
    fig.add_trace(go.Scatter(x=df_results['Luck Weight'], y=df_results['Lower bound'], mode='lines', name='95% Confidence Interval', line=dict(dash='dash', color = "grey"))) # Combined names
    fig.add_trace(go.Scatter(x=df_results['Luck Weight'], y=df_results['Upper bound'], mode='lines', line=dict(dash='dash', color = "grey"), showlegend=False)) # Hide legend for duplicate trace
    fig.update_layout(title="Impact of Luck Weight on Astronaut Selection",
                      xaxis_title="Luck Weight", yaxis_title="Avg. Luck Impact", yaxis_tickformat='.0%')
    st.plotly_chart(fig, use_container_width=True)