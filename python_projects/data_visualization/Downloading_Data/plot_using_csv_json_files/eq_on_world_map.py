import json
from plotly.graph_objs import Scattergeo, Layout
# from plotly.graph_objs import scattergeo, layout
from plotly import offline

filename = "Data\\sample_json_files\\eq_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data["features"]
mags,longs,lats = [],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    long = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)
# Map the eathquakes
datas = [{
    'type': "scattergeo",
    'lon': longs,
    'lat': lats,
    'marker':{
        'size':[3*mag for mag in mags],
    },
}]
# datas = [scattergeo(lon = longs, lat = lats)] question1
my_layout = Layout(title = 'Global Earthquakes')
# my_layout = layout(title = 'Global Earthquakes') question 2
fig = {'data': datas, "layout":my_layout}
offline.plot(fig,filename="global_eathqakes_plot2.html")