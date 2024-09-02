#Sortables https://github.com/ohtaman/streamlit-sortables
import streamlit as st
from streamlit_sortables import sort_items
import folium
from folium.plugins import Draw


from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[48.8584, 2.2945], zoom_start=16)
folium.Marker(
    [48.8584, 2.2945], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

eifel = (48.8584, 2.2945)
notre_dame = (48.8530,2.3499)

folium.PolyLine(
    locations=[eifel, notre_dame],
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
