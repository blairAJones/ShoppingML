#run this in a virtual environment (after running requirements.txt) to avoid issues with base kernel crashing

import numpy as np
import pandas as pd
from k_means_constrained import KMeansConstrained

def fit_kmc(df, column='price_value', n_clusters=3, min_frac=0.25, max_frac=0.50, random_state=1216):
    n = len(df)
    model = KMeansConstrained(
        n_clusters=n_clusters,
        size_min=int(min_frac * n),
        size_max=int(max_frac * n),
        random_state=random_state
    )
    df['cluster'] = model.fit_predict(df[[column]])

    centers = model.cluster_centers_.flatten()
    sorted_indices = np.argsort(centers)  
    labels = ['low', 'medium', 'high']
    cluster_label_map = {cluster_idx: label for cluster_idx, label in zip(sorted_indices, labels)}

    df['price_tier'] = df['cluster'].map(cluster_label_map)
    return df


df_iphone = pd.read_csv("data/iphone_new.csv")

import re
def extract_storage(title):
    # Match numbers followed by optional space and GB or TB (case-insensitive)
    pattern = re.compile(r'(\d+\s*(?:GB|TB))', re.IGNORECASE)
    matches = pattern.findall(title)
    if matches:
        # Standardize by removing spaces and uppercasing unit (e.g., "1 tb" -> "1TB")
        storage = matches[0].replace(" ", "").upper()
        return storage
    else:
        return "Unknown"

df_iphone['storage'] = df_iphone['title'].apply(extract_storage)
df_iphone['storage'] = df_iphone['storage'].replace({'6GB': '128GB'})
df_iphone["model_variant"] = df_iphone["title"].str.extract(r'\b(Pro Max|Pro|Plus)\b', flags=re.IGNORECASE).fillna("none")

df_iphone = fit_kmc(df_iphone, column='price.value')
df_iphone.to_csv("data/iphone_kmc.csv", index=False)

df_soccer = pd.read_csv("data/soccer_new.csv")
df_soccer = fit_kmc(df_soccer, column='price.value')
df_soccer.to_csv("data/soccer_kmc.csv", index=False)

df_microwaves = pd.read_csv("data/microwave_new.csv")
df_microwaves = df_microwaves[~((df_microwaves["cu_ft"] == "unknown") & (df_microwaves["price_value"] < 70))]
df_microwaves["commercial"] = df_microwaves["title"].str.contains("Commercial", case=False, na=False)
df_microwaves = fit_kmc(df_microwaves, column='price_value')
df_microwaves.to_csv("data/microwave_kmc.csv", index=False)

df_lego = pd.read_csv("data/lego_new.csv")
df_lego = fit_kmc(df_lego, column='price_value')
df_lego.to_csv("data/lego_kmc.csv", index=False)
