## Compare to M1 max from internet friend
`M1 max`
 
```shell
# CPU
$ python pytorch_m1_macbook.py --device cpu
Epoch 1 / 5: time = 427.44[s], loss = 168.22
Epoch 2 / 5: time = 859.18[s], loss = 134.87
Epoch 3 / 5: time = 1284.35[s], loss = 121.36
Epoch 4 / 5: time = 1716.77[s], loss = 112.03
Epoch 5 / 5: time = 2148.09[s], loss = 105.66
Train time on cpu: 2148.09[s] (Train loss = 105.66)
Test time on cpu: 90.19[s](Test loss = 20.52)
```


```shell
# GPU
$ python pytorch_m1_macbook.py --device mps
Epoch 1 / 5: time = 57.19[s], loss = 170.57
Epoch 2 / 5: time = 114.71[s], loss = 138.20
Epoch 3 / 5: time = 172.46[s], loss = 124.46
Epoch 4 / 5: time = 229.30[s], loss = 113.49
Epoch 5 / 5: time = 286.53[s], loss = 104.97
Train time on mps: 286.53[s] (Train loss = 104.97)
Test time on mps: 45.05[s](Test loss = 20.24)
```


`2019 16inch`
```shell
# intel i7
Epoch 1 / 5: time = 308.75[s], loss = 172.36
Epoch 2 / 5: time = 618.65[s], loss = 139.98
Epoch 3 / 5: time = 952.42[s], loss = 126.97
Epoch 4 / 5: time = 1275.09[s], loss = 117.12
Epoch 5 / 5: time = 1646.17[s], loss = 108.15
Train time on cpu: 1646.17[s] (Train loss = 108.15)
Files already downloaded and verified
Test time on cpu: 70.17[s](Test loss = 20.45)
```
```shell
# GPU 5300M
Files already downloaded and verified
Epoch 1 / 5: time = 163.31[s], loss = 170.97
Epoch 2 / 5: time = 296.59[s], loss = 136.47
Epoch 3 / 5: time = 427.19[s], loss = 122.78
Epoch 4 / 5: time = 559.90[s], loss = 112.44
Epoch 5 / 5: time = 692.08[s], loss = 105.57
Train time on mps: 692.08[s] (Train loss = 105.57)
```