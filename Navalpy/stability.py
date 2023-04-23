class Stability():
    def __init__(self, Height, Volume_ship, T_inertia, L_inertia, GMT, BMT, KMT, KB, KG):
        self.Height = Height
        self.volume_ship = Volume_ship
        self.T_inertia = T_inertia
        self.L_inertia = L_inertia
        self.gmt = GMT
        self.BMT = BMT
        self.KMT = KMT
        self.KB = KB
        self.KG = KG

    def get_BMT(self):
        self.BMT = self.T_inertia/self.volume_ship
        return self.BMT
    
    def get_KMT(self):
        self.KMT = self.BMT + self.KB
        return self.KMT
    
    def get_GMT(self):
        self.GMT =self.KMT + self.KG
        return self.GMT