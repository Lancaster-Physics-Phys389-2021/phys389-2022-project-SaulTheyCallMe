import ParticleClass
import ParticleGenerator
import ParticleWall
import Angle
import NearestPoint
import random
import pytest
import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from shapely.geometry import Point



BH1 = gpd.GeoDataFrame([[0,Point(0,1,2)],[1,Point(5,2,4)],[2,Point(9,6,8)]],columns=['ID','geometry'])

BH2 = gpd.GeoDataFrame([[4,Point(5,0,6)],[5,Point(2,1,1)],[6,Point(8,5,15)]],columns=['ID','geometry'])
Nearest = NearestPoint.NearPoint
Connections = Nearest.ckdnearest(BH1, BH2)

def test_Near1():
    assert int(Connections.iloc[0].ID) == 5
    assert int(Connections.iloc[1].ID) == 4
    assert int(Connections.iloc[2].ID) == 6



