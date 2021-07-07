# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 02:29:25 2021

@author: WeiKuang Lin
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def density_plot(df_long, var_cont, var_group, color_list, var_group_order=None, ylim = (0,0.06)):
    """
    Argument:
        df_long is a long formate dataframe
        var_group is a string indicating the groups
        var_cont is a string indication the continuous variable
        color_list is a list for color shown in density plot
        var_group_order is a list indicating the order of grouping variable

    Output:
        Density plot
    """
    
    # Descriptive statistics
    df_stats = df_long.groupby([var_group])[var_cont].agg(['count', 'mean', 'std'])
    df_stats['index'] = df_stats.index
    df_stats['label'] = df_stats["index"] + ' N=' +df_stats["count"].astype(str) 
    df_stats

    # Density Plot Layer
    fig, ax = plt.subplots()
    fig.set_size_inches(6.5, 6)
    ax.set(ylim=ylim)

    if pd.isnull(var_group_order):
        var_group_order = df_long[var_group].unique()

    for x,c  in zip(  var_group_order  , color_list):
        # density plot 
        subset = df_long[df_long[ var_group ] == x]
        sns.kdeplot(subset[ var_cont ], color=c, ax=ax, label= df_stats.loc[x,'label'] , bw_adjust=2)
    
        # Vertical line for mean
        plt.axvline(x=df_stats.loc[x,'mean'] , color= c, linestyle='--',  linewidth=.7)

    SMALL_SIZE = 11
    MEDIUM_SIZE = 15
    BIGGER_SIZE = 15
    
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1) 
    plt.show()