import folium
from streamlit_folium import folium_static

def basic_map_widget(lat,lon):
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup="Requested Location").add_to(m)
    st_data = folium_static(m)