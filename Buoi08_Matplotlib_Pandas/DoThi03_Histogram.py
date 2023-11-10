import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(25, 0.2, 20)
print(data)

plt.hist(data)
plt.show()