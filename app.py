import streamlit as st
import os

import pandas as pd


if __name__ == '__main__':
    st.set_page_config(page_title="NBA dashboard", page_icon=':basketball:')

    st.title(":basketball: Dashboard NBA :basketball:")
    st.image(os.path.join("static", "nba_logo.png"), use_column_width=True)

    st.divider()

    st.markdown("A National Basketball Association (NBA) é a principal liga de basquetebol profissional da América do Norte. "
            "Com 30 franquias (29 nos Estados Unidos e 1 no Canadá), a NBA também é considerada a principal liga de "
            "basquete do mundo.")

    st.markdown("O trabalho foi desenvolvido sobre a base "
                "[NBA players](https://www.kaggle.com/datasets/justinas/nba-players-data/data) que contém dados "
                "dos jogadores que participaram da liga nas temporadas regulares de 1996 a 2022.")

    df_download = pd.read_csv("https://raw.githubusercontent.com/alyssondss42/NBA_Dashboard/master/data/nba_data_v2.csv")

    st.markdown("Baixe os dados já tratados que utilizamos nesse dashboard.")
    st.download_button(
        label="Download",
        data=df_download.to_csv().encode("utf-8"),
        file_name="nba_dataset.csv",
        mime="text/csv",
    )

    st.divider()
    st.markdown("O dashboard foi dividido em duas páginas: ")
    st.markdown(' - A página "1 - General" contém uma análise geral dos dados da base;')
    st.markdown('- A página "2 - Team Players" contém uma análise segmentada por time e jogadores;')
    st.page_link("pages/general.py", label="General", icon="1️⃣")
    st.page_link("pages/team_players.py", label="Team Players", icon="2️⃣")

    st.divider()

    st.write("**Grupo:** ")
    st.markdown("- Álysson Soares - (ass5@cesar.school)")
    st.markdown("- Eveline Cavalcanti - (ecfp@cesar.school)")
    st.markdown("- Fernando Rangel - (ftrs@cesar.school)")
    st.markdown("- Tathiana Martins - (tsm2@cesar.school)")
    st.markdown("- Vandelson Elias - (vemf@cesar.school)")





