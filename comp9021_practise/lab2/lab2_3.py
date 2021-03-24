
for i in range(100, 1000):
    same = False
    string_lineA = str(i)[::-1]
    lineA_len = len(string_lineA)
    for j in range(10, 100):
        if j < 10:
            continue
        string_lineB = str(j)[::-1]
        lineB_len = len(string_lineB)

        
        multi = i * j
        string_multi = str(multi)[::-1]
        multi_len = len(string_multi)

        multi_mid_array = list()
        for index in range(2):
            mult_mid_line = str(i * int(string_lineB[index]))
            if index != 0:
                mult_mid_line += '0'
            mult_mid_line = mult_mid_line[::-1]
            multi_mid_array.append(mult_mid_line)

        
        while len(multi_mid_array[0]) < multi_len:
            multi_mid_array[0] += '0'
        
        while len(multi_mid_array[1]) < multi_len:
            multi_mid_array[1] += '0'
        
        while lineA_len < multi_len:
            string_lineA += '0'
            lineA_len += 1

        while lineB_len < multi_len:
            string_lineB += '0'
            lineB_len += 1 

        # print(f"{i} {j} {multi_mid_array[0]} {multi_mid_array[1]}")
        
        compare_num = int(string_lineA[0]) + int(string_lineB[0]) + int(string_multi[0]) + int(multi_mid_array[0][0])+int(multi_mid_array[1][0])
        for index in range(0,multi_len):
            if (lineA_len == multi_len and lineA_len == lineB_len and lineA_len == len(multi_mid_array[0]) and lineA_len == len(multi_mid_array[1])):
                # print(f"{i} {j} {multi_mid_array[0]} {multi_mid_array[1]} {int(string_multi)}")

                if (int(string_lineA[index]) + int(string_lineB[index]) + int(string_multi[index]) + int(multi_mid_array[0][index])+int(multi_mid_array[1][index])) != compare_num:
                    # print(f"{i} {j} {string_lineA} {string_lineB} {multi_mid_array[0]} {multi_mid_array[1]} {int(string_multi)} add: {int(string_lineA[index]) + int(string_lineB[index]) + int(string_multi[index]) + int(multi_mid_array[0][index])+int(multi_mid_array[1][index])}")
                    
                    same = False
                    break
                else:
                    same = True
        
        if same == True:
            print(f"{i} * {j} = {multi}, all columns adding up to {compare_num}.")

        

