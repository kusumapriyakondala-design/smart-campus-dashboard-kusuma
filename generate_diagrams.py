import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("campus_data.csv")
output_dir = os.path.abspath(".")

# Attendance Bar Chart
fig1, ax1 = plt.subplots()
ax1.bar(df["Department"], df["Attendance"])
ax1.set_title("Department-wise Attendance")
ax1.set_ylabel("Attendance (%)")
fig1.savefig(os.path.join(output_dir, "attendance_chart.png"))

# Energy Line Chart
fig2, ax2 = plt.subplots()
ax2.plot(df["Department"], df["Energy"], marker='o')
ax2.set_title("Energy Consumption")
ax2.set_ylabel("kWh")
fig2.savefig(os.path.join(output_dir, "energy_chart.png"))

# Student Pie Chart
fig3, ax3 = plt.subplots()
ax3.pie(df["Students"], labels=df["Department"], autopct='%1.1f%%')
ax3.set_title("Student Distribution")
fig3.savefig(os.path.join(output_dir, "student_distribution.png"))

# Fees Bar Chart
fig4, ax4 = plt.subplots()
ax4.bar(df["Department"], df["Fees_Collected"])
ax4.set_title("Fees Collection")
ax4.set_ylabel("Amount (Rs)")
fig4.savefig(os.path.join(output_dir, "fees_collection.png"))

print("Charts successfully generated!")
