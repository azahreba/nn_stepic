import numpy as np

# python3 -m pip install --upgrade pip
# pip3 install --user numpy

a = np.array([[1,2,3], [4,5,6]])  # создаём массив
print(a)  # смотрим на массив
print(a.shape)  # смотрим на форму массива
print(np.eye(3, 4, 1) + (np.eye(3, 4)*2))
