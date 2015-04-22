### Schedule

**9:00 am**: coffee coffee coffee

**9:15 am**: [Pair Problem](pair.md)

**9:45 am**: [Linear regression's assumptions](Linear_Regression_Assumptions.pdf)

**10:45 am**: Get those Products Minimally Viable!

**12:00 pm**: Lunch of champions.

**1:30 pm**: Make Products even more viable.

**5:00 pm**: More fun!


#### Some example code to plot Q-Q plots

```Python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

measurements = np.random.normal(loc = 20, scale = 5, size=100)
stats.probplot(measurements, dist="norm", plot=plt)
plt.show()
```
