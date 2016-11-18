import pandas as pd
import matplotlib.pyplot as plt
import load_data as ld

plt.style.use('fivethirtyeight')   

with open("cnn_data.json") as f:
        df = ld.cnn_dataframe(f)

print("There were %d questions asked"%len(set(df.question)))

def add_color(name):
        dem_blue = "#3333FF"
        rep_red  = "#EE3523"
        neutral  = "#DDDDDD"

        if name == 'Hillary':
                return dem_blue
        elif name == 'Donald':
                return rep_red
        else:
                return neutral

def ask_a_question(df, que):

        df_q = df[df.question == que]
        df_q = df_q.set_index('answer')

        df_q.candidate_pct.plot(kind='bar', color=df.Colour)

        plt.title(que)
        plt.ylabel('Candidate %')
        plt.show()



df['Colour'] = df.candidate.apply(add_color)

ask_a_question(df, 'area type')
