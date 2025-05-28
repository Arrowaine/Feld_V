def calculate_s_score(parameter: str, distortion_percent: float) -> int:
    """
    Рассчитывает S-Score на основе таблицы преобразования относительных искажений.
    
    Параметры:
    - parameter: Название параметра (например, "Limb Length", "Arm Length" и т.д.)
    - distortion_percent: Процентное искажение (может быть отрицательным или положительным)
    
    Возвращает:
    - S-Score (целое число от 1 до 10)
    """ 
    # Таблица преобразования (границы диапазонов для каждого параметра и S-Score)
    s_score_table = {
        0: [
                (-float('inf'), -26.1),   # S-Score 1
                (-26.1, -19.51),           # S-Score 2
                (-19.51, -12.91),          # S-Score 3
                (-12.91, -4.1),            # S-Score 4
                (-4.1, 5.35),              # S-Score 5
                (5.35, 15.3),             # S-Score 6
                (15.3, 25.85),             # S-Score 7
                (25.85, 36.5),            # S-Score 8
                (36.5, 57.1),              # S-Score 9
                (57.1, float('inf'))],       # S-Score 10
        1: [(-float('inf'), -26.9),
            (-26.9, -20.1),
            (-20.1, -12.51),
            (-12.51, -3.1),
            (-3.1, 6.5),
            (6.5, 17.04),
            (17.04, 30.3),
            (30.3, 44),
            (44, 59.1),
            (59.1, float('inf'))],
        2: [(-float('inf'), -31.7),
            (-31.7, -25.1),
            (-25.1, -17.8),
            (-17.8, -8.11),
            (-8.11, 2.46),
            (2.46, 13),
            (13, 28),
            (28, 44.8),
            (44.8, 60.1),
            (60.1, float('inf'))],
        3: [(-float('inf'), -28.5),
            (-28.5, -22.21),
            (-22.21, -11.51),
            (-11.51, -2.21),
            (-2.21, 9.85),
            (9.85, 21.5),
            (21.5, 30.7),
            (30.7, 44.9),
            (44.9, 63.1),
            (63.1, float('inf'))],
        4: [(-float('inf'), -28.1),
            (-28.1, -17),
            (-17, -6.3),
            (-6.3, 4.33),
            (4.33, 22.1),
            (22.1, 38.4),
            (38.4, 54.9),
            (54.9, 74.5),
            (74.5, 103.1),
            (103.1, float('inf'))],
        5: [(-float('inf'), -9.21),
            (-9.21, -0.36),
            (-0.36, 14.29),
            (14.29, 24.9),
            (24.9, 41),
            (41, 55.5),
            (55.5, 73),
            (73, 97),
            (97, 121),
            (121, float('inf'))],
        6: [(-float('inf'), -23.71),
            (-23.71, -15.31),
            (-15.31, 2.5),
            (2.5, 11.5),
            (11.5, 25),
            (25, 45),
            (45, 69),
            (69, 92),
            (92, 119.1),
            (119.1, float('inf'))]}
    if parameter not in s_score_table:
        raise ValueError(f"Неизвестный параметр: {parameter}. Допустимые параметры: {list(s_score_table.keys())}")   
    ranges = s_score_table[parameter]
    for score, (lower, upper) in enumerate(ranges, start=1):
        if lower <= distortion_percent < upper:
            return score
    return 10 if distortion_percent >= ranges[-1][0] else 1

    
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
    s_score = [calculate_s_score(factors.index(factor),factor) for factor in factors]
    return factors, s_score

def text_s_score(s_score):
    if s_score == 1:
        return "ОЧЕНЬ низкий"
    elif s_score <= 3:
        return "Ниже среднего"
    elif s_score <= 6:
        return "Средний"
    elif s_score <= 9:
        return "Выше среднего"
    elif s_score == 10:
        return "ОЧЕНЬ высокий"
    