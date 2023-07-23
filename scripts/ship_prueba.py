from launching.stability import Stability
import logging
import numpy as np

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ship = Stability(Height = 8,
                 Volume_ship =24, 
                 T_inertia = 1344234, 
                 L_inertia = None, 
                 KB = 7, 
                 KG = 3)

BMT = ship.get_BMT()
logger.info(f"BMT = {BMT}")