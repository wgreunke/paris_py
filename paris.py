#Sortables https://github.com/ohtaman/streamlit-sortables
import streamlit as st
from streamlit_sortables import sort_items
import folium
from folium.plugins import Draw

st.title("Draw a Line on a Map")

# Get user input for the map center
center_lat = st.number_input("Center Latitude", value=37.7749)
center_lng = st.number_input("Center Longitude", value=122.4194)

# Create the map
m = folium.Map(location=[center_lat, center_lng], zoom_start=12)

# Add the Draw plugin to the map

tokyo = (35.6895, 139.6917)
maui = (20.7967, -156.3319)

if maui[1] < 0:
    maui = (maui[0], maui[1] + 360)

# Calculate the midpoint
midpoint = ((tokyo[0] + maui[0]) / 2, (tokyo[1] + maui[1]) / 2)

# Create a map centered around the midpoint
m = folium.Map(location=midpoint, zoom_start=2)

# Draw a line connecting Tokyo and Maui
folium.PolyLine(
    locations=[tokyo, maui],
    color='green',
    weight=2
).add_to(m)

# Add markers for Tokyo and Maui
folium.Marker(location=tokyo, popup='Tokyo').add_to(m)
folium.Marker(location=maui, popup='Maui').add_to(m)

# Display the map
st.folium_map(m)



original_items = [
    {'header': 'Itinerary',  'items': ['Lourve', 'Arc d Triumph', 'Notre Dame']},
    {'header': 'Maybe', 'items': ['Hotel', 'Latin Quarter', 'Airport','Charles de Gaul Station']}
]

sorted_items = sort_items(original_items, multi_containers=True)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
temp=sorted_items[0]['items'][0]
st.write(temp)
