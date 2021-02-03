from django.contrib.gis.db import models

class Anchors(models.Model):
    s2id = models.CharField(max_length=80)
    lat = models.FloatField()
    lon = models.FloatField()
    label = models.CharField(max_length=80)
    sublabel = models.CharField(max_length=80, null = True)
    label_sour = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=80)
    distance_f = models.CharField(max_length=80, null = True)
    drift_radi = models.CharField(max_length=80, null = True)
    at_dock = models.CharField(max_length=80)
    geom = models.MultiPointField(srid=4326)


    def __str__(self):
        return self.s2id
    


class RealTimeVessel(models.Model):
    mmsi = models.FloatField(null = True)
    flag = models.CharField(max_length=254, null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    fishing = models.FloatField(null = True)
    geartype = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)


    def __str__(self):
        return str(self.mmsi)


class Anomaly(models.Model):
    col0 = models.BigIntegerField(null = True)
    mmsi = models.FloatField(null = True)
    datetime = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    sog = models.FloatField(null = True)
    cog = models.FloatField(null = True)
    heading = models.BigIntegerField(null = True)
    vesselname = models.CharField(max_length=254, null = True)
    imo = models.CharField(max_length=254, null = True)
    callsign = models.CharField(max_length=254, null = True)
    vesseltype = models.FloatField(null = True)
    status = models.FloatField(null = True)
    length = models.FloatField(null = True)
    width = models.FloatField(null = True)
    draft = models.FloatField(null = True)
    cargo = models.FloatField(null = True)
    transcieve = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)


class Trajectory(models.Model):
    mmsi = models.FloatField(null = True)
    time = models.FloatField(null = True)
    distance_f = models.FloatField(null = True)
    distance00 = models.FloatField(null = True)
    speed = models.FloatField(null = True)
    course = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    is_fishing = models.FloatField(null = True)
    source = models.CharField(max_length=254, null = True)
    vessel_typ = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)


class AnomalyDay1(models.Model):
    unnamed = models.BigIntegerField(null = True)
    mmsi = models.FloatField(null = True)
    datetime = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    sog = models.FloatField(null = True)
    cog = models.FloatField(null = True)
    heading = models.BigIntegerField(null = True)
    vesselname = models.CharField(max_length=254, null = True)
    imo = models.CharField(max_length=254, null = True)
    callsign = models.CharField(max_length=254, null = True)
    vesseltype = models.CharField(max_length=254, null = True)
    status = models.IntegerField(null = True)
    length = models.CharField(max_length=254, null = True)
    width = models.CharField(max_length=254, null = True)
    draft = models.CharField(max_length=254, null = True)
    cargo = models.CharField(max_length=254, null = True)
    transcieve = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)


class AnomalyDay2(models.Model):
    unnamed = models.BigIntegerField(null = True)
    mmsi = models.FloatField(null = True)
    datetime = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    sog = models.FloatField(null = True)
    cog = models.FloatField(null = True)
    heading = models.BigIntegerField(null = True)
    vesselname = models.CharField(max_length=254, null = True)
    imo = models.CharField(max_length=254, null = True)
    callsign = models.CharField(max_length=254, null = True)
    vesseltype = models.CharField(max_length=254, null = True)
    status = models.IntegerField(null = True)
    length = models.CharField(max_length=254, null = True)
    width = models.CharField(max_length=254, null = True)
    draft = models.CharField(max_length=254, null = True)
    cargo = models.CharField(max_length=254, null = True)
    transcieve = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)


class AnomalyDay3(models.Model):
    unnamed = models.BigIntegerField(null = True)
    mmsi = models.FloatField(null = True)
    datetime = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    sog = models.FloatField(null = True)
    cog = models.FloatField(null = True)
    heading = models.BigIntegerField(null = True)
    vesselname = models.CharField(max_length=254, null = True)
    imo = models.CharField(max_length=254, null = True)
    callsign = models.CharField(max_length=254, null = True)
    vesseltype = models.CharField(max_length=254, null = True)
    status = models.IntegerField(null = True)
    length = models.CharField(max_length=254, null = True)
    width = models.CharField(max_length=254, null = True)
    draft = models.CharField(max_length=254, null = True)
    cargo = models.CharField(max_length=254, null = True)
    transcieve = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)

    def __str__ (self):
        return self.datetime


class AnomalyDay4(models.Model):
    unnamed = models.BigIntegerField(null = True)
    mmsi = models.FloatField(null = True)
    datetime = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    sog = models.FloatField(null = True)
    cog = models.FloatField(null = True)
    heading = models.BigIntegerField(null = True)
    vesselname = models.CharField(max_length=254, null = True)
    imo = models.CharField(max_length=254, null = True)
    callsign = models.CharField(max_length=254, null = True)
    vesseltype = models.CharField(max_length=254, null = True)
    status = models.IntegerField(null = True)
    length = models.CharField(max_length=254, null = True)
    width = models.CharField(max_length=254, null = True)
    draft = models.CharField(max_length=254, null = True)
    cargo = models.CharField(max_length=254, null = True)
    transcieve = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)



class AnomalyDay6(models.Model):
    unnamed = models.BigIntegerField(null = True)
    mmsi = models.FloatField(null = True)
    datetime = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    lon = models.FloatField(null = True)
    sog = models.FloatField(null = True)
    cog = models.FloatField(null = True)
    heading = models.BigIntegerField(null = True)
    vesselname = models.CharField(max_length=254, null = True)
    imo = models.CharField(max_length=254, null = True)
    callsign = models.CharField(max_length=254, null = True)
    vesseltype = models.CharField(max_length=254, null = True)
    status = models.IntegerField(null = True)
    length = models.CharField(max_length=254, null = True)
    width = models.CharField(max_length=254, null = True)
    draft = models.CharField(max_length=254, null = True)
    cargo = models.CharField(max_length=254, null = True)
    transcieve = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)

    def __str__ (self):
        return str(self.datetime)






class Fishermen(models.Model):
    catch_type = models.CharField(null = True, max_length = 254)
    work_date = models.DateField(null = True)
    catch_weight = models.IntegerField(null = True)

    def __str__(self):
        return str(self.work_date)