import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches
plt.style.use('seaborn-pastel')

x_min = -2
x_max = 3

num_frames = 100

# Create 2 plots stacked vertically which share an x-axis
fig, ax = plt.subplots(2, sharex=True)

ax[0].set_xlim((x_min, x_max))
ax[0].set_ylim((-0.5, 1.5))
ax[0].set_xlabel('$\\tau$')
# ax[0].set_ylabel('$f(\\tau), g(\\tau)$')

ax[1].set_xlim([x_min, x_max])
ax[1].set_ylim([-0.5, 1.5])
ax[1].set_xlabel('$\\tau$')
# ax[1].set_ylabel('$(f \\ast g)(\\tau)$')

line_fx, = ax[0].plot([], [], lw=2, label='$f(\\tau)$')
line_gx, = ax[0].plot([], [], lw=2, label='$g(t - \\tau)$')
line_t_ax0 = ax[0].axvline(0, color='black')
line_t_ax1 = ax[1].axvline(0, color='black')

# Draw a thick line at y=0
ax[0].plot([x_min, x_max], [0, 0], lw=3, color='black')

# Create a rectangle to show the shared area of f(t) and g(t)
rect = mpatches.Rectangle([0, 0], 1, 1, ec="none", fc='C2')
ax[0].add_patch(rect)


line_conv, = ax[1].plot([], [], lw=2, color='C2', label='$(f \\ast g)(t)$')
conv = []
conv_t = []


ax[0].legend(loc='upper right')
ax[1].legend(loc='upper right')

ax[0].set_title('Convolution of Two Box Car Functions')


def init():
    line_fx.set_data([], [])
    line_gx.set_data([], [])
    line_conv.set_data([], [])
    return line_fx, line_gx, line_conv
def animate(i):
    print(i)

    # 
    t = x_min + (i/num_frames)*(x_max - x_min)

    print(f't = {t}')

    x = np.linspace(x_min, x_max, 1000)

    # Box-car function which doesn't move
    f_x = np.where((x > 0) & (x < 1), 1, 0)

    # Draw unit step function (reversed)
    g_x = np.where((x > t - 1) & (x < t), 1, 0)

    conv_t.append(t)

    if t >= 0 and t < 1.0:
        conv.append(t)
        rect.set_bounds(0, 0, t, 1)
    elif t >= 1.0 and t < 2.0:
        conv.append(2 - t)
        rect.set_bounds(t - 1, 0, 1 - (t-1), 1)
    else:
        conv.append(0)
        rect.set_bounds(0, 0, 0, 0)

    line_t_ax0.set_data([t, t], [0, 1])
    line_t_ax1.set_data([t, t], [0, 1])
    line_fx.set_data(x, f_x)
    line_gx.set_data(x, g_x)
    line_conv.set_data(conv_t, np.array(conv))
    ax[0].set_xticks([t])
    ax[0].set_xticklabels(['$t$'])
    return line_t_ax0, line_t_ax1, line_fx, line_gx, line_conv, rect

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=num_frames, interval=100, blit=True)

# Using imagemagick makes the GIF loop. pillow does not do this.
anim.save('convolution-two-box-car-functions.gif', writer='imagemagick')