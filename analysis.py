import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import load_data as ld
   

with open("cnn_data.json") as f:
        df = ld.cnn_dataframe(f)




