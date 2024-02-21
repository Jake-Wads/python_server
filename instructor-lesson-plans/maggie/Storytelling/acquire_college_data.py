import pandas as pd

df_scorecard = pd.read_csv("https://query.data.world/s/cy4dp4biln74tcah6dz7dytjxwjj4r", encoding="iso-8859-1")
df_scorecard.to_csv("scorecard.csv")

df_completion = pd.read_csv("https://query.data.world/s/727shc4rfhvmivgekk76nu7kg4jpia", encoding="iso-8859-1")
df_completion.to_csv("completion_rates.csv")

# https://data.world/databeats/college-completion/workspace/data-dictionary