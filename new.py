import numpy as np
import pandas as pd 

n1=np.random.randint(1,10,(5,5))
p1=pd.DataFrame(n1)
p1.columns=('A','B','C','D','E')
print(n1)
print(p1)