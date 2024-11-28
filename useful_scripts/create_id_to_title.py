import pandas as pd

df = pd.read_csv("data/wikilink_graph.2006-03-01.csv", sep="\t")

# page_id and page_title pairs
id_to_title = pd.concat([
    df[['page_id_to', 'page_title_to']].rename(columns={'page_id_to': 'page_id', 'page_title_to': 'page_title'}),
    df[['page_id_from', 'page_title_from']].rename(columns={'page_id_from': 'page_id', 'page_title_from': 'page_title'})
])

# remove duplicate page_id entries
id_to_title = id_to_title.drop_duplicates().reset_index(drop=True)


id_to_title.to_csv("data/id_to_title.csv", index=False)

print("ID to Title table successfully created")
