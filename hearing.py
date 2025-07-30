data = []
frequency = [1, 2, 3, 4, 6, 8]

thresholds = {
    "m" : {
        25 : {
            20 : [14, 11, 7, 9, 11, 14, 16, 17],
            25 : [14, 11, 7, 10, 11, 14, 17, 18],
            30 : [15, 11, 7, 11, 13, 16, 19, 21],
            35 : [15, 12, 8, 12, 15, 19, 22, 25],
            40 : [16, 13, 9, 14, 17, 24, 27, 31],
            45 : [17, 14, 11, 16, 21, 29, 33, 38],
            50 : [18, 15, 12, 19, 25, 35, 39, 46],
            55 : [20, 17, 14, 22, 30, 42, 48, 56],
            60 : [21, 19, 16, 25, 36, 50, 57, 67],
            65 : [23, 21, 18, 30, 42, 59, 67, 80],
            70 : [25, 23, 21, 34, 49, 70, 79, 94],
            75 : [27, 25, 24, 39, 57, 81, 92, 110],
            80 : [29, 28, 27, 44, 65, 93, 105, 120]
        },

        50 : {
            20 : [8, 5, 2, 4, 4, 6, 7, 8],
            25 : [8, 5, 2, 4, 5, 7, 8, 9],
            30 : [8, 6, 3, 5, 6, 8, 10, 11],
            35 : [8, 6, 3, 6, 7, 11, 12, 14],
            40 : [9, 7, 4, 7, 9, 14, 16, 18],
            45 : [10, 8, 5, 9, 12, 18, 20, 24],
            50 : [11, 9, 6, 11, 15, 22, 25, 30],
            55 : [12, 10, 7, 13, 19, 28, 32, 38],
            60 : [13, 11, 9, 16, 23, 34, 39, 46],
            65 : [14, 13, 11, 19, 28, 41, 47, 56],
            70 : [16, 14, 13, 22, 34, 49, 56, 67],
            75 : [17, 16, 15, 26, 40, 58, 65, 79],
            80 : [19, 18, 17, 30, 46, 68, 76, 92]
        },

        75 : {
            20 : [2, 1, -2, -1, -1, 0, 0, 0],
            25 : [2, 1, -2, -1, -1, 1, 1, 1],
            30 : [2, 1, -1, 0, 0, 2, 2, 2],
            35 : [3, 1, -1, 0, 1, 4, 4, 5],
            40 : [3, 2, 0, 1, 3, 6, 7, 8],
            45 : [4, 2, 0, 3, 5, 9, 10, 12],
            50 : [4, 3, 1, 4, 7, 13, 14, 17],
            55 : [5, 4, 2, 6, 10, 17, 19, 23],
            60 : [6, 5, 4, 8, 14, 21, 24, 29],
            65 : [7, 6, 5, 11, 17, 27, 30, 37],
            70 : [8, 8, 6, 13, 21, 33, 37, 45],
            75 : [9, 9, 8, 16, 26, 40, 45, 54],
            80 : [11, 11, 10, 19, 31, 47, 53, 64]
        }
    },

    "f" : {
        25 : {
            20 : [14, 11, 7, 9, 10, 13, 15, 17],
            25 : [14, 11, 7, 9, 11, 14, 16, 18],
            30 : [14, 11, 7, 10, 11, 15, 17, 20],
            35 : [15, 12, 8, 11, 13, 16, 20, 23],
            40 : [16, 13, 9, 13, 15, 19, 23, 26],
            45 : [17, 14, 11, 15, 17, 22, 26, 31],
            50 : [18, 15, 12, 17, 20, 25, 31, 37],
            55 : [19, 17, 14, 20, 23, 39, 36, 44],
            60 : [21, 19, 16, 23, 27, 34, 43, 51],
            65 : [23, 21, 18, 26, 32, 39, 50, 60],
            70 : [24, 23, 21, 30, 36, 45, 57, 70],
            75 : [27, 25, 24, 34, 42, 51, 66, 80],
            80 : [29, 28, 27, 39, 48, 58, 75, 92]
        },

        50 : {
            20 : [8, 5, 2, 4, 4, 6, 7, 8],
            25 : [8, 5, 2, 4, 4, 6, 8, 8],
            30 : [8, 6, 3, 4, 5, 7, 9, 10],
            35 : [8, 6, 3, 5, 6, 9, 10, 12],
            40 : [9, 7, 4, 6, 8, 10, 13, 15],
            45 : [10, 8, 5, 8, 9, 13, 16, 18],
            50 : [11, 9, 6, 10, 12, 15, 19, 23],
            55 : [12, 10, 7, 12, 14, 18, 23, 28],
            60 : [13, 11, 9, 14, 17, 22, 28, 34],
            65 : [14, 13, 11, 17, 21, 26, 34, 41],
            70 : [16, 14, 13, 20, 24, 30, 39, 48],
            75 : [17, 16, 15, 23, 28, 35, 46, 56],
            80 : [19, 18, 17, 27, 33, 41, 53, 65]
        },

        75 : {
            20 : [2, 1, -2, -1, -1, 0, 1, 0],
            25 : [3, 1, -2, -1, -1, 1, 1, 1],
            30 : [3, 1, -1, 0, 0, 1, 2, 2],
            35 : [3, 1, -1, 0, 1, 2, 3, 3],
            40 : [4, 2, 0, 1, 2, 4, 5, 6],
            45 : [4, 2, 0, 2, 3, 5, 7, 8],
            50 : [5, 3, 1, 4, 5, 7,10, 12],
            55 : [6, 4, 2, 5, 7, 10, 13, 16],
            60 : [6, 5, 4, 7, 9, 12, 17, 20],
            65 : [7, 6, 5, 9, 12, 15, 21, 25],
            70 : [9, 8, 6, 11, 15, 19, 25, 31],
            75 : [10, 9, 8, 14, 18, 23, 30, 37],
            80 : [11, 11, 10, 17, 21, 27, 36, 44]
        }
    }
}

def get_thresholds(s, p, a):

    for key, value in thresholds["f"][25].items():
        if a < key:
            a = key - 5
            break
    try:
        return thresholds[s][int(p)][a]
    
    except KeyError:
        return False

def calculateCLB(right_data, left_data, age, sex, fq):

    if sex == False:
        return False
    
    if fq == False:
        return False

    threshold = get_thresholds(sex, fq, age)
    if threshold == False:
        return False
    threshold = threshold[2:]

    right = 0
    left = 0
    thresh = 0

    for i in range(0,3):
        right += right_data[i]
        left += left_data[i]
        thresh += threshold[i]

    right = right/3
    left = left/3
    thresh = thresh/3

    if right < left:
        output = (right*4 + left)/5
    else:
        output = (right + left*4)/5

    return output - thresh

def calculateDHSS(right_data, left_data, age, sex, fq):

    right_bulge = calculateBulge(right_data, age, sex, fq)
    left_bulge = calculateBulge(left_data, age, sex, fq)

    if (right_bulge == False or left_bulge == False):
        return False

    right_data_avg = 0
    left_data_avg = 0
    right_bulge_avg = 0
    left_bulge_avg = 0

    for i in range(0, 3):
        right_data_avg += right_data[i]
        left_data_avg += left_data[i]
        right_bulge_avg += right_data[i] - right_bulge[i]
        left_bulge_avg += left_data[i] - left_bulge[i]

    right_data_avg = right_data_avg/3
    left_data_avg = left_data_avg/3
    right_bulge_avg = right_bulge_avg/3
    left_bulge_avg = left_bulge_avg/3

    if right_data_avg < left_data_avg:
        data_avg = (right_data_avg*4 + left_data_avg)/5
    else:
        data_avg = (right_data_avg + left_data_avg*4)/5

    if right_bulge_avg < left_bulge_avg:
        bulge_avg = (right_bulge_avg*4 + left_bulge_avg)/5
    else:
        bulge_avg = (right_bulge_avg + left_bulge_avg*4)/5

    return data_avg - bulge_avg

def calculateBulge(data, age, sex, fq):

    if sex == False:
        return False
    
    if fq == False:
        return False

    threshold = get_thresholds(sex, fq, age)
    if threshold == False:
        return False
    threshold = threshold[2:]

    lower = data[0] - threshold[0]
    upper = data[-1] - threshold[-1]

    def get_bulge(lower, upper):
        bulge = []
        d = (upper - lower)/5
        misfit = [lower, round(lower + d), round(lower + 2*d), round(lower + 3*d), round(lower + 4*d), upper]
        for i in range (0, len(threshold)):
            bulge.append(data[i] - threshold[i] - misfit[i])

        return bulge

    pass_one = get_bulge(lower, upper)

    for i in pass_one:
        if i > 0:
            lower = round(data[0] - (pass_one[3]*0.15)) - threshold[0]
            upper = round(data[-1] - (pass_one[3]*0.4)) - threshold[-1]
            pass_two = get_bulge(lower, upper)
            return pass_two
    
    return pass_one