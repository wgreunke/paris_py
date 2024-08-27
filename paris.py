#Sortables https://github.com/ohtaman/streamlit-sortables



import streamlit as st
from streamlit_sortables import sort_items

original_items = [
    {'header': 'Itinerary',  'items': ['Lourve', 'Arc d Triumph', 'Notre Dame']},
    {'header': 'Maybe', 'items': ['Hotel', 'Latin Quarter', 'Airport','Charles de Gaul Station']}
]

sorted_items = sort_items(original_items, multi_containers=True)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')

st.write(origional_items[0]['items'][0])
