str_= "hello world"
i = 0
ne_= ''
while i<len(str_):
    if str_[i] in 'aeiou':
        ne_ = ne_ + '*'
    else:
        ne_ = ne_+ str_[i]
    i += 1
print(ne_)
