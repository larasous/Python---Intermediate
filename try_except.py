"""
Tratando exceções em Python
"""

try:
    a = 1 / 0
except NameError as error:  # Trata a exceção e pega erro do tipo NameError
    print("Error:", error)
except (IndexError, KeyError) as error:
    print("Erro de indice ou chave")
except Exception as error: # Trata a exceção e pega qualquer tipo de erro
    print('Outro erro')
else:  # roda se o try estiver sem erros
    pass
finally:  # Executa após tudo, tendo erros ou não
    a = None
    
print(a)