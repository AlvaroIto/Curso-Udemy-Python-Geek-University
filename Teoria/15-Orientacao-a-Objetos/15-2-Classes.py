'''
Classes são modelos dos objetos do mundo real sendo representados computacionalmente
Para definir uma classe, utilizamos a palavra reservada class e por convenção utilizamos o nome com a inicial maiusculo, caso seja nome composto, ambas as iniciais em maiusculo e todas juntas
EX.:
    class Nome:
        pass
    
    class NomeComposto:
        pass


Classes podem conter:
    - Atributos -> Representam as características do objeto, ou seja, pelos atributos conseguimos representar computacionalmente os estaos do objeto. No caso dad lâmpadad, possivelmente iríamos querer saber a lâmpada  é 110 ou 220, a cor, luminosidade etc.
    - Métodos (funções) -> Representam os comportamentos do objeto, ou seja, as ações que esse objeto pode realizar no seu sistema, no caso da lâmpada, iríamos querer representar no nosos sistema de ligar e desligar.




Sistema para automatizar o controle das lâmpadas;



'''

class Lampada:
    pass

lamp = Lampada()
print(type(lamp))
