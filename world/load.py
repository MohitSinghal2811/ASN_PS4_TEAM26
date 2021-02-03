from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Anchors, RealTimeVessel, Trajectory, Anomaly

anchors_mapping = {
    's2id': 's2id',
    'lat': 'lat',
    'lon': 'lon',
    'label': 'label',
    'sublabel': 'sublabel',
    'label_sour': 'label_sour',
    'iso3': 'iso3',
    'distance_f': 'distance_f',
    'drift_radi': 'drift_radi',
    'at_dock': 'at_dock',
    'geom': 'MULTIPOINT',
}

realtimevessel_mapping = {
    'mmsi': 'mmsi',
    'flag': 'flag',
    'lat': 'lat',
    'lon': 'lon',
    'fishing': 'fishing',
    'geartype': 'geartype',
    'geom': 'MULTIPOINT',
}


trajectory_mapping = {
    'mmsi': 'mmsi',
    'time': 'times',
    'distance_f': 'distance_f',
    'distance00': 'distance00',
    'speed': 'speed',
    'course': 'course',
    'lat': 'lat',
    'lon': 'lon',
    'is_fishing': 'is_fishing',
    'source': 'source',
    'geom': 'MULTIPOINT',
}

anomaly_mapping = {
    'col0': 'col0',
    'mmsi': 'MMSI',
    'lat': 'LAT',
    'datetime': 'DateTime',
    'lon': 'LON',
    'sog': 'SOG',
    'cog': 'COG',
    'heading': 'Heading',
    'vesselname': 'VesselName',
    'imo': 'IMO',
    'callsign': 'CallSign',
    'vesseltype': 'VesselType',
    'status': 'Status',
    'length': 'Length',
    'width': 'Width',
    'draft': 'Draft',
    'cargo': 'Cargo',
    'transcieve': 'Transcieve',
    'geom': 'MULTIPOINT',
}


anchors_shp = "C:/Users/lenovo/Desktop/blue_economy/geodjango/world/data/anchorage_mygeodata/anchorages_-clean-point.shp"
realtimevessels_shp = "E:/blue_economy/geodjango/world/data/real_time_vessels/CSV.shp"
trajectory_shp = "E:/blue_economy/geodjango/world/data/trajectory/CSV.shp"
anomaly_shp = "E:/blue_economy/geodjango/world/data/anomalies/CSV.shp"


def run(verbose=True):
    print("HI")
    lm = LayerMapping(RealTimeVessel, realtimevessels_shp, realtimevessel_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)



# run() 