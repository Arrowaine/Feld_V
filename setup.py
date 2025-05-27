def score_factor(factor):
    if factor < -26:
        return 1
    elif factor < -19.5:
        return 2
    elif factor < -12.9:
        return 3
    elif factor < -4:
        return 4
    elif factor < 5.35:
        return 5
    elif factor < 15.3:
        return 6
    elif factor < 25.85:
        return 7
    elif factor < 36.5:
        return 8
    elif factor < 57.1:
        return 9
    elif factor > 57:
        return 10
    else:
        return None
    
def create_factors(real,im):
    delta = [(im[i]-real[i])/real[i]*100 for i in range(len(real))]

    avg = [delta[0], delta[1], delta[2], 
            (delta[3]+delta[4])/2,
            (delta[5]+delta[6])/2,
            (delta[7]+delta[8])/2,
            (delta[9]+delta[10])/2,
            (delta[11]+delta[12])/2,
            delta[13], delta[14], delta[15],delta[16], delta[17],
            (delta[18]+delta[19])/2,
            (delta[20]+delta[21])/2,
            (delta[22]+delta[23])/2,
            (delta[24]+delta[25])/2 ]
    
    factors = [ (avg[4]+avg[6]+avg[7]+avg[13]+avg[15]+avg[16])/6,
            (avg[4]+avg[6]+avg[7])/3,
            (avg[13]+avg[15]+avg[16])/3,
            (avg[10]+avg[11]+avg[12])/3,
            (avg[3]+avg[5]+avg[14])/3,
            (avg[0]+avg[1]+avg[2])/3,
            (avg[8]+avg[9])/2        ]
    
    s_score = [score_factor(factor) for factor in factors]

    return factors, s_score
        