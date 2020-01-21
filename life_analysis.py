# Function for first round data cleansing

def data_cleansing(raw, filter_out, replace_dict, drop_list):
    
    # Remove unnecessary columns that contain these text
    df = raw.copy()
    for f in filter_out:
        df = df.loc[:, ~df.columns.str.contains(f)]

    # Clean up characters from column names
    for key, value in replace_dict.items():
        df.columns = df.columns.str.replace(key, value)

    # Manually drop irrelevant columns
    remain_cols = [i for i in df.columns if i not in drop_list]
    df = df[remain_cols]

    # Drop column if data is > 20% null
    df = df.drop(df.loc[:,list((100*(df.isnull().sum()/len(df.index))>20))].columns, 1)

    # Replace NaN values with the state's median. If still missing, use national.
    df = df.groupby('State_Abbreviation').apply(lambda x: x.fillna(x.median()))
    df = df.fillna(df.median())

    # Remove state-level data, keep only county-level data
    df = df.drop(df[df.County_FIPS_Code==0].index)

    return df

# Function to remove outliers

def remove_outliers(df, k):
    # k = num of std from mean as outlier
    
    dfcopy = df.copy()
    for col in df.columns:
        mean = dfcopy[col].mean()
        std  = dfcopy[col].std()
        df = df.drop(df[df[col] > mean + k*std].index)
        df = df.drop(df[df[col] < mean - k*std].index)
    print(f'{round((1 - df.shape[0] / dfcopy.shape[0])*100,1)}% of rows removed')
    print(f'{df.shape[0]} rows remains')
    return df

# Function to log transform data

def log_transform(df, target):

    import numpy as np
    dfcopy = df.copy()
    for col in df.columns:
        if col != target:
            if df[col].min() > 0:
                df[col] = np.log(df[col])
            else:
                df[col] = np.log(df[col] + dfcopy[col].min() + 1)
    return df

# Function to plot scatter diagram and histogram for all indicators

def plot_all(df, num_of_plots_per_row = 6, target = None):
    
    import matplotlib.pyplot as plt
    from textwrap import wrap
    
    num_of_cols = df.shape[1]
    num_of_sets = num_of_cols // (num_of_plots_per_row + 1)
    k = 0
    for r, s in enumerate(range(num_of_sets)):
        color = 'blue' if (r % 2) == 0 else 'red'
        x1 = k
        x2 = k + num_of_plots_per_row
        k = k + num_of_plots_per_row + 1
        r = r * 2
        dfplot = df.iloc[:, x1:x2]
        cols_to_plot = list(dfplot.columns)

        fig, axes = plt.subplots(nrows=2, ncols=len(cols_to_plot), figsize=(18,4))
        for n, xcol in enumerate(cols_to_plot):
            axes[0,n].set_title("\n".join(wrap(xcol, 25)), fontsize=9)
            axes[0,n].scatter(dfplot[xcol], df.Life_expectancy, color=color, s=2)
            axes[0,n].set_ylabel(target, fontsize=8)
            axes[1,n].hist(dfplot[xcol], color=color)       
        plt.show()