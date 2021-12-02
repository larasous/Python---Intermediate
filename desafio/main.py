import cnpj

cnpj_user = input('Informe o cnpj: ').replace('.', '').replace('-', '').replace('/', '')
var = cnpj.validar(cnpj_user)
print(var)