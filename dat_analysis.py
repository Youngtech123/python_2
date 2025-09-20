import pandas as pd 
import matplotlib.pyplot as plt
from collections import Counter
# Load dataset
df = pd.read_csv("metadata.csv")
#check rows 
print("Shape:", df.shape)
#Examine the first rows 
print(df.head(5))
# check if there are missing values 
print(df.isnull().sum().head(15))
#check datatypes in our table 
print(df.dtypes.head(15))
#Basic stats of our table 
print(df.describe())

#part Two 
#check to see colums with missing values 
print(df.isnull().sum())
# Drop columns with too many missing values (not useful for analysis)
df_clean = df.drop(columns=[
    "sha", "pmcid", "pubmed_id", "mag_id", 
    "who_covidence_id", "arxiv_id", "pdf_json_files", 
    "pmc_json_files", "url", "s2_id"
])

# Drop rows with no title AND no abstract
df_clean = df_clean.dropna(subset=["title", "abstract"], how="all")

# Drop rows with missing publish_time (since date is important for trends)
df_clean = df_clean.dropna(subset=["publish_time"])

print("Cleaned dataset shape:", df_clean.shape) 
# Convert publish_time to datetime
df_clean["publish_time"] = pd.to_datetime(df_clean["publish_time"], errors="coerce")

# Extract publication year
df_clean["publish_year"] = df_clean["publish_time"].dt.year

# Create a new column: abstract word count
df_clean["abstract_word_count"] = df_clean["abstract"].fillna("").apply(lambda x: len(x.split()))

print(df_clean[["publish_time", "publish_year", "abstract_word_count"]].head())

#Part Three 
# Count papers by year
papers_per_year = df_clean["publish_year"].value_counts().sort_index()

print(papers_per_year)

# Plot number of publications over time
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
papers_per_year.plot(kind="line", marker="o")
plt.title("Number of Publications Over Time")
plt.xlabel("Publication Year")
plt.ylabel("Number of Papers")
plt.grid(True)
plt.show()

# Count papers by journal
top_journals = df_clean["journal"].value_counts().head(10)

print("Top Journals:\n", top_journals)

# Plot top journals
plt.figure(figsize=(10,6))
top_journals.plot(kind="bar")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Journal")
plt.ylabel("Number of Papers")
plt.xticks(rotation=45, ha="right")
plt.show()

# Combine all titles into one string
all_titles = " ".join(df_clean["title"].dropna().astype(str))

# Split into words (convert to lowercase for consistency)
words = all_titles.lower().split()

# Remove very common short words (stopwords)
stopwords = {"the", "and", "of", "in", "to", "a", "for", "on", "with", 
             "by", "from", "at", "is", "an", "as", "are", "that"}

filtered_words = [w for w in words if w not in stopwords and len(w) > 3]

# Count the most common words
word_counts = Counter(filtered_words).most_common(20)

# Separate words and counts for plotting
labels, values = zip(*word_counts)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(labels, values, color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.title("Top 20 Most Frequent Words in Paper Titles")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()

# Count papers by source
papers_by_source = df_clean["source_x"].value_counts().head(10)  # top 10 sources

# Plot as bar chart
plt.figure(figsize=(10,6))
papers_by_source.plot(kind="bar", color="lightgreen")
plt.title("Top 10 Sources of COVID-19 Research Papers")
plt.xlabel("Source")
plt.ylabel("Number of Papers")
plt.xticks(rotation=45, ha="right")
plt.show()

df_clean.to_csv("metadata_clean.csv", index=False)
print("Cleaned dataset saved as metadata_clean.csv")
