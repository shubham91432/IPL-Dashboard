import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dataset_reader

st.set_page_config(page_title="Runs")

mathces = dataset_reader.get_matches_data()
delivery = dataset_reader.get_deliveries_data()

st.title("Indian Premier League (Cricket)")

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)


st.subheader("Deliveries Dataset")
st.dataframe(delivery)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Runs across Season")

fig, ax = plt.subplots(figsize=(10,6))
mathces_played_byteams=pd.concat([mathces['team1'],mathces['team2']])
mathces_played_byteams=mathces_played_byteams.value_counts().reset_index()
mathces_played_byteams.columns=['Team','Total Mathces']
mathces_played_byteams['wins']=mathces['winner'].value_counts().reset_index()['winner']
mathces_played_byteams.set_index('Team',inplace=True)
runs_per_over = delivery.pivot_table(index=['over'],columns='batting_team',values='total_runs',aggfunc=sum)
runs_per_over[(mathces_played_byteams[mathces_played_byteams['Total Mathces']>50].index)].plot(color=["b", "r", "#Ffb6b2", "g",'brown','y','#6666ff','black','#FFA500']) #plotting graphs for teams that have played more than 100 matches
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.xticks(x)
plt.ylabel('total runs scored')
fig=plt.gcf()
fig.set_size_inches(16,10)
plt.title("Run per over by team across season")
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Player of the Match")

fig, ax = plt.subplots(figsize=(10,6))
#the code used is very basic but gets the job done easily
ax = mathces['player_of_match'].value_counts().head(10).plot.bar(width=.8, color=sns.color_palette('inferno',10))  #counts the values corresponding 
# to each batsman and then filters out the top 10 batsman and then plots a bargraph 
ax.set_xlabel('player of match') 
ax.set_ylabel('count')
for p in ax.patches:
  ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()+0.25))
st.pyplot(fig)


st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Chances of Scoring 200+ Runs")

fig, ax = plt.subplots(figsize=(10,6))
high_scores=delivery.groupby(['match_id', 'inning','batting_team','bowling_team'])['total_runs'].sum().reset_index()
high_scores1=high_scores[high_scores['inning']==1]
high_scores2=high_scores[high_scores['inning']==2]
high_scores1=high_scores1.merge(high_scores2[['match_id','inning', 'total_runs']], on='match_id')
high_scores1.rename(columns={'inning_x':'inning_1','inning_y':'inning_2','total_runs_x':'inning1_runs','total_runs_y':'inning2_runs'},inplace=True)
high_scores1=high_scores1[high_scores1['inning1_runs']>=200]
high_scores1['is_score_chased']=1
high_scores1['is_score_chased'] = np.where(high_scores1['inning1_runs']<=high_scores1['inning2_runs'], 'yes', 'no')
slices=high_scores1['is_score_chased'].value_counts().reset_index().is_score_chased
list(slices)
labels=['target not chased','target chased']
plt.pie(slices,labels=labels,colors=['#1f2ff3', '#0fff00'],startangle=90,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
fig = plt.gcf()
fig.set_size_inches(6,6)
plt.legend()
plt.title("Chance of chasing 200+ score")
st.pyplot(fig)