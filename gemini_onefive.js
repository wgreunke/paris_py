```javascript
import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const App = () => {
  const [plan, setPlan] = useState([
    { id: '1', name: 'Golden Gate Bridge', lat: 37.8199, lng: -122.4783 },
    { id: '2', name: 'Alcatraz Island', lat: 37.8269, lng: -122.423 },
  ]);
  const [maybe, setMaybe] = useState([
    { id: '3', name: 'Fisherman's Wharf', lat: 37.8098, lng: -122.411 },
    { id: '4', name: 'Lombard Street', lat: 37.8027, lng: -122.419 },
  ]);

  const handleOnDragEnd = (result) => {
    if (!result.destination) return;

    const items = result.destination.droppableId === 'plan' ? plan : maybe;
    const [reorderedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reorderedItem);

    if (result.destination.droppableId === 'plan') {
      setPlan([...items]);
    } else {
      setMaybe([...items]);
    }
  };

  return (
    <div className="app">
      <h1>Plan Your Trip</h1>
      <div className="container">
        <DragDropContext onDragEnd={handleOnDragEnd}>
          <Droppable droppableId="plan">
            {(provided) => (
              <div
                ref={provided.innerRef}
                {...provided.droppableProps}
                className="list-container"
              >
                <h2>Plan</h2>
                {plan.map((place, index) => (
                  <Draggable key={place.id} draggableId={place.id.toString()} index={index}>
                    {(provided) => (
                      <div
                        ref={provided.innerRef}
                        {...provided.draggableProps}
                        {...provided.dragHandleProps}
                        className="list-item"
                      >
                        {place.name}
                      </div>
                    )}
                  </Draggable>
                ))}
                {provided.placeholder}
              </div>
            )}
          </Droppable>
          <Droppable droppableId="maybe">
            {(provided) => (
              <div
                ref={provided.innerRef}
                {...provided.droppableProps}
                className="list-container"
              >
                <h2>Maybe</h2>
                {maybe.map((place, index) => (
                  <Draggable key={place.id} draggableId={place.id.toString()} index={index}>
                    {(provided) => (
                      <div
                        ref={provided.innerRef}
                        {...provided.draggableProps}
                        {...provided.dragHandleProps}
                        className="list-item"
                      >
                        {place.name}
                      </div>
                    )}
                  </Draggable>
                ))}
                {provided.placeholder}
              </div>
            )}
          </Droppable>
        </DragDropContext>
      </div>
      <div className="map-container">
        <MapContainer center={[37.7749, -122.4194]} zoom={12}>
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {plan.map((place) => (
            <Marker key={place.id} position={[place.lat, place.lng]}>
              <Popup>{place.name}</Popup>
            </Marker>
          ))}
        </MapContainer>
      </div>
    </div>
  );
};

export default App;
```

**Explanation:**

1. **Import necessary libraries:**
   - `react` and `useState` for managing component state.
   - `react-beautiful-dnd` for drag-and-drop functionality.
   - `react-leaflet` for displaying the map.

2. **Define initial state:**
   - `plan` and `maybe` arrays store the places with their names, latitude, and longitude.

3. **`handleOnDragEnd` function:**
   - This function is triggered when a drag-and-drop operation ends.
   - It identifies the source and destination lists and updates the corresponding state arrays.

4. **`DragDropContext`:**
   - Wraps the sortable lists to enable drag-and-drop functionality.
   - `onDragEnd` prop is set to the `handleOnDragEnd` function.

5. **`Droppable`:**
   - Defines each sortable list (plan and maybe).
   - `droppableId` is used to identify the list.

6. **`Draggable`:**
   - Defines each draggable item within the list.
   - `draggableId` is set to the item's ID.
   - `index` is used for positioning within the list.

7. **`MapContainer`:**
   - Displays the map using Leaflet.
   - `center` prop sets the initial map view.
   - `zoom` prop sets the initial zoom level.

8. **`TileLayer`:**
   - Adds a base map layer from OpenStreetMap.

9. **`Marker`:**
   - Places markers on the map for each place in the `plan` array.
   - `position` prop is set to the place's latitude and longitude.
   - `Popup` displays the place name when the marker is clicked.

**To run this app:**

1. Make sure you have Node.js and npm installed.
2. Create a new React project using `create-react-app`:
   ```bash
   npx create-react-app my-trip-planner
   ```
3. Install the required packages:
   ```bash
   npm install react-beautiful-dnd react-leaflet leaflet
   ```
4. Replace the contents of `src/App.js` with the code provided above.
5. Start the development server:
   ```bash
   npm start
   ```

This will open the app in your browser, allowing you to drag and drop places between the "Plan" and "Maybe" lists, and see the selected places displayed on the map.
