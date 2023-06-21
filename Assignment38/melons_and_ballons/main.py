import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# melons
melons_width=np.random.normal(20,6,300)
melons_height=np.random.normal(25,6,300)
melons_weight=np.random.normal(150,6,300)

# ballons
ballons_width=np.random.normal(40,5,300)
ballons_height=np.random.normal(50,5,300)
ballons_weight=np.random.normal(20,5,300)

ax=plt.axes(projection="3d")
ax.scatter(melons_width,melons_height,melons_weight,marker="o",c="g",alpha=0.5)
ax.scatter(ballons_width,ballons_height,ballons_weight,marker="*",c="r")


# legend
for i in [["o","melon","g"],["*","ballon","r"]]:
    ax.scatter([],[],marker=i[0],label=i[1],alpha=0.5,c=i[2])
ax.legend(scatterpoints=1,frameon=True,labelspacing=1)
ax.set_xlabel("width")
ax.set_ylabel("height")
ax.set_zlabel("weight")
ax.set_title("melons and ballons")
plt.show()