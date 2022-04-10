#문자열 뒤집기 풀이
#0216

def reverse(word):
    def my_len(a):
        cnt = 0
        for i in a:
            cnt += 1
        return cnt
    
    new_word = ''
    for i in range(my_len(word)):
        new_word += word[my_len(word)-i-1]
    return new_word

a = 'reverse this strings'
print(reverse(a))