matrix = [[1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]
answer_list = []
for ind_str, mea_str in enumerate(matrix):
    for ind_line, mea_line in enumerate(mea_str):
        if mea_line == 1:
            try:
                if matrix[ind_str - 1][ind_line - 1] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass
            try:
                if matrix[ind_str - 1][ind_line] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass
            try:
                if matrix[ind_str - 1][ind_line + 1] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass
            try:
                if matrix[ind_str][ind_line - 1] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass
            try:
                if matrix[ind_str][ind_line + 1] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass
            try:
                if matrix[ind_str + 1][ind_line - 1] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass
            try:
                if matrix[ind_str + 1][ind_line] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass
            try:
                if matrix[ind_str + 1][ind_line + 1] == 1 and ind_str - 1 > 0 and ind_line - 1 > 0:
                    answer_list.append("НЕТ")
                else:
                    answer_list.append("ДА")
            except:
                pass

yes_or_not = "НЕТ" in answer_list
if yes_or_not == False:
    print("ДА")
else:
    print("НЕТ")