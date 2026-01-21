import folium
from folium.plugins import MarkerCluster, MiniMap
from geopy.distance import geodesic 


center_coords = [43.3177, 45.6949]


locations = [
    {"name": "Грозный-Сити", "coords": [43.3151, 45.6941], "type": "Culture", "color": "blue"},
    {"name": "ТЦ Грозный Молл", "coords": [43.3160, 45.6910], "type": "Shop", "color": "red"},
    {"name": "Ахмат Арена", "coords": [43.3245, 45.7265], "type": "Sport", "color": "green"},
    {"name": "Цветочный парк", "coords": [43.3145, 45.6935], "type": "Park", "color": "orange"}
]


my_map = folium.Map(location=center_coords, zoom_start=15, tiles='Cartodb Positron')
marker_cluster = MarkerCluster().add_to(my_map)


for place in locations:

    distance = geodesic(center_coords, place["coords"]).meters
    
  
    if distance < 1000:
        dist_text = f"{int(distance)} м"
    else:
        dist_text = f"{round(distance/1000, 1)} км"


    folium.Marker(
        location=place["coords"],
        popup=folium.Popup(f"<b>{place['name']}</b><br>Тип: {place['type']}<br>📏 До центра: {dist_text}", max_width=250),
        icon=folium.Icon(color=place["color"], icon='info-sign')
    ).add_to(marker_cluster)


folium.Circle(
    location=center_coords,
    radius=500,
    color='green',
    fill=True,
    fill_opacity=0.1,
    popup='Центральный район'
).add_to(my_map)


folium.Marker(center_coords, popup="Центр: Сердце Чечни", icon=folium.Icon(color='orange', icon='star')).add_to(my_map)


minimap = MiniMap(toggle_display=True)
my_map.add_child(minimap)


my_map.save("/Users/muhammad/Desktop/index.html")

print(f"Готово! Версия 3.0 запущена. Просчитано объектов: {len(locations)}")

