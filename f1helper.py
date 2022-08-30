import fastf1 as ff1
from fastf1 import plotting
import matplotlib.pyplot as plt

plotting.setup_mpl()
ff1.Cache.enable_cache('cache')

quali = ff1.get_session(2021, 'Austrian GP', 'Q')
laps = quali.load_laps(with_telemetry=True)

# Initializing plot
fig, ax = plt.subplots(figsize=(15, 8))

# Plotting driver data
for driver in ['NOR', 'RIC']:
    lap = laps.pick_driver(driver).pick_fastest()
    tel = lap.get_telemetry()
    ax.plot(tel['Distance'], tel['Speed'], label=driver)

# Finalizing plot
ax.set_xlabel('Distance [m]')
ax.set_ylabel('Speed [km/h]')
ax.set_title('Qualifying lap comparison (Distance vs. Speed)')
ax.legend()
plt.show()