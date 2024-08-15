def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = ['ort', 123, False]
values_dict = {'a':123, 'b':True, 'c':'ORT'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [12, 'jk']
print_params(*values_list_2)
