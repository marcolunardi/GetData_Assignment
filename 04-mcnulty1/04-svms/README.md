### Schedule

**9:00 am**: Good morning

**9:15 am**: [Pair Problem](pair.md)

**9:45 am**: [Support Vector Machines](SVMs.pdf)

**10:30 am**: Jackie on NetworkX

 * [data](../../extra/networkx/networkx_test.csv)
 * [notebook](../../extra/networkx/NetworkX_Demo_20150430.ipynb)

**11:15 am**: McNulty work and Challenges

**12:00 pm**: Lunch

**1:30 pm**: McNulty work and Challenges

**5:00 pm**: Home


### Reading:

#### More on SVMs

[SVM math][14]
[A tutorial on SVMs][8]
[Another tutorial on SVMs][16]
[An Idiot's Guide to SVMs][9]
[SVM lecture][10]
[How to tune SVM Parameters][13]
[Preprocessing data in sklearn][11]
[SVMs in sklearn][12]
[RBF Kernel][15]

[1]: https://www.kaggle.com/c/titanic-gettingStarted
[8]: http://research.microsoft.com/pubs/67119/svmtutorial.pdf
[9]: http://www.cs.ucf.edu/courses/cap6412/fall2009/papers/Berwick2003.pdf
[10]: http://www.slideshare.net/shaochuan/support-vector-machine-2449514
[11]: http://scikit-learn.org/stable/modules/preprocessing.html
[12]: http://scikit-learn.org/stable/modules/svm.html
[13]: http://www.svms.org/parameters/
[14]: http://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf
[15]: https://charlesmartin14.wordpress.com/2012/02/06/kernels_part_1/
[16]: http://www.cs.columbia.edu/~kathy/cs4701/documents/jason_svm_tutorial.pdf

####Some more on Error Metrics

[Precision, recall, sensitivity, specificity](http://uberpython.wordpress.com/2012/01/01/precision-recall-sensitivity-and-specificity/)
[Wikipedia page on precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall)
[Scikit learn on classification metrics](http://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
[Receiver Operating Characteristic](http://gim.unmc.edu/dxtests/roc2.htm)
[Area under curve (ROC)](http://gim.unmc.edu/dxtests/roc3.htm)


#####What is the relationship between F1 and Fß?

If you have found the [metrics function](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html) in `sklearn` that spits out your precision, recall, and F score, you might have found yourself asking: "What is Fß? Is it the same as F1?"

The answer is ... yes. F1 combines precision and recall. Fß does
the same thing, but uses a weight so that you can weigh one of these
two (precision or recall) more than the other when combining them. It
is a way to tune your score if you care more about precision than
recall, for example. F1 is the Fß for which ß = 1. In
`sklearn`, the default value for ß is 1.

The [wikipedia page](http://en.wikipedia.org/wiki/F1_score) has more on this relationship.
