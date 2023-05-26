import matplotlib.pyplot as plt
	
fig, ax1 = plt.subplots()

vin = range(-10, 12, 2)

# iled = [0, 0, 0, 1, 5, 10, 14, 18, 22, 22, 22]
# rldr = [11300, 10600, 10300, 9500, 1600, 517, 274, 177.6, 145.7, 145.8, 145.9]

iled = [0, 1, 2, 2, 2.5, 2.5, 3, 3.5, 4, 4, 5]
rldr = [306, 157, 73, 43, 31, 23, 17, 14.5, 12, 11, 9]

color = 'tab:red'
ax1.set_xlabel('Input Voltage')
ax1.set_ylabel('LED Current (mA)', color=color)
ax1.plot(vin, iled, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('LDR Resistance (k)', color=color)  # we already handled the x-label with ax1
ax2.plot(vin, rldr, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Vactrol Response - Red LED')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
