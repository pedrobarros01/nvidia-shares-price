import pandas as pd
import numpy as np


def transform_colum_date_datasset(datasset: pd.DataFrame):
    datasset_copy = datasset.copy()
    datasset_copy['Date'] = pd.to_datetime(datasset_copy['Date'])
    dates_idx = pd.DatetimeIndex(datasset_copy['Date'])
    idx = [i for i, d in enumerate(dates_idx)]
    datasset_copy['Timer_day'] = idx
    return datasset_copy