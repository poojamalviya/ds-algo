# def special_format(n):
#     n = float(n)
#     print(type(n))
#     currency = "{:,.2f}".format(n)
#     return currency

def special_format(n):
	import decimal
	d = decimal.Decimal(str(n))
	n = float(n)
	if d.as_tuple().exponent < -2:
		s = str(n)
	else:
		s = '{0:.2f}'.format(n)
	l = len(s)
	i = l - 1
	res, flag, k = '', 0, 0
	while i >= 0:
		if flag == 0:
			res += s[i]
			if s[i] == '.':
				flag = 1
		elif flag == 1:
			k += 1
			res += s[i]
			if k == 3 and i - 1 >= 0:
				res += ','
				flag = 2
				k = 0
		else:
			k += 1
			res += s[i]
			if k == 2 and i - 1 >= 0:
				res += ','
				flag = 2
				k = 0
		i -= 1
	return str(res[::-1])

print special_format(0)
print special_format(None)
print special_format("1230123")
print special_format(1230123)
print special_format("123012332423423.00")

