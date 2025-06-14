import csv
import random
import time
import json
from datetime import datetime
import matplotlib.pyplot as plt

csv_filename = "temperature_log.csv"
json_filename = "temperature_log.json"
fieldnames = ['Timestamp', 'Temperature (°C)']
temperature_data = []

with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(10):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(20.0, 35.0), 2)
        temperature_data.append({'Timestamp': timestamp, 'Temperature (°C)': temperature})
        writer.writerow({'Timestamp': timestamp, 'Temperature (°C)': temperature})

        if temperature > 30.0:
            print(f"⚠️ ALERT: High Temperature Detected at {timestamp} - {temperature}°C")
        else:
            print(f"{i+1}. Logged: {timestamp} - {temperature}°C")

        time.sleep(1)

with open(json_filename, mode='w') as json_file:
    json.dump(temperature_data, json_file, indent=4)

timestamps = [entry['Timestamp'] for entry in temperature_data]
temperatures = [entry['Temperature (°C)'] for entry in temperature_data]

plt.figure(figsize=(10, 5))
plt.plot(timestamps, temperatures, marker='o', color='blue')
plt.title("Simulated Temperature Readings")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_plot.png")
