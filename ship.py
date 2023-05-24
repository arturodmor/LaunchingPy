from Navalpy.stability import Stability

ship = Stability(Height = 8,
                 Volume_ship =24, 
                 T_inertia = 1344234, 
                 L_inertia = None, 
                 KB = 7, 
                 KG = 3)

barco = ship.get_BMT()

print(barco)