import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HollywoodsMostProfitableStories.csv")

print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

print('missing values :')
print(df.isnull().sum())

df['Profitability'].fillna(df['Profitability'].mean(),inplace=True)

df['Rotten Tomatoes %'].fillna(df['Rotten Tomatoes %'].mean(),inplace=True)

df['Audience  score %'].fillna(df['Audience  score %'].mean(),inplace=True)

df = df.dropna(subset=['Lead Studio'])

print(df.isnull().sum())

print('duplicate values :')

print(df.duplicated().sum())

new_set = df.to_csv('cleaned_movie_set.csv',index=False)

movies_by_genre = df.groupby('Genre')['Film'].count().reset_index()

print(movies_by_genre)

sns.barplot(data=movies_by_genre,x='Genre',y='Film',color='red')
plt.title('movie count by genre')
plt.xlabel('genre')
plt.ylabel('movies count')
plt.show()

#Top2 Genres by revenue

genre_gross = df.groupby('Genre')['Worldwide Gross'].sum()

print(genre_gross)

top_genres_by_revenue = genre_gross.sort_values(ascending=False).head(5)

print(top_genres_by_revenue)

#plot

top_genres_by_revenue.plot(kind='pie',autopct='%1.1f%%',startangle=90,title='top 5 genres')
plt.show()


revenue_by_year = df.groupby('Year')['Worldwide Gross'].sum()

print(revenue_by_year)

revenue_by_year.plot(kind='barh', color='purple',title='revneue by year')
plt.xlabel('revenue')
plt.ylabel('year')
plt.show()

sns.boxplot(x='Genre',y='Profitability',data=df,palette='Set2')
plt.show()

numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Generate a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


