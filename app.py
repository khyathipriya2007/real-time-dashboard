import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Real-Time Dashboard", layout="wide")

# Title
st.title("📊 Real-Time Sales Dashboard")

# Read CSV
df = pd.read_csv("data.csv")

# Show Dataset
st.subheader("Sales Data")
st.dataframe(df)

# Charts
st.subheader("Monthly Sales")
st.line_chart(df.set_index("Month")["Sales"])

st.subheader("Monthly Profit")
st.bar_chart(df.set_index("Month")["Profit"])

# Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", df["Sales"].sum())

with col2:
    st.metric("Total Profit", df["Profit"].sum())

# Refresh Button
if st.button("Refresh Dashboard"):
    st.success("Dashboard Updated Successfully!") 