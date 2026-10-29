import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')

variables = df[['age', 'chol', 'trestbps', 'thalach']]

for variable in variables:
    plt.figure()
    plt.hist(df[variable].dropna(), bins=15, edgecolor="black")
    plt.title(f"Histogram of {variable}")
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{variable}_histogram.png")
    plt.show()

print(df.head())

from scipy.stats import shapiro, probplot

for variable in variables:
    data=df[variable].dropna()
    stats,p=shapiro(data)
    print(variable,"p-value:",p)
    if p>0.05:
        print("We do not reject normality")
    else:
        print("We reject normality")

    probplot(data, dist="norm", plot=plt)
    plt.title(variable)
    plt.tight_layout()
    plt.savefig(f"{variable}_qqplot.png")
    plt.show()




