"""Utility Functions for working with DataFrames"""

import pandas as pd
import numpy as np

TEST_DF = pd.DataFrame([1,2,3])

def target_statistics(df,col_name):
    iqr = np.percentile(df[str(col_name)],75) - np.percentile(df[str(col_name)],25)
    lower_B = np.percentile(df[str(col_name)],25)
    upper_B = np.percentile(df[str(col_name)],75)
    x_bar = np.mean(df[str(col_name)])
    var = np.var(df[str(col_name)],ddof=1)
    std = np.std(df[str(col_name)],ddof=1)
    median = np.median(df[str(col_name)])
    mode = stats.mode(df[str(col_name)])
    tax_range = df[str(col_name)].max() - df[str(col_name)].min()
    
    print( " Statistics for DataFrame using Target: '{}'".format(str(col_name)),('\n'),
          'Mean:',round(x_bar,2),('\n'),
          'Median:',median,('\n'),
          'Mode:',mode,('\n'),
          'Tax range:', tax_range,('\n'),
          'Lower Bound:',lower_B,('\n'),
          'Upper Bound:',upper_B,('\n'),
          'Interquartile Range:', iqr)

target_statistiscs = target_statistics()