import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ваши данные с координатами x, y и h (высота)
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
h = [[10, 20, 30, 47, 45],
     [10, 20, 30, 47, 18],
     [10, 20, 10000, 47, 18],
     [14, 20, 30, 47, 18],
     [10, 70, 30, 67, 18]]


# Создаем сетку координат x и y
X, Y = np.meshgrid(x, y)

# Преобразуем координаты и высоту в массив numpy
X = np.array(X)
Y = np.array(Y)
H = np.array(h)

# Создаем экземпляр графика 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Строим поверхность
surf = ax.plot_surface(X, Y, H, cmap='viridis')

# Добавляем метку осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')

# Показываем график
plt.show()
