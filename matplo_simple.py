import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
# from matplotlib.patches import FancyBboxPatch
import main

fig, ax = plt.subplots(figsize=(8, 6))


# Створення даних
x, y = main.wind()

for xi, yi in zip(x, y):
    ax.arrow(xi, yi, 0.5, 0, head_width=0.1, head_length=0.1, fc='blue', ec='blue')

# Побудова графіку
#plt.plot(x, y)
ax.scatter(x, y, s=5)


x_target = 0
y_target = 0

ax.scatter(x_target, y_target, color='red')
label = 'Target'
ax.text(x_target, y_target-0.5, label, ha='center')

# Add an oval shape
width = 3
height = 3
ellipse = Ellipse(xy=(x_target, y_target), width=width, height=height*1.2, edgecolor='red', facecolor='none')
ax.add_patch(ellipse)

text_below = ' Conditional re-optimization, wind = 8 m/s: µx =−0.25m,' \
             ' µy = −0.08m, σx = 0.77m,σy = 0.54m'
ax.text(0, -18, text_below, ha='center')

# Add a square box with text
text = '-> CARP position and velocity\n- µ + 1σ\no µ'
textbox = ax.text(-13, 12.1, text, ha='left', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))

# # Add a blue line below the text
# line_y = 13 - 0.6
# ax.axhline(line_y, color='red')

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)



plt.show()
