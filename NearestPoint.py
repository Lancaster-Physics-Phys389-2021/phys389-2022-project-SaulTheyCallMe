import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from shapely.geometry import Point

class NearPoint:
    """
    Class to analyze and find two closes points between two arrays.
    It will make use of geopandas, sheply.geometry and cKDTree near point analysis.
    
    La and Bm are arrays to analyse
    """
        
    def ckdnearest(Bm):
        La1 = np.load("LatticeTwoBody.npy",allow_pickle=True)
        #Converting Beam particles position into a geopanda data frame
        BeamPoints = []
        for B in range(0, len(Bm)):
            BeamPoints.append({
                'geometry' : Point(Bm[B].position[0], Bm[B].position[1], Bm[B].position[2])})
        gdA = gpd.GeoDataFrame(BeamPoints)
        #Convertin Lattice particles position into a geopanda data frame
        LatticePoints = []
        for p in range(0, len(La1)):
            LatticePoints.append({
                'geometry' : Point(La1[p].position[0], La1[p].position[1], La1[p].position[2]),'id': p})
        gdB = gpd.GeoDataFrame(LatticePoints)
        #Making use of the lambda function to set positions
        nA = np.array(list(gdA.geometry.apply(lambda x: (x.x, x.y, x.z))))
        nB = np.array(list(gdB.geometry.apply(lambda x: (x.x, x.y, x.z))))
        #Definint cKDTree to be used to find the nearest points
        btree = cKDTree(nB)
        #Find the closest distance between nA and nB and the index number of the lattice particle closest to
        #the beam particle.
        dist, idx = btree.query(nA, k=1)
        gdB_nearest = gdB.iloc[idx].drop(columns="geometry").reset_index(drop=True)
        #Storing the data
        gdf = pd.concat(
            [
                gdB_nearest,
                pd.Series(dist, name='dist')
            ], 
            axis=1)
        return gdf
