import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pb_one_two import pb100m, pb200m, pb400m

'''
plots correlation matrixs and saves as png
also describes data and exports it to an excel file
'''

data = {'400': pb400m, '200': pb200m, '100': pb100m}

df = pd.DataFrame(data, columns=['400','200','100'])

corrMatrix = df.corr()

corrVisualisation = sns.heatmap(data=corrMatrix, annot=True, cmap='mako', center=0)

file_name = str(input("Name the file: "))

df.describe().to_csv("plots/"+ file_name + ".csv")
plt.savefig("plots/" + file_name + ".png")  
