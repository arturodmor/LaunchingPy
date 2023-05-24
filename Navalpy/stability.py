class Stability():
    def __init__(self, Height, Volume_ship, T_inertia, L_inertia, KB, KG):
        self.Height = Height
        self.volume_ship = Volume_ship
        self.T_inertia = T_inertia
        self.L_inertia = L_inertia
        self.KB = KB
        self.KG = KG

    def get_BMT(self):
        BMT = self.T_inertia/self.volume_ship
        return BMT
    
    def get_KMT(self):
        KMT = self.BMT + self.KB
        return KMT
    
    def get_GMT(self):
        GMT =self.KMT + self.KG
        return GMT