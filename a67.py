from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')

X=[[1],
   [2],
   [3],
   [77],
   [99],
   [45]
    ]
Y=[1,
   2,
   3,
   77,
   99,
   45
   ]

X=np.array(X)
Y=np.array(Y)

model=MLPRegressor(verbose=True,hidden_layer_sizes=(20,20,),max_iter=5000)

'''
model.fit(X,Y)
print(model.loss_)
#print(model.coefs_)
#print(model.intercepts_)
print(model.n_iter_)
#print(model.n_layers_)
#print(model.n_outputs_)
#print(model.out_activation_)

##plt.plot(model.loss_curve_)
##plt.show()
'''

    
new=np.array([[37]])
model.fit(X,Y)
pre=model.predict(new)
print(pre)
plt.plot(model.loss_curve_)
plt.show()

