import cnpj

""" cnpj_user = input('Informe o cnpj: ').replace('.', '').replace('-', '').replace('/', '')
var = cnpj.validar(cnpj_user)
print(var) """
for i in range(10):
    cnpj_novo = cnpj.gera()
    verifica = cnpj.validar(cnpj_novo)
    print(f'{cnpj_novo} - {verifica}')
    