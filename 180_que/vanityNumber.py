def vanityNumber(arr, num):
    res =[]
    phone = {'A': 2,
            'B' : 2, 
            'C' : 2, 
            'D' : 3, 
            'E' : 3, 
            'F' : 3, 
            'G' : 4, 
            'H' : 4, 
            'I' : 4, 
            'J' : 5, 
            'K' : 5, 
            'L' : 5, 
            'M' : 6, 
            'N' : 6, 
            'O' : 6, 
            'P' : 7, 
            'Q' : 7, 
            'R' : 7, 
            'S' : 7, 
            'T' : 8, 
            'U' : 8, 
            'V' : 8, 
            'W' : 9, 
            'X' : 9, 
            'Y' : 9, 
            'Z': 9}
    decode =[]
    for word in arr:
        code =''
        for letter in word:
            code += str(phone[letter])
        decode.append(code)
    print decode
    for d in decode:
        for n in num:
            if d in n:
                res.append(n)
    return res






arr =['TWLO', 'CODE' ,'HTCH']
num = ['+17474824380' , '+14157088956','+919810155555' ,'+15109926333', '+1415123456']

print vanityNumber(arr, num)