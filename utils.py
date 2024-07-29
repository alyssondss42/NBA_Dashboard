from globals import AZUL_NBA, VERMELHO_NBA, LARANJA_NBA
import plotly.graph_objects as go
import numpy as np


def plot_mean_age(df):
    df_age_mean = df[['age', 'season']].groupby(['season']).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_age_mean.index,
                             y=df_age_mean['age'],
                             mode='lines+markers',
                             line=dict(color=AZUL_NBA, width=2),
                             marker=dict(color=LARANJA_NBA, size=8)
                             )
                  )
    # Atualizar layout com título e rótulos dos eixos
    fig.update_layout(
        title='Média de idade dos jogadores por temporada/ano',
        xaxis_title='Temporada',
        yaxis_title='Idade',
        title_x=0.25,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="Temporada",
                         step="year",
                         stepmode="backward"),
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="category"
        )
    )
    return fig


def calculate_mean_est(df, est_name):
    mean_value = df[est_name].mean()
    return round(mean_value, 3)


def calculate_sum_est(df, est_name):
    sum_value = df[est_name].sum()
    return round(sum_value, 3)


def plot_corr(df):
    corr_height_reb = df[['player_height', 'reb', 'season']].groupby('season').corr().unstack().iloc[:, 1]
    corr_height_ast = df[['player_height', 'ast', 'season']].groupby('season').corr().unstack().iloc[:, 1]
    corr_height_pts = df[['player_height', 'pts', 'season']].groupby('season').corr().unstack().iloc[:, 1]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=corr_height_ast.index,
                             y=corr_height_ast.values,
                             mode='lines+markers',
                             line=dict(color=VERMELHO_NBA, width=2),
                             name="Assitências"
                             ))

    fig.add_trace(go.Scatter(x=corr_height_reb.index,
                             y=corr_height_reb.values,
                             mode='lines+markers',
                             line=dict(color=LARANJA_NBA, width=2),
                             name="Rebotes"
                             ))
    fig.add_trace(go.Scatter(x=corr_height_pts.index,
                             y=corr_height_pts.values,
                             mode='lines+markers',
                             line=dict(color=AZUL_NBA, width=2),
                             name="Pontos"
                             ))

    fig.update_layout(title='Correlação da altura com as estatísticas por temporada',
                      xaxis_title='Temporada',
                      yaxis_title='Correlação',
                      title_x=0.25)

    return fig


def plot_histogram(df, column_name, x_axis_name):
    # valores uteis
    player_mean = np.mean(df[column_name])
    min_ = min(df[column_name])
    max_ = max(df[column_name])

    fig = go.Figure()

    fig.add_trace(go.Histogram(x=df[column_name],
                               marker_color=AZUL_NBA,
                               xbins=dict(start=min_,
                                          end=max_,
                                          size=5),
                               opacity=0.7
                               ))

    # add linha de altura média
    fig.add_vline(x=player_mean,
                  line_dash='dash',
                  line_color=VERMELHO_NBA,
                  annotation_text=f'Média: {player_mean:.2f}')

    fig.update_layout(xaxis_title=x_axis_name,
                      yaxis_title='Frequência',
                      bargap=0.1,
                      bargroupgap=0.1)

    return fig


def plot_top10_est(df, column_name, color_hex=AZUL_NBA):
    df = df[[column_name, 'player_name']].groupby(['player_name']).sum()
    df = df[column_name].nlargest(10).sort_values(ascending=True)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=df.index,
            x=df.values,
            orientation='h',
            marker=dict(color=color_hex)
        )
    )

    fig.update_layout(
        xaxis_title='Quantidade',
        yaxis_title='Jogador'
    )

    return fig


def create_card(content, text_color):
    return f"""
    <div style="
        border: 1px solid #ddd; 
        border-radius: 6px; 
        padding: 8px; 
        margin: 8px; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: #000000;
        color: {text_color};
    ">
        <p style="text-align: center; color: {text_color}; font-size: 24px;">{content}</p>
    </div>
    """