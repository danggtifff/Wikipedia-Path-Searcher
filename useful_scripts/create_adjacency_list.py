import pandas as pd;

# Load dataset
df = pd.read_csv("Data/wikilink_graph.2006-03-01.csv", sep="\t")

df.drop(columns={"page_title_from", "page_title_to"}, inplace=True)

# merge all outward connections of a page id into one list of id's
df_grouped = df.groupby(['page_id_from']).agg({
    'page_id_to': lambda x: list(x.dropna())
}).reset_index()

df.drop(columns={"page_id_from", "page_id_to"}, inplace=True)

df_grouped.to_csv("Data/merged.csv", index=False)

print("Adjacency list successfully created")