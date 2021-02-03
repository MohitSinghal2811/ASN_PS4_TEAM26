from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Anchors, RealTimeVessel, Trajectory, Anomaly, AnomalyDay1, AnomalyDay2, AnomalyDay3, AnomalyDay4, AnomalyDay6

anomaly_mapping = {
    'unnamed': 'Unnamed:_0',
    'mmsi': 'MMSI',
    'datetime': 'DateTime',
    'lat': 'LAT',
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

anomaly_shp = "E:/blue_economy/geodjango/world/data/anomaly_day6/CSV.shp"

def run(verbose=True):
    print("HI")
    lm = LayerMapping(AnomalyDay6, anomaly_shp, anomaly_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)



# run() 