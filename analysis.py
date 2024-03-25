import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import savgol_filter
from scipy.integrate import cumulative_trapezoid  # Import cumulative_trapezoid from scipy.integrate

# Inputs (Please fill in the values accordingly)
Eb = 2.1e11  # Young's modulus of the bars (Pa)
rho_b = 8000  # Density of the bars (kg/m^3)
lo = 3e-3  # Initial length of the specimen (m)
Ab = 314e-6  # Cross-sectional area of the bars (m^2)
As = 255e-6  # Cross-sectional area of the specimen (m^2)

# Specify file type (csv or xlsx) and filename
file_type = "csv"  # Change to "xlsx" for Excel files
filename = "test_data/test.csv"  # Update with your actual filename

# Read data based on file type
if file_type == "csv":
    data = pd.read_csv(filename)
elif file_type == "xlsx":
    data = pd.read_excel(filename)
else:
    print("Unsupported file type. Please specify 'csv' or 'xlsx'.")
    exit()

# Extract data for plotting
time_data = data["Time"]  # Assuming "Time" is the column name for time data
incident_voltage = data["Incident"]
reflected_voltage = data["Reflected"]
transmitted_voltage = data["Transmitted"]

# Define Savitzky-Golay filter parameters
window_length = 51  # Adjust window size (odd number recommended)
poly_order = 3  # Adjust polynomial order (controls smoothness)

# Apply Savitzky-Golay filter to each data series
incident_voltage_filtered = savgol_filter(incident_voltage, window_length, poly_order)
reflected_voltage_filtered = savgol_filter(reflected_voltage, window_length, poly_order)
transmitted_voltage_filtered = savgol_filter(transmitted_voltage, window_length, poly_order)

# Conversion of Voltage to Strain using the provided relation
strain_incident = 1.53e-3 * incident_voltage_filtered
strain_reflected = 1.53e-3 * reflected_voltage_filtered
strain_transmitted = 1.53e-3 * transmitted_voltage_filtered

# Calculate particle velocities at specimen/input-bar and specimen/output-bar interfaces
cb = np.sqrt(Eb / rho_b)  # Bar wave speed
v1 = cb * (strain_incident - strain_reflected)
v2 = cb * strain_transmitted

# Calculate mean axial strain rate in the specimen
es_dot = (v1 - v2) / lo

# Integrate strain rate to get nominal strain using cumulative_trapezoid from scipy.integrate
es = cumulative_trapezoid(es_dot, time_data, initial=0)

# Calculate nominal stress in the specimen
Ss = (Eb * Ab / As) * transmitted_voltage_filtered

# Calculate true strain using the formula: εs(t) = -ln(1 - es(t))
epsilon_tolerance = 1e-10  # Small constant to prevent division by zero
es_safe = np.clip(es, epsilon_tolerance, 1 - epsilon_tolerance)  # Clip es to ensure it remains within valid range
true_strain = -np.log(1 - es_safe)

# Calculate true stress using the formula: σs(t) = Ss(t) * (1 - es(t))
true_stress = Ss * (1 - es)

# Plot the results
plt.figure(figsize=(12, 8))

# Plot filtered voltage data
plt.subplot(2, 1, 1)
plt.plot(time_data, incident_voltage_filtered, label="Incident Voltage (Filtered)")
plt.plot(time_data, reflected_voltage_filtered, label="Reflected Voltage (Filtered)")
plt.plot(time_data, transmitted_voltage_filtered, label="Transmitted Voltage (Filtered)")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.title("Filtered Voltage vs Time")
plt.grid(True)
plt.legend()

# Plot strain data
plt.subplot(2, 1, 2)
plt.plot(time_data, strain_incident, label="Incident Strain")
plt.plot(time_data, strain_reflected, label="Reflected Strain")
plt.plot(time_data, strain_transmitted, label="Transmitted Strain")
plt.xlabel("Time (ms)")
plt.ylabel("Strain")
plt.title("Strain vs Time")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Plot stress-strain curve
plt.figure(figsize=(8, 6))
plt.plot(es, Ss, color='blue', linewidth=2)
plt.xlabel("Nominal Strain")
plt.ylabel("Nominal Stress (Pa)")
plt.title("Stress-Strain Curve")
plt.grid(True)
plt.show()

# Plot True stress-strain curve
plt.figure(figsize=(8, 6))
plt.plot(true_strain, true_stress, color='red', linewidth=2, label='True Stress-Strain')
plt.xlabel("True Strain")
plt.ylabel("True Stress (Pa)")
plt.title("True Stress-Strain Curve")
plt.grid(True)
plt.legend()
plt.show()
