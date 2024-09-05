#Sortables https://github.com/ohtaman/streamlit-sortables
import streamlit as st
from streamlit_sortables import sort_items
import folium
from folium.plugins import Draw
import pandas as pd

from streamlit_folium import st_folium

# Create a session object for the two lists
if 'plan_list' not in st.session_state:
    st.session_state['plan_list'] = ["Louvre Museum"]


#Make a dataframe that has the locations.  This will later be used by a db.
df_columns=["place","place_lat","place_long"] #Keep it simple for now.
row_1=["Eifel Tower",48.8584, 2.2945]
row_2=["Notre Dame Cathedral",48.8530,2.3499]
row_3=["Louvre Museum",48.8606, 2.3376]
row_4=["Charles DeGaule Airport",49.0079, 2.5508]
places_df=pd.DataFrame([row_1,row_2,row_3,row_4],columns=df_columns)
st.write(places_df)
st.write(places_df.at[0,'place'])

# Make a list of places that you want to show then make a subset from the dataframe.
#st.session_state.plan_list=["Notre Dame Cathedral","Louvre Museum"]
st.write("session plan list")
st.write(st.session_state.plan_list)
plan_list=["Notre Dame Cathedral","Louvre Museum"]

# Given the place list, return the rows of the df that match the place list.
plan_df = places_df[places_df['place'].isin(st.session_state.plan_list)]
#plan_df = places_df[places_df['place'].isin(plan_list)]

#filtered_df = df[df['Category'].isin(target_values)]
st.write("plan_df")
st.write(plan_df)

#Create a list of tupples from the dataframe that has lat, long
#  I think this crashes if plan_df is empty
# Check if DF is empty.  If it is give a default value for the city.   (Eifle Tower)
if plan_df.empty:
    plan_tuples=[(48.8584, 2.2945)] #Default Value for Map
else:
    plan_tuples = [(row['place_lat'], row['place_long']) for _, row in plan_df.iterrows()]
    

st.write(plan_tuples)

#Values held has tupples
eifel = (48.8584, 2.2945)
notre_dame = (48.8530,2.3499)
louvre=(48.8606, 2.3376)

start_place=plan_tuples[0]
st.write(start_place[0])
# center on Liberty Bell, add marker
#m = folium.Map(location=[48.8584, 2.2945], zoom_start=18)
# Smaller number is farther out.  18 is at block level
m = folium.Map(location=[start_place[0],start_place[1]], zoom_start=14) 

# Loop through the plan_df and add markers to the map
for index, row in plan_df.iterrows():
    folium.Marker(location=[row['place_lat'],row['place_long']],popup=row['place']).add_to(m)

#Add the lines from the places to the map.
folium.PolyLine(
#    locations=[eifel, notre_dame,louvre],
    locations=[plan_tuples],
    color='red',
    weight=2
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)

#This is default values for the two sorting columns

temp_origional=["Lourve","Notre Dame"]

# A list of dictionaries.
original_items = [
#    {'header': 'Itinerary',  'items': ['Lourve', 'Arc d Triumph', 'Notre Dame']},
    {'header': 'Itinerary',  'items': temp_origional},
    {'header': 'Maybe', 'items': ['Hotel', 'Latin Quarter', 'Airport','Charles de Gaul Station']}
]


#sorted_items = sort_items(original_items, multi_containers=True)
# sort_items returns a list that must be parsed.
sorted_list=sort_items(original_items, multi_containers=True)
st.session_state.plan_list=sorted_list[0]['items']

st.write(sorted_list[0]['items'])

temp_list=["box","House"]
st.write(temp_list)
st.write(st.session_state.plan_list)


#st.write(f'original_items: {original_items}')
#st.write(f'sorted_items: {sorted_items}')
#temp=sorted_items[0]['items'][0]
#st.write(temp)
