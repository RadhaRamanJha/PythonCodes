import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "Data\\sample_json_files\\eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data["features"]
mags,longs,lats,howver_texts = [],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    long = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    description = eq_dict["properties"]["title"]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)
    howver_texts.append(description)
# Map the eathquakes
datas = [{
    'type': "scattergeo",
    'lon': longs,
    'lat': lats,
    'text':howver_texts,
    'marker':{
        'size':[3*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale' : True,
        'colorbar':{'title':'Magnitude'}
    },
}]
my_layout = Layout(title = 'Global Earthquakes',title_x = 0.5)
fig = {'data': datas, "layout":my_layout}
offline.plot(fig,filename="longer_global_eathqakes_plot.html")