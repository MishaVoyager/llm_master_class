from typing import Optional

import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from pandas import DataFrame


def draw_hist_with_average(
        df: DataFrame,
        series_name: str,
        label: Optional[str] = None,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        show: bool = False
) -> None:
    """Рисует гистограмму с линией среднего значения"""
    plt.ticklabel_format(style='plain', axis='y', useOffset=False)
    plt.hist(df[series_name],
             range=(
                 df[series_name].mean() - 3 * df[series_name].std(),
                 df[series_name].mean() + 3 * df[series_name].std()),
             color='green',
             bins=100,
             label=label
             )
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axvline(df[series_name].mean(), color='grey', linestyle='--', label="Среднее")
    if show:
        plt.legend()
        plt.show()