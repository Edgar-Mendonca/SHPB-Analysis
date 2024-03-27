import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import SpanSelector

# Load data from CSV file
data = pd.read_csv('test_data/rawdata.csv')
time_data = data['Time'].values
incident_voltage = data['Incident'].values
transmitted_voltage = data['Transmitted'].values

fig, ((ax1, ax3), (ax2, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(12, 8))

ax1.plot(time_data, incident_voltage)
ax1.set_title('Press left mouse button and drag '
              'to select a region of Incident Voltage')
ax2.plot(time_data, incident_voltage)
ax2.set_title('Press left mouse button and drag '
              'to select a region of Reflected Voltage')


line1, = ax3.plot([], [])
line2, = ax4.plot([], [])

ax5.plot(time_data, transmitted_voltage)
ax5.set_title('Press left mouse button and drag '
              'to select a region of Tranmitted Voltage')

line3, = ax6.plot([], [])


#Incident
def onselect_incident(xmin, xmax):
    indmin, indmax = np.searchsorted(time_data, (xmin, xmax))
    indmax = min(len(time_data) - 1, indmax)

    region_x = time_data[indmin:indmax]
    region_y = incident_voltage[indmin:indmax]

    if len(region_x) >= 2:
        line1.set_data(region_x, region_y)
        ax3.set_xlim(region_x[0], region_x[-1])
        ax3.set_ylim(region_y.min(), region_y.max())
        fig.canvas.draw_idle()

        # Save selected data to CSV
        selected_data = pd.DataFrame({'Time': region_x, 'Incident Voltage': region_y})
        selected_data.to_csv('selected_incident.csv', index=False)


span_incident = SpanSelector(
    ax1,
    onselect_incident,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:blue"),
    interactive=True,
    drag_from_anywhere=True
)

#Reflected
def onselect_reflected(xmin, xmax):
    indmin, indmax = np.searchsorted(time_data, (xmin, xmax))
    indmax = min(len(time_data) - 1, indmax)

    region_x = time_data[indmin:indmax]
    region_y = incident_voltage[indmin:indmax]  # Change to reflected voltage data

    if len(region_x) >= 2:
        line2.set_data(region_x, region_y)
        ax4.set_xlim(region_x[0], region_x[-1])
        ax4.set_ylim(region_y.min(), region_y.max())
        fig.canvas.draw_idle()

        # Save selected data to CSV
        selected_data = pd.DataFrame({'Time': region_x, 'Reflected Voltage': region_y})
        selected_data.to_csv('selected_reflected.csv', index=False)


span_reflected = SpanSelector(
    ax2,
    onselect_reflected,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:orange"),
    interactive=True,
    drag_from_anywhere=True
)


#Transmitted
def onselect_transmitted(xmin, xmax):
    indmin, indmax = np.searchsorted(time_data, (xmin, xmax))
    indmax = min(len(time_data) - 1, indmax)

    region_x = time_data[indmin:indmax]
    region_y = transmitted_voltage[indmin:indmax]  

    if len(region_x) >= 2:
        line3.set_data(region_x, region_y)
        ax6.set_xlim(region_x[0], region_x[-1])
        ax6.set_ylim(region_y.min(), region_y.max())
        fig.canvas.draw_idle()

        # Save selected data to CSV
        selected_data = pd.DataFrame({'Time': region_x, 'Transmitted Voltage': region_y})
        selected_data.to_csv('selected_transmitted.csv', index=False)


span_transmitted = SpanSelector(
    ax5,
    onselect_transmitted,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:green"),
    interactive=True,
    drag_from_anywhere=True
)




plt.show()
