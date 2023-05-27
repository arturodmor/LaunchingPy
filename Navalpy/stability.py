import pandas as pd

class Stability():
    def __init__(self, Height, Volume_ship, T_inertia, L_inertia, KB, KG):
        self.Height = Height
        self.volume_ship = Volume_ship
        self.T_inertia = T_inertia
        self.L_inertia = L_inertia
        self.KB = KB
        self.KG = KG

    def T_inertia_integration(self,step_interval,shape_type):
        """Integrate a basic ship according to her shape."""

        df_T_inertia = pd.DataFrame()
        df_T_inertia['section'] = [0,2.5,5,7.5,10,35,60,65,70]
        df_T_inertia['manga'] = [0,13.23,17.32,19.36,20,20,20,0]

        for value in df_T_inertia['section']:
            if shape_type == "r":
                T_inertia = (1/12)*(value)^3
                df_T_inertia['T_inertia'] = T_inertia
            

    def get_BMT(self):
        BMT = self.T_inertia/self.volume_ship
        return BMT
    
    def get_KMT(self):
        KMT = self.BMT + self.KB
        return KMT
    
    def get_GMT(self):
        GMT =self.KMT + self.KG
        return GMT