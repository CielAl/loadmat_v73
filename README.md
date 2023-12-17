# loadmat_v73
load V7.3 or above mat files in python.


```
from loadmat_v73 import loadmat

exclude = ['field1/nested_field2', '#refs#']
fname = 'some.mat'
data=loadmat(fname, squeeze_me=True, exclude_h5=exclude)
```