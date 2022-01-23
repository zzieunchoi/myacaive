user_data = {'id' : ['zzieunchoi', 'tove1004', '', 'ckh', '','jjyeong'], 'pw' : ['', '970707' , '701220', '700805', '', '000331']}
print(user_data)

def my_len(a):
    cnt = 0
    for i in a:
        cnt += 1
    return cnt

def is_user_data_valid(dict):
    torf_dict = {}
    for i in range(0, my_len(dict['id'])):
        if dict['id'][i] and dict['pw'][i] :
            torf_dict[i] = True
        else:
            torf_dict[i] = False
    return torf_dict

print(is_user_data_valid(user_data))

