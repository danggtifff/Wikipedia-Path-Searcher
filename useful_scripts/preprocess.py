import pandas as pd;

# Load your dataset
df = pd.read_csv("Data/wikilink_graph.2007-03-01.csv", sep="\t")

df.drop(columns={"page_id_from", "page_id_to"}, inplace=True)
# Group by encounter_csn and aggregate CPT codes into a list, keeping first values for other columns
df_grouped = df.groupby(['page_title_from']).agg({
    'page_title_to': lambda x: list(x.dropna())
}).reset_index()

df.drop(columns={"page_title_from", "page_title_to"}, inplace=True)
# Save the cleaned data to a new CSV file
df_grouped.to_csv("Data/merged.csv", index=False)

# Output the result
print("FARM MERGE VALLEY")