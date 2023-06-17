# function to clean columns containing numerical values
def impute_median(df, column_name):
    median_value = df[~df[column_name].astype(str).str.contains('NA')][column_name].astype(float).median()
    df.loc[df[column_name].astype(str).str.contains('NA'), column_name] = median_value
    df[column_name] = df[column_name].fillna(median_value)

    return df
