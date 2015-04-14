
# coding: utf-8

# ## Exercise 2.4


# setup environment
import nsfg
import thinkstats2
import thinkplot
import numpy as np
import math
import pandas as pd


# cleaning data
preg = nsfg.ReadFemPreg()
def CleanFemPreg(df):
    df.agepreg /= 100.0
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
CleanFemPreg(preg)


# slicing the data   
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

firsts_totalwgt_lb = firsts.totalwgt_lb
others_totalwgt_lb = others.totalwgt_lb


# Cohen's D
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d


CohenEffectSize(firsts_totalwgt_lb, others_totalwgt_lb)



raw_differences = firsts_totalwgt_lb.mean() - others_totalwgt_lb.mean()
raw_differences


# # Exercise 3.1


# getting the data
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    return df


resp = ReadFemResp()
resp['numkdhh'].head()


# observed pmf
pmf = thinkstats2.Pmf((resp.numkdhh), label = 'observed')


# calculating biased pmf
def BiasPmf(pmf, label):
	new_pmf = pmf.Copy(label = label)
	for x, p in pmf.Items():
		new_pmf.Mult(x, x)
	new_pmf.Normalize()
	return new_pmf
biased_pmf = BiasPmf(pmf, label = 'biased')


# plotting
get_ipython().magic(u'matplotlib inline')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel = 'class size', ylabel = 'PMF')


# difference in means
pmf.Mean()
biased_pmf.Mean()


def CohenEffectSize(group1, group2):
    diff = group1.Mean() - group2.Mean()
    var1 = group1.Var()
    var2 = group2.Var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d


CohenEffectSize(pmf, biased_pmf)


# # Exercise 4.2


import random
sample_size = range(1000)
sample = []
generate_samples = random.random()

for num in sample_size:
    generate_samples = random.random()
    sample.append(generate_samples)


sample
cdf_plot = thinkstats2.Cdf(sample, label = "CDF")
pmf_plot = thinkstats2.Pmf(sample, label = "PMF")
cdf_plot
pmf_plot
thinkplot.Cdf(cdf_plot)
thinkplot.Pmf(pmf_plot)


"""Yes, the distribution is uniform.  You can see that the Cdf is a linear line at a 45 degree angle.
This means that the cumulative distribution is increasing at the same pace over time.
Also, the probabilities of each value """

column_names = list(preg[:1])
column_names
# ageatend, hpageend, ageqtnur_n, ageqtnur_p, ageqtnur


preg['ageatend'].head()
birth_weight = preg['totalwgt_lb']
mothers_age = preg['ageatend']
birth_weight.describe()
mothers_age.describe()
thinkplot.Scatter(birth_weight, mothers_age)

def Corr(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)
    meanx, varx = MeanVar(xs)
    meany, vary = MeanVar(ys)
    corr = Cov(xs, ys, meanx, meany) / math.sqrt(varx * vary)
    return corr

Corr(mothers_age, birth_weight)


def SpearmanCorr(xs, ys):
    xranks = pandas.Series(xs).rank()
    yranks = pandas.Series(ys).rank()
    return Corr(xranks, yranks)
from pandas import pandas


SpearmanCorr(mothers_age, birth_weight)


# # Exercise 8.2

def Estimate3(n=7, m=1000):
    lam = 2
    means = []
    medians = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        Lm = math.log(2) / thinkstats2.Median(xs)
        means.append(L)
        medians.append(Lm)
    print('rmse L', RMSE(means, lam))
    print('rmse Lm', RMSE(medians, lam))
    print('mean error L', MeanError(means, lam))
    print('mean error Lm', MeanError(medians, lam))

Estimate3()


