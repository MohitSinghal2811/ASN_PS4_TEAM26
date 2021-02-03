from django.contrib.gis import admin
from .models import Anchors, RealTimeVessel, Trajectory, AnomalyDay1, AnomalyDay2, AnomalyDay3, AnomalyDay4, Fishermen
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Anchors, LeafletGeoAdmin)
admin.site.register(RealTimeVessel, LeafletGeoAdmin)
admin.site.register(Trajectory, LeafletGeoAdmin)
admin.site.register(AnomalyDay1, LeafletGeoAdmin)
admin.site.register(AnomalyDay2, LeafletGeoAdmin)
admin.site.register(AnomalyDay3, LeafletGeoAdmin)
admin.site.register(AnomalyDay4, LeafletGeoAdmin)
admin.site.register(Fishermen, LeafletGeoAdmin)
