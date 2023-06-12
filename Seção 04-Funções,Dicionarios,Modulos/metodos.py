# metodos uteis dos diciionarios em python
# len(dicionario) - retorna o tamanho do dicionario
# dicionario.keys() - retorna as chaves do dicionario
# dicionario.values() - retorna os valores do dicionario
# dicionario.items() - retorna os itens do dicionario
# dicionario.clear() - limpa o dicionario
# dicionario.copy() - copia o dicionario
# dicionario.get('chave') - retorna o valor da chave informada
# dicionario.pop('chave') - retorna o valor da chave informada e a remove do dicionario
# dicionario.popitem() - retorna o ultimo item do dicionario e o remove
# dicionario.update({'chave':'valor'}) - atualiza o dicionario com a chave e valor informados
# dicionario.setdefault('chave','valor') - retorna o valor da chave informada, se não existir, insere a chave com o valor informado
# dicionario.fromkeys('chave','valor') - retorna um dicionario com a chave e valor informados
# dicionario.has_key('chave') - retorna True se a chave existir no dicionario
# dicionario.iteritems() - retorna um iterador com os itens do dicionario
# dicionario.iterkeys() - retorna um iterador com as chaves do dicionario
# dicionario.itervalues() - retorna um iterador com os valores do dicionario
# dicionario.viewitems() - retorna uma view com os itens do dicionario
# dicionario.viewkeys() - retorna uma view com as chaves do dicionario
# dicionario.viewvalues() - retorna uma view com os valores do dicionario
# dicionario.setdefault('chave','valor') - retorna o valor da chave informada, se não existir, insere a chave com o valor informado
import copy
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(len(dicionario))
print(dicionario.keys())
print(dicionario.values())
d2 = copy.deepcopy(dicionario)
print(d2)
