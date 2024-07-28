from utils import plot_mean_age, create_card, calculate_mean_est, plot_corr, calculate_sum_est, plot_histogram
from globals import VERMELHO_NBA, AZUL_NBA, LARANJA_NBA
import plotly.offline as po
import streamlit as st
import pandas as pd
import numpy as np
import os


if __name__ == '__main__':
    st.title("⛹️ Dados por time e jogadores ⛹️")

    st.divider()

    df = pd.read_csv(os.path.join("data", "nba_data_v2.csv"))

    st.markdown("<h3 style='text-align: center;'>Selecione o intervalo das temporadas</h3>", unsafe_allow_html=True)
    start_year, end_year = st.select_slider(
        "",
        options=df['season'].unique().tolist(),
        value=(1996, 2022)
    )
    st.divider()

    df_filtered = df[(df['season'] >= start_year) & (df['season'] <= end_year)]

    teams_name = df_filtered['team_abbreviation'].unique().tolist()
    players_name = df_filtered['player_name'].unique().tolist()

    with st.container():
        col_1, col_2 = st.columns(2)

        with col_1:
            st.markdown("<p style='text-align: center;'>Selecione os times</p>", unsafe_allow_html=True)
            selected_teams = st.multiselect(
                label="",
                options=teams_name,
                default=None,
                help="Qual time você pretende analisar?"
            )

            if selected_teams:
                pass

        with col_2:
            st.markdown("<p style='text-align: center;'>Selecione os jogadores</p>", unsafe_allow_html=True)
            selected_players = st.multiselect(
                label="",
                options=players_name,
                default=None
            )


