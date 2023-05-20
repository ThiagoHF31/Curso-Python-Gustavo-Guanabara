n = input ('digite algo:')
t = type(n)
p = (n.isalpha(),n.isnumeric(),n.isalnum())
print('O número{} é do tipo{} e apresetna as seguites características:{}'.format(n, t, p))
