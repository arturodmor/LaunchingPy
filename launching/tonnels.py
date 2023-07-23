import math

def max_ton_key(p, secure_coef, alpha_rad, f0, N_eels):

    alpha_rad = math.radians(5)
    F_key = p*secure_coef*(math.sin(alpha_rad)-(f0*math.cos(alpha_rad)))/(N_eels)

    return F_key