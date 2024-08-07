import os
import pandas as pd
import numpy as np


class Dataframe_insights:
    
    def missing_value_report(self, df):
        missing_count = df.isnull().sum()
        missing_count = missing_count[missing_count > 0]
        missing_percentage = (missing_count / len(df)) * 100
        missing_report = pd.DataFrame({
            'Columns' : missing_count.index,
            'Missing_values' : missing_count.values,
            'Missing_Percentage' : missing_percentage.values
        })

        return missing_report
    
    def percentile_report(self, series):
        percentiles = [10, 25, 50, 75, 90]
        percentile_values = series.quantile([p/100 for p in percentiles])
        percentile_df = pd.DataFrame([percentile_values.values],
                                     columns = ['10th Percentile', '25th Percentile',
                                                '50th Percentile', '75th Percentile',
                                                '90th Percentile'])
        
        return percentile_df
    
    def value_counts(self, series):
        values = series.value_counts()
        values_df = values.reset_index()
        values_df.columns = ['Category', 'Count']
        values_df.sort_values(by = 'Count', ascending = False)
        return values_df
    


    
df_insights = Dataframe_insights()


os.chdir('c:\\Users\\RohanMariyala\\MyPracticeTrack\\Week4')
df = pd.read_csv('housing.csv')
#print(os.getcwd())

missing_value_report = df_insights.missing_value_report(df)
print(missing_value_report)
percentile_report = df_insights.percentile_report(df['housing_median_age'])
print("\n\n")
print(percentile_report)
print("\n\n")

value_counts = df_insights.value_counts(df['ocean_proximity'])

print(value_counts)


