import numpy as np
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures


d = np.array([[2,4],
              [3,6]])

d_t = d.T

d_m_d_t = np.matmul(d, d_t)

print(d_t)
print(np.linalg.det(d_m_d_t))
# hello