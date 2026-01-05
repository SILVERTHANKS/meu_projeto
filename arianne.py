try:
    capacidade = 32767
    valor = 37727
    if valor > capacidade :
      raise OverflowError("erro overflow estouro de 16bits!")
    else:
        print("controle de estouro de 16bits ok!")
except OverflowError as e:
    print(e)        