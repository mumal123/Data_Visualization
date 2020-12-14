import pandas as pd
from matplotlib.pyplot import pie, axis, show



df = pd.read_csv ('data.csv')

sums = df.groupby(df["country"])["cases"].sum()
axis('equal');
pie(sums, labels=sums.index);
show()