import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

class NearPoint:

    def ckdnearest(gdA, gdB):

        nA = np.array(list(gdA.geometry.apply(lambda x: (x.x, x.y, x.z))))
        nB = np.array(list(gdB.geometry.apply(lambda x: (x.x, x.y, x.z))))
        btree = cKDTree(nB)
        dist, idx = btree.query(nA, k=1)
        gdB_nearest = gdB.iloc[idx].drop(columns="geometry").reset_index(drop=True)
        gdf = pd.concat(
            [
                gdB_nearest,
                pd.Series(dist, name='dist')
            ], 
            axis=1)
        return gdf
