#%%
import pandas as pd

#%%
df = pd.read_csv('stats.csv')
df = df.convert_dtypes()

df.datetime = pd.to_datetime(df.datetime)
df = df.set_index('datetime')

df.speed_avg.where(~df.speed_avg.isnull(), df.distance / (df.time/60), inplace=True)

# %%
df.plot.scatter(x='distance', y='speed_avg', s=df.speed_max.astype(int), c=df.index, colormap="viridis")

# %%
df
# %%
