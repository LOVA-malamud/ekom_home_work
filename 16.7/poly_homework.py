import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

gym_hours  = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(-1,1)

muscle_gain = np.array([3.1,5.0,7.2,8.9,11.2,12.8,15.2,17.1,19.2,21.0])

load_kg = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5]).reshape(-1,1)

strength_score = np.array([-20.5,-15.2,-7.6,-0.8,3.2,2.1,4.7,6.0,4.9,1.6,-3.8])

fig, axes = plt.subplots(1, 2, figsize=(16,5))

axes[0].scatter(gym_hours, muscle_gain, color='red')
axes[0].set_xlabel('Hours spent in the gym')
axes[0].set_ylabel('Muscle gain (kg)')
axes[0].set_title('Gym Hours vs Muscle Gain')
axes[0].grid(True)

axes[1].scatter(load_kg, strength_score, color='blue')
axes[1].set_xlabel('Load lifted (kg)')
axes[1].set_ylabel('Strength score')
axes[1].set_title('Load vs Strength Score')
axes[1].grid(True)

plt.tight_layout()
plt.show()