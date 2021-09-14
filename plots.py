import pandas as pd
import plotly.express as px
data = pd.read_csv("datasets/android-games.csv")
# Game Categories
games_cat = px.histogram(data, x='category', barmode='group', title="Number of Games by Category")
games_cat.update_layout(xaxis={'categoryorder':'total descending'})

# Total Ratings
data = data.rename(columns={'total ratings':'Total_ratings'})

# Making installs into numerical values
def in_thousand(inst):
    if inst == '500.0 k':
        return '0.5 M' 
    elif inst == '100.0 k':
        return '0.1 M'
    else:
        return inst
data['installs'] = data['installs'].apply(in_thousand)
data['installs'] = data['installs'].str.replace('M', '').str.strip().astype('float')
data = data.rename(columns={'installs': 'installs_in_million'})

# Paid and free games
paid_free = data['paid'].value_counts()
label = ['Free', 'Paid']
paid_free_games = px.pie(paid_free, values=data['paid'].value_counts().values, names=label, title='Paid & Free Games')
paid_free_games.update_traces(textposition='inside', textinfo='percent+label')

# Total Ratings by Category
total_ratings_by_category = data.groupby('category')['Total_ratings'].mean()
ratings_by_cat = px.bar(total_ratings_by_category, x=total_ratings_by_category.index, y=total_ratings_by_category.values, labels={'y':'Total_Ratings'}, title='Total Ratings by Category')
ratings_by_cat.update_layout(xaxis={'categoryorder':'total descending'})

# Number of Game Installations by Game Category
install_by_category = data.groupby('category')['installs_in_million'].mean()
install_in_million_by_cat = px.bar(install_by_category, x= install_by_category.index, y=install_by_category.values, labels={'y':'Install in Millions'}, title='Number of Installs(in millions) By Category')
install_in_million_by_cat.update_layout(xaxis={'categoryorder':'total descending'})

# Growth in 30 days by Category
growth_by_category_30 = data.groupby('category')['growth (30 days)'].mean()
growth_30_by_cat = px.bar(growth_by_category_30, x= growth_by_category_30.index, y=growth_by_category_30, labels={'y':'Growth in 30 days'}, title='Growth of each Category in 30 days')
growth_30_by_cat.update_layout(xaxis={'categoryorder':'total descending'})

# Growth in 60 days by Category
growth_by_category_60 = data.groupby('category')['growth (60 days)'].mean()
growth_60_by_cat = px.bar(growth_by_category_60, x= growth_by_category_60.index, y=growth_by_category_60, labels={'y':'Growth in 60 days'}, title='Growth of each Category in 60 days')
growth_60_by_cat.update_layout(xaxis={'categoryorder':'total descending'})

# Top 3 Games by Category and Their Total Ratings
top_ranked_games = data[data['rank']<4][['rank','title','category', 'Total_ratings', 'installs_in_million', '5 star ratings']]
top3_ranked_ratings = px.scatter(top_ranked_games, y= 'title', x='Total_ratings', hover_data = top_ranked_games[['category','rank']], color='category', title = "Top 3 Games by Their Total Ratings", height=1000)

# Top 20 Games by Category and Their Installs
top_20 = data.sort_values(by='installs_in_million', ascending=False).head(20)
top20_ranked_installs = px.bar(top_20, x= 'title', y='installs_in_million', hover_data = top_20[['5 star ratings']], color='category', title = "Top 20 Games by Their Installs", width=1000, height=600)
top20_ranked_installs.update_layout(xaxis={'categoryorder':'total descending'})
