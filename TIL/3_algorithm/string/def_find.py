def my_find(p, t):
    for i in range(my_len(t)-my_len(p)+1):
        if t[i:i+my_len(p)] == p:
            return i
    return -1


p = "is"
t = "This is a book"
print(my_find(p, t))