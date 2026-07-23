import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Netflix.csv")
print(df.head())
print(df.tail())
print("Shape of Dataset:",df.shape)
print("\nColumn Names:",df.columns)
df.info()
print("Missing Values:",df.isnull().sum())
print(df.isnull().sum())
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")
print(df.isnull().sum())
print(df.duplicated().sum())


content_count = df['type'].value_counts()
print(content_count)

rating_count = df['rating'].value_counts()
print(rating_count.head(10))

country_count = df['country'].value_counts().head(10)
print(country_count)

genre_count = df["listed_in"].value_counts().head(10)
print(genre_count)

release_year_count = df["release_year"].value_counts().sort_index()
print(release_year_count)

director_count = df['director'].value_counts().head(10)
print(director_count)


content_count.plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()

rating_count.head(10).plot(kind='bar')
plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.show()

country_count.plot(kind='bar',figsize=(10,5))
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha='right')
plt.show()

genre_count.plot(kind='bar',figsize=(10,5))
plt.title("Top 10 Netflix Genre Categories")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha='right')
plt.show()

release_year_count.plot(kind='line',figsize=(12,5))
plt.title("Netflix content release over the years")
plt.xlabel("Release year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()

director_count.plot(kind='bar',figsize=(10,5))
plt.title("Top 10 Directors on Netflix")
plt.xlabel("Directors")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha='right')
plt.show()
