from globals import VERMELHO_NBA, AZUL_NBA, LARANJA_NBA
import plotly.offline as po
from utils import plot_top10_est
import streamlit as st
import pandas as pd
import numpy as np
import os


if __name__ == '__main__':
    st.set_page_config(page_title="NBA dashboard", page_icon=':basketball:')

    st.title("⛹️ Dados por time e jogadores ⛹️")

    st.divider()

    df = pd.read_csv(os.path.join("data", "nba_data_v2.csv"))
    disable_player_filter = True

    # Variaveis para dinamizar os anos extremos da base
    min_year = df['season'].min()
    max_year = df['season'].max()

    st.markdown("<h3 style='text-align: center;'>Selecione o intervalo das temporadas</h3>", unsafe_allow_html=True)
    start_year, end_year = st.select_slider(
        "",
        options=df['season'].unique().tolist(),
        value=(min_year, max_year)
    )

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
                default=None
            )

            if selected_teams:
                disable_player_filter = False
                df_utils = df_filtered[df_filtered['team_abbreviation'].isin(selected_teams)]
                players_name = df_utils['player_name'].unique().tolist()

            else:
                df_utils = df_filtered.copy(deep=True)

        with col_2:
            st.markdown("<p style='text-align: center;'>Selecione os jogadores</p>", unsafe_allow_html=True)
            selected_players = st.multiselect(
                label="",
                options=players_name,
                default=None,
                disabled=disable_player_filter,
                help="Selecione pelo menos um time para desbloquear o filtro de jogadores"
            )

            if selected_players:
                df_utils = df_utils[df_utils['player_name'].isin(selected_players)]

        st.divider()

        with st.container():
            st.markdown("<h3 style='text-align: center;'>Top Pontuadores</h3>", unsafe_allow_html=True)
            fig1 = plot_top10_est(df_utils, column_name='pts_per_season', color_hex=AZUL_NBA)
            st.plotly_chart(fig1, use_container_width=True)

        with st.container():
            st.markdown("<h3 style='text-align: center;'>Top Assistências</h3>", unsafe_allow_html=True)
            fig2 = plot_top10_est(df_utils, column_name='ast_per_season', color_hex=VERMELHO_NBA)
            st.plotly_chart(fig2, use_container_width=True)

        with st.container():
            st.markdown("<h3 style='text-align: center;'>Top Rebotes</h3>", unsafe_allow_html=True)
            fig3 = plot_top10_est(df_utils, column_name='reb_per_season', color_hex=LARANJA_NBA)
            st.plotly_chart(fig3, use_container_width=True)


