import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data2.csv")
mobileBrand = df["MobileBrand"].tolist()

figure = ff.create_distplot([mobileBrand],["MobileBrand"],show_hist=False)
figure.show()