#Sortables https://github.com/ohtaman/streamlit-sortables
import streamlit as st
from streamlit_sortables import sort_items
import folium
from folium.plugins import Draw
import pandas as pd

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[48.8584, 2.2945], zoom_start=16)
folium.Marker(
    [48.8584, 2.2945], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

#Make a dataframe that has the locations.  This will later be used by a db.
df_columns=["place","place_lat","place_long"] #Keep it simple for now.
row_1=["Eifel Tower",48.8584, 2.2945]
row_2=["Notre Dame Cathedral",48.8530,2.3499]
row_3=["Louvre Museum",48.8606, 2.3376]
places_df=pd.DataFrame([row_1,row_2,row_3],columns=df_columns)
st.write(places_df)
st.write(places_df.at[0,'place'])

#Create a list of tupples from the dataframe that has lat, long
places_tuples = [(row['place_lat'], row['place_long']) for _, row in places_df.iterrows()]
st.write(places_tuples)

#Values held has tupples
eifel = (48.8584, 2.2945)
notre_dame = (48.8530,2.3499)
louvre=(48.8606, 2.3376)


folium.PolyLine(
    locations=[eifel, notre_dame,louvre],
    color='red',
    weight=2
).add_to(m)


# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)


original_items = [
    {'header': 'Itinerary',  'items': ['Lourve', 'Arc d Triumph', 'Notre Dame']},
    {'header': 'Maybe', 'items': ['Hotel', 'Latin Quarter', 'Airport','Charles de Gaul Station']}
]

sorted_items = sort_items(original_items, multi_containers=True)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
temp=sorted_items[0]['items'][0]
st.write(temp)
