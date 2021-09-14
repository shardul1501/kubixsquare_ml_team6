import streamlit as st
import plots
st.set_page_config(layout='wide', page_title='Visualization of Android Games')
f = open('css/style.css', 'r')
st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
f.close()
st.markdown("# Visualization of Android Games on Play Store")
st.markdown('## By AI/ML Team 6')
options = ['--Select A Option--', 'No. of Games By Category', 'Total Ratings By Category', 'No. of Installs in Million By Category', 'Paid vs Free Games', 'Growth of Games by Category', 'Top 3 Most Rated Games In Each Category', 'Top 20 Most Installed Games In Each Category']
choice = options.index(st.selectbox('', options))
if choice == 1:
    st.plotly_chart(plots.games_cat)
if choice == 2:
    st.plotly_chart(plots.ratings_by_cat)
if choice == 3:
    st.plotly_chart(plots.install_in_million_by_cat)
if choice == 4:
    st.plotly_chart(plots.paid_free_games)
if choice == 5:
    # st.plotly_chart(plots.fig)
    st.plotly_chart(plots.growth_30_by_cat)
    st.plotly_chart(plots.growth_60_by_cat)
if choice == 6:
    st.plotly_chart(plots.top3_ranked_ratings)
if choice == 7:
    st.plotly_chart(plots.top20_ranked_installs)