#Sortables https://github.com/ohtaman/streamlit-sortables
import streamlit as st
from streamlit_sortables import sort_items
import folium
from folium.plugins import Draw

st.title("Draw a Line on a Map")

# Get user input for the map center
center_lat = st.number_input("Center Latitude", value=37.7749)
center_lng = st.number_input("Center Longitude", value=-122.4194)

# Create the map
m = folium.Map(location=[center_lat, center_lng], zoom_start=12)

# Add the Draw plugin to the map
draw = Draw(
    position="topleft",
    polyline=True,  # Enable drawing polylines (lines)
    circle=False,  # Disable drawing circles
    rectangle=False,  # Disable drawing rectangles
    polygon=False,  # Disable drawing polygons
    marker=False,  # Disable drawing markers
    edit_polyline=True,  # Allow editing of polylines
    edit_marker=False,  # Disable editing of markers
    edit_circle=False,  # Disable editing of circles
    edit_rectangle=False,  # Disable editing of rectangles
    edit_polygon=False,  # Disable editing of polygons
)
m.add_child(draw)

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
