import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Smart Campus Dashboard", layout="wide")

# Title
st.title("🏫 Smart Campus Data Analytics Dashboard")

# Load Data
df = pd.read_csv("campus_data.csv")

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
dept = st.sidebar.multiselect("Select Department", df["Department"], default=df["Department"])

filtered_df = df[df["Department"].isin(dept)]

# KPIs
st.subheader("📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", int(filtered_df["Students"].sum()))
col2.metric("Avg Attendance", f"{filtered_df['Attendance'].mean():.1f}%")
col3.metric("Total Energy", int(filtered_df["Energy"].sum()))
col4.metric("Fees Collected", f"₹{filtered_df['Fees_Collected'].sum():,}")

# Show Data
st.subheader("📋 Dataset")
st.dataframe(filtered_df)

# Charts
st.subheader("📈 Visual Analytics")

# Attendance Bar Chart
fig1, ax1 = plt.subplots()
ax1.bar(filtered_df["Department"], filtered_df["Attendance"])
ax1.set_title("Department-wise Attendance")
ax1.set_ylabel("Attendance (%)")
st.pyplot(fig1)

# Energy Line Chart
fig2, ax2 = plt.subplots()
ax2.plot(filtered_df["Department"], filtered_df["Energy"], marker='o')
ax2.set_title("Energy Consumption")
ax2.set_ylabel("kWh")
st.pyplot(fig2)

# Student Pie Chart
fig3, ax3 = plt.subplots()
ax3.pie(filtered_df["Students"], labels=filtered_df["Department"], autopct='%1.1f%%')
ax3.set_title("Student Distribution")
st.pyplot(fig3)

# Fees Bar Chart
fig4, ax4 = plt.subplots()
ax4.bar(filtered_df["Department"], filtered_df["Fees_Collected"])
ax4.set_title("Fees Collection")
ax4.set_ylabel("Amount (₹)")
st.pyplot(fig4)

# Footer
st.markdown("---")
st.write("Developed as part of Smart Campus Project 🚀")
