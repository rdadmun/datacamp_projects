import pandas as pd
import numpy as np

# Load the dataset
file_path = "bank_marketing.csv"
df = pd.read_csv(file_path)

# Cleaning and transforming the client dataset
client_df = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]].copy()
client_df["job"] = client_df["job"].str.replace(".", "_", regex=False)
client_df["education"] = client_df["education"].replace("unknown", np.nan).str.replace(".", "_", regex=False)
client_df["credit_default"] = client_df["credit_default"].map(lambda x: 1 if x == "yes" else 0).astype(bool)
client_df["mortgage"] = client_df["mortgage"].map(lambda x: 1 if x == "yes" else 0).astype(bool)
client_df.to_csv("client.csv", index=False)

# Cleaning and transforming the campaign dataset
campaign_df = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "day", "month"]].copy()
campaign_df["previous_outcome"] = campaign_df["previous_outcome"].map(lambda x: 1 if x == "success" else 0).astype(bool)
campaign_df["campaign_outcome"] = campaign_df["campaign_outcome"].map(lambda x: 1 if x == "yes" else 0).astype(bool)

# Mapping month names to numbers
month_map = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
             "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
campaign_df["month"] = campaign_df["month"].map(month_map)

# Creating last_contact_date column
campaign_df["last_contact_date"] = pd.to_datetime(campaign_df[["day", "month"]].assign(year=2022))
campaign_df.drop(columns=["day", "month"], inplace=True)
campaign_df.to_csv("campaign.csv", index=False)

# Cleaning and transforming the economics dataset
economics_df = df[["client_id", "cons_price_idx", "euribor_three_months"]].copy()
economics_df.to_csv("economics.csv", index=False)

print("Data processing complete. Files saved: client.csv, campaign.csv, economics.csv")
