import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset 
df = pd.read_csv("metadata.csv")

# Title and description
st.title("CORD-19 Data Explorer")
st.write("This app allows you to explore COVID-19 research papers interactively.")

# Show sample of the data
st.subheader("Sample of the Data")
st.write(df.head())

# Add a year column 
df['year'] = pd.to_datetime(df['publish_time'], errors="coerce").dt.year

# Interactive widget: Year range slider
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filter data by selected year range
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Dropdown to select a column for visualization
column_option = st.selectbox("Select a column to visualize", ["year", "source_x", "journal"])

# Visualization
st.subheader("Visualization")
if column_option == "year":
    counts = filtered_df['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(counts.index, counts.values)
    ax.set_title("Publications by Year")
    st.pyplot(fig)

elif column_option == "source_x":
    counts = filtered_df['source_x'].value_counts().head(10)
    fig, ax = plt.subplots()
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Sources")
    st.pyplot(fig)

elif column_option == "journal":
    counts = filtered_df['journal'].value_counts().head(10)
    fig, ax = plt.subplots()
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Journals")
    st.pyplot(fig)

# Display shape of filtered dataset
st.subheader("Filtered Data Info")
st.write(f"Number of records in selected range: {filtered_df.shape[0]}")
