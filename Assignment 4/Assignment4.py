import numpy as np

# Q1
my_array = np.array([1, 2, 3, 4, 5])
new_array_add = my_array + 2
new_array_mul = my_array * 3
new_array_div = my_array / 2

# Q2
num_array = np.array([1, 2, 3, 6, 4, 5])[::-1]

x_array = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y_array = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

most_common_x = np.bincount(x_array).argmax()
index_x = np.where(x_array == most_common_x)[0]

most_common_y = np.bincount(y_array).argmax()
index_y = np.where(y_array == most_common_y)[0]

# Q3
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
first_row_second_col = matrix[0, 1]
third_row_first_col = matrix[2, 0]

# Q4
name_array = np.linspace(10, 100, 25)
array_dim = name_array.ndim
array_shape = name_array.shape
total_elements = name_array.size
data_type = name_array.dtype
total_bytes = name_array.nbytes
reshaped_array = name_array.reshape(25, 1)
transpose_possible = name_array.T.shape

# Q5
my_2d_array = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
mean_value = np.mean(my_2d_array)
median_value = np.median(my_2d_array)
max_value = np.max(my_2d_array)
min_value = np.min(my_2d_array)
unique_values = np.unique(my_2d_array)
reshaped_array_2d = my_2d_array.reshape(4, 3)
resized_array_2d = np.resize(my_2d_array, (2, 3))
