import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data2.csv")
avgRating = df["AvgRating"].tolist()

figure = ff.create_distplot([avgRating],["AvgRating"],show_hist=False)
figure.show()