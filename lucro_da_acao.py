#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Tuple, Union
class LucroDaAcao:

    def calcula_acao(self, acao:list) -> Union[Tuple, None]:  
        """ Pega a lista de valores e verifica qual é o menor preço e depois 
        qual é o maior preço. """
        # Pega o valor minimo
        valor_minimo = min(acao)
        valor_maximo = max(acao)
        
        index_valor_minimo = acao.index(valor_minimo)
        index_valor_maximo = acao.index(valor_maximo)

        if index_valor_minimo < index_valor_maximo:
           dia_da_acao = (index_valor_minimo+1, index_valor_maximo+1)  
        else:
           dia_da_acao = 0 
        
        return dia_da_acao

    def pega_acao(self, acao:list) -> Tuple: 
        """ Retorna ao usuário o dia da compra e o dia da venda """
        calcula_acao = self.calcula_acao(acao) 
        if calcula_acao == 0:
           print("Não compensa comprar ação com este dados!")
        else:
           print(f"É vantajoso comprar ação no dia "+\
                   f"{calcula_acao[0]} e vender no dia {calcula_acao[1]}")

        return calcula_acao


        
