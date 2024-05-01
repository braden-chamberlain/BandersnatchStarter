from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """creates a graph from the data"""

    df = df.drop(columns=['_id'])
    graph = Chart(
        df,
        title=f'{y} by {x} for {target}',
        background='#1c1c1c',
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=800,
        height=800,
        padding=10
    ).configure_title(
        fontSize=24,
        color='lightgray'
    ).configure_axis(
        labelColor='lightgray',
        titleColor='lightgray',
        gridColor='#333333'
    ).configure_legend(
        labelColor='lightgray',
        titleColor='lightgray'
    )
    return graph
