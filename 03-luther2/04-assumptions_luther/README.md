### Schedule

**9:00 am**: Coffee and the realization that presentations are tomorrow.

**9:15 am**: [Pair Problem](pair.md)

**9:45 am**: Linear Regression Assumptions Part Two: Electric Boogaloo

**10:45 am**: Let's get `seaborn`.

**11:00 am**: What do you mean your project isn't finished yet?

**12:00 pm**: Eat something.

**1:30 pm**: Work time

**5:00 pm**: Home time


#### Some example code to plot Q-Q plots

```Python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

measurements = np.random.normal(loc = 20, scale = 5, size=100)
stats.probplot(measurements, dist="norm", plot=plt)
plt.show()
```
