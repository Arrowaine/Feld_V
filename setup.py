def math(real,im):
    delta = []
    for i in range(len(real)):
        delta.append((im[i]-real[i])/real[i]*100)
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
    