import pandas as pd
import numpy as np

def merge_all_data(file1, file2, file3, file4):
    # Load CSVs
    user_health_df = pd.read_csv(file1, parse_dates=['date'])
    supplement_usage_df = pd.read_csv(file2, parse_dates=['date'])
    experiments_df = pd.read_csv(file3)
    user_profile_df = pd.read_csv(file4)
    
    # User Health Data Clean
    user_health_df = user_health_df.dropna(subset=['user_id', 'date'])
    if user_health_df['sleep_hours'].dtype == 'O':
        user_health_df['sleep_hours'] = user_health_df['sleep_hours'].str.strip('hH').astype(float)
    # Supplement Usage Clean
    supplement_usage_df = supplement_usage_df.dropna(subset=['user_id', 'date'])
    # Convert supplement dosage to grams
    supplement_usage_df['dosage_grams'] = supplement_usage_df.apply(
    	lambda row: row['dosage'] / 1000 if row['dosage_unit'] == 'mg' else row['dosage'], axis=1
    )
    # Experiments Clean
    experiments_df.rename(columns={'name': 'experiment_name'}, inplace=True)
    # User Profiles Clean
    user_profile_df = user_profile_df.dropna(subset=['user_id', 'email'])
    
    # Map age to age groups
    def categorize_age(age):
        if pd.isna(age):
            return 'Unknown'
        elif age < 18:
            return 'Under 18'
        elif age <= 25:
            return '18-25'
        elif age <= 35:
            return '26-35'
        elif age <= 45:
            return '36-45'
        elif age <= 55:
            return '46-55'
        elif age <= 65:
            return '56-65'
        else:
            return 'Over 65'

    user_profile_df['user_age_group'] = user_profile_df['age'].apply(categorize_age)
    
    #print(user_health_df.columns)
    #print(user_profile_df.columns)
    #print(supplement_usage_df.columns)
    #print(experiments_df.columns)

     # Merge user_profiles and user_health
    user_health_profiles_df = pd.merge(user_health_df, user_profile_df[['user_id', 'email', 'user_age_group']], on='user_id', how='left')
    
    # Merge user_profiles_health_df and supplement_df
    user_h_p_supp_df = pd.merge(user_health_profiles_df, supplement_usage_df[['user_id', 'date', 'experiment_id', 'is_placebo', 'supplement_name', 'dosage_grams']], on=['user_id', 'date'], how='left')

    # Merge health data and supplement data on user_id and date
    merged_data = pd.merge(user_h_p_supp_df, experiments_df[['experiment_id', 'experiment_name']], on=['experiment_id'], how='left')
    
    # Fill missing supplement values
    merged_data['supplement_name'].fillna('No intake', inplace=True)
    merged_data['experiment_name'].fillna(np.nan, inplace=True)
    merged_data['dosage_grams'].fillna(np.nan, inplace=True)
    merged_data['is_placebo'].fillna(np.nan, inplace=True)

    final_columns = [
            'user_id', 'date', 'email', 'user_age_group', 'experiment_name', 'supplement_name',
        'dosage_grams', 'is_placebo', 'average_heart_rate', 'average_glucose',
        'sleep_hours', 'activity_level'
        ]
    
    final_df = merged_data[final_columns]
    
    print(final_df)
    print(final_df.columns)
    print(final_df.dtypes)
    print(final_df.info())

merge_all_data('/Users/ryan/workspace/github.com/rdadmun/Datacamp/data_engineer_projects/user_health_data.csv', 
               '/Users/ryan/workspace/github.com/rdadmun/Datacamp/data_engineer_projects/supplement_usage.csv', 
               '/Users/ryan/workspace/github.com/rdadmun/Datacamp/data_engineer_projects/experiments.csv', 
               '/Users/ryan/workspace/github.com/rdadmun/Datacamp/data_engineer_projects/user_profiles.csv')