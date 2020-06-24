from lucro_da_acao import LucroDaAcao
lucro_da_acao = LucroDaAcao()

def test_calcula_acao():
    """ Calcula ação """
    # Vantagem
    vantagem = [10,9,8,7,11]
    # Desvantagem
    desvantagem = [10,9,8,7,6]
    # Testa se retorna None se for desvantajoso comprar uma ação
    assert lucro_da_acao.calcula_acao(desvantagem) == None
    # Testar se retorna a vantagem
    assert lucro_da_acao.calcula_acao(vantagem) == (4,5)
    
