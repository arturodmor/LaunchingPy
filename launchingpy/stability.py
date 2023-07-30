import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

class Stability:
    def __init__(self, Height, Volume_ship, T_inertia, L_inertia, KB, KG):
        self.Height = Height
        self.volume_ship = Volume_ship
        self.T_inertia = T_inertia
        self.L_inertia = L_inertia
        self.KB = KB
        self.KG = KG
        self.T_df = self.section_and_beams()
        self.T_integration = self.T_inertia_integration(self.T_df)


    def set_section_and_beams(self,sections,beams):
        """return dataframe that relates the beams with each x point sections"""
        
        df_T_inertia = pd.DataFrame()

        try:
            if np.issubdtype(sections.dtype, np.integer) and np.issubdtype(beams.dtype, np.integer):

                df_T_inertia['sections'] = sections
                df_T_inertia['beams'] = beams

                return df_T_inertia
            
            elif type(sections and beams) == 'list':
                df_T_inertia['sections'] = np.array(sections)
                df_T_inertia['beams'] = np.array(beams)

                return df_T_inertia
            
        except ValueError:
            logger.error("Check the vector length")


    def T_inertia_integration(self):
        """Integrate a basic ship according to her shape."""

        df_T_inertia = self.set_section_and_beams()
        df_T_inertia['T_inertia'] = df_T_inertia['manga'].apply(lambda x: (1/12) * x**3)
        
        return df_T_inertia


    def get_BMT(self):
        BMT = self.T_inertia/self.volume_ship
        return BMT
    

    def get_KMT(self):
        KMT = self.BMT + self.KB
        return KMT
    

    def get_GMT(self):
        GMT =self.KMT + self.KG
        return GMT