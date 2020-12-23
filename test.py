import numpy as np
expert1 = np.array([[True, False, False, True, True],
                   [False, True, False, False, True],
                   [True, True, True, False, False]])

expert2 = np.array([[True, False, False, False, True],
                   [False, False, False, False, False],
                   [True, False, True, False, False]])


exp1_and_exp2 = (expert1 & expert2 == True)
Jaccard_index = float(exp1_and_exp2.sum() / ((expert1.size + expert2.size) - exp1_and_exp2.sum()))

print('Индекс Жаккара: ', round(Jaccard_index,2))
print('')






