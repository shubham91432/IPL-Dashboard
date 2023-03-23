import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dataset_reader

st.set_page_config(page_title="Toss")

mathces = dataset_reader.get_matches_data()
delivery = dataset_reader.get_deliveries_data()

st.title("Indian Premier League (Cricket)")

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Matches Dataset")

st.dataframe(mathces)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Toss Decision across Season")

fig, ax = plt.subplots(figsize=(10,6))
sns.countplot(x='season',hue='toss_decision',data=mathces)
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Maximum Toss Winner")

ax=mathces['toss_winner'].value_counts().plot.bar(width=0.9,color=sns.color_palette('RdYlGn',20))
for p in ax.patches:
  ax.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()+1))
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Is Toss Winner also a Match Winner")

fig, ax = plt.subplots(figsize=(10,6))
df=mathces[mathces['toss_winner']==mathces['winner']]
slices=[len(df),(577-len(df))]
labels=['yes','no']
plt.pie(slices,labels=labels,startangle=90,shadow=True,explode=(0,0.05),autopct='%1.1f%%',colors=['r','g'])

plt.title("Is Toss Winner also a Match Winner")
st.pyplot(fig)