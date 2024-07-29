from utils import plot_mean_age, create_card, calculate_mean_est, plot_corr, plot_histogram
from globals import VERMELHO_NBA, AZUL_NBA, LARANJA_NBA
import streamlit as st
import pandas as pd
import os


if __name__ == '__main__':
    st.set_page_config(page_title="NBA dashboard", page_icon=':basketball:')

    st.title(":bar_chart: Análise geral dos dados :bar_chart:")

    df = pd.read_csv(os.path.join("data", "nba_data_v2.csv"))

    st.divider()
    st.markdown("<h3 style='text-align: center;'>Selecione o intervalo das temporadas</h3>", unsafe_allow_html=True)
    start_year, end_year = st.select_slider(
        "",
        options=df['season'].unique().tolist(),
        value=(1996, 2022)
    )
    st.divider()

    df_filtered = df[(df['season'] >= start_year) & (df['season'] <= end_year)]

    with st.container():
        col_1, col_2, col_3 = st.columns(3)

        with col_1:
            st.markdown("<h3 style='text-align: center;'>Média de pts: </h3>", unsafe_allow_html=True)
            st.markdown(create_card(calculate_mean_est(df_filtered, 'pts_per_season'), AZUL_NBA), unsafe_allow_html=True)

        with col_2:
            st.markdown("<h3 style='text-align: center;'>Média de ast: </h3>", unsafe_allow_html=True)
            st.markdown(create_card(calculate_mean_est(df_filtered, 'ast_per_season'), VERMELHO_NBA), unsafe_allow_html=True)

        with col_3:
            st.markdown("<h3 style='text-align: center;'>Média de reb: </h3>", unsafe_allow_html=True)
            st.markdown(create_card(calculate_mean_est(df_filtered, 'reb_per_season'), LARANJA_NBA), unsafe_allow_html=True)

    st.divider()

    with st.container():
        # add dados aqui
        fig1 = plot_mean_age(df_filtered)
        st.plotly_chart(fig1, use_container_width=True)

    st.divider()


    with st.container():
        col_1, col_2 = st.columns(2)
        # add dados aqui
        with col_1:
            st.text("Distribuição da altura dos jogadores")
            fig2 = plot_histogram(df_filtered, column_name='player_height', x_axis_name='Altura (cm)')
            st.plotly_chart(fig2, use_container_width=True)

        with col_2:
            st.text("Distribuição do peso dos jogadores")
            fig3 = plot_histogram(df_filtered, column_name='player_weight', x_axis_name='Peso (kg)')
            st.plotly_chart(fig3, use_container_width=True)

    st.divider()
    with st.container():
        fig4 = plot_corr(df_filtered)
        st.plotly_chart(fig4, use_container_width=True)




