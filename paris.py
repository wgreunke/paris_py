#Sortables https://github.com/ohtaman/streamlit-sortables
import streamlit as st
from streamlit_sortables import sort_items
import folium
from folium.plugins import Draw


from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

tokyo = (35.6895, 139.6917)
maui = (20.7967, -156.3319)

folium.PolyLine(
    locations=[tokyo, maui],
    color='green',
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
