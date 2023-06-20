import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("california_cities.csv")



plt.scatter(data["latd"],data["longd"],
            s=data["area_total_km2"],alpha=0.5,linewidth=0,
            c=np.log10(data["population_total"]))
plt.xlabel("latitude")
plt.ylabel("longitude")
plt.title("Area and population of california ceties")
plt.colorbar(label="log 10 population")
for area in [100,300,500]:
    plt.scatter([],[],c="k",alpha=0.3,s=area,label=str(area)+"km$^2$",linewidth=0)
plt.legend(scatterpoints=1,frameon=False,labelspacing=1,title="City Area")

plt.show()