import pandas as pd
import matplotlib.pyplot as plt
import load_data as ld
import seaborn as sns; sns.set()


with open("cnn_data.json") as f:
        df = ld.cnn_dataframe(f)

print("There were %d questions asked"%len(set(df.question)))

def ask_a_question(df, que):

	c_pal = {'Hillary':'#3333FF', 'Donald':'#EE3523', 'N/A':'#DDDDDD'}

        df_q = df[df.question == que]

	g = sns.FacetGrid(df_q, col='answer', hue='candidate', col_wrap=3)
        g.map(sns.barplot, 'candidate', 'candidate_pct', palette=c_pal)
	g.set_xticklabels(rotation=90)
	g.set_ylabels('Candidate %')
	g.set_xlabels('')
	plt.ylim(0,100)
	plt.show()



ask_a_question(df, 'area type')

